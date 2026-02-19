import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd

# ISA / physics helpers (lightweight, not aircraft-specific)
G0 = 9.80665
R_AIR = 287.05
GAMMA = 1.4
T0 = 288.15
P0 = 101325.0
RHO0 = 1.225
LAPSE = -0.0065
MPS_TO_KTS = 1.94384

def isa_atmosphere(alt_m):
    """Return (T, p, rho) for ISA up to ~20 km."""
    if alt_m <= 11000.0:
        T = T0 + LAPSE * alt_m
        p = P0 * (T / T0) ** (-G0 / (LAPSE * R_AIR))
    else:
        T = T0 + LAPSE * 11000.0
        p11 = P0 * (T / T0) ** (-G0 / (LAPSE * R_AIR))
        p = p11 * np.exp(-G0 * (alt_m - 11000.0) / (R_AIR * T))
    rho = p / (R_AIR * T)
    return T, p, rho

def mach_to_tas(mach, temp_k):
    a = np.sqrt(GAMMA * R_AIR * temp_k)
    return mach * a

def tas_to_cas(tas_mps, rho):
    # CAS ~ EAS for this simplified model
    eas = tas_mps * np.sqrt(rho / RHO0)
    return eas * MPS_TO_KTS

def tat_from_mach(temp_k, mach, recovery=0.9):
    t_t = temp_k * (1.0 + recovery * (GAMMA - 1.0) * 0.5 * mach**2)
    return t_t - 273.15

class AircraftEnv(gym.Env):
    """
    Custom Environment that follows gym interface.
    The goal is to find the optimal Mach number to minimize fuel flow given flight conditions.
    """
    metadata = {'render_mode': ['human']}

    def __init__(self, data_path=None, episode_len=30, dt_seconds=60.0):
        super(AircraftEnv, self).__init__()
        
        # Load data to sample realistic initial states
        self.df = None
        if data_path:
            self.df = pd.read_csv(data_path)
        
        # Action Space: Continuous Mach number selection [0.70, 0.86]
        # We normalize action to [-1, 1] for stable learning in PPO/SAC
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(1,), dtype=np.float32)
        
        # Observation Space (normalized):
        # [Altitude_ft, GrossWeight_kg, TAT_C, CAS_kts, TempDev_C, Wind_kts, Phase, TargetAlt_ft]
        self.obs_mean = np.array([35000.0, 69000.0, -35.0, 280.0, 0.0, 0.0, 1.0, 35000.0], dtype=np.float32)
        self.obs_std = np.array([5000.0, 8000.0, 10.0, 30.0, 5.0, 20.0, 0.8, 6000.0], dtype=np.float32)
        self.observation_space = spaces.Box(
            low=-5.0,
            high=5.0,
            shape=(8,),
            dtype=np.float32,
        )
        
        self.state = None
        self.current_step = 0
        self.episode_len = episode_len
        self.dt_hours = dt_seconds / 3600.0
        self.dt_minutes = dt_seconds / 60.0
        
        # Simple aircraft/engine constants (representative narrowbody class)
        self.mach_min = 0.70
        self.mach_max = 0.86
        self.mach_crit = 0.78
        self.mach_climb_max = 0.78
        self.mach_descent_max = 0.82
        self.s_ref = 125.0  # m^2
        self.ar = 9.5
        self.e = 0.82
        self.cd0 = 0.02
        self.k = 1.0 / (np.pi * self.e * self.ar)
        self.cd_wave = 0.015
        self.tsfc_base = 1.6e-5  # kg/(N*s) ~ 0.058 kg/(N*hr)

        # Tail variability (small per-tail deltas)
        self.tail_profile = {
            "cd0": self.cd0,
            "tsfc_base": self.tsfc_base,
            "mach_crit": self.mach_crit,
            "s_ref": self.s_ref,
        }

        # Altitude constraints and profiles
        self.min_altitude_ft = 10000.0
        self.max_altitude_ft = 41000.0
        self.cruise_window_ft = 300.0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        # Initialize state with a random sample from our "historical data" or random realistic values
        if self.df is not None:
            sample = self.df.sample(1).iloc[0]
            self.altitude = float(sample['altitude'])
            self.weight = float(sample['grossWeight'])
            self.mach = float(sample['mach'])
            self.temp_dev = float(sample.get('tempDevC', 0.0))
            self.wind_kts = float(sample.get('windKts', 0.0))
            self.phase = float(sample.get('phase', 1.0))
            self.target_altitude = float(sample.get('targetAltitude', self.altitude))
            self._set_tail_profile(sample.get('tail', None))
        else:
            self.phase = float(np.random.choice([0.0, 1.0, 2.0], p=[0.2, 0.6, 0.2]))
            if self.phase == 0.0:  # climb
                self.altitude = np.random.uniform(22000, 32000)
                self.target_altitude = np.random.uniform(33000, 39000)
            elif self.phase == 2.0:  # descent
                self.altitude = np.random.uniform(33000, 39000)
                self.target_altitude = np.random.uniform(15000, 25000)
            else:  # cruise
                self.altitude = np.random.uniform(33000, 39000)
                self.target_altitude = float(self.altitude + np.random.uniform(-500, 500))

            self.weight = np.random.uniform(60000, 78000)
            self.mach = np.random.uniform(self.mach_min, self.mach_max)
            self.temp_dev = np.random.normal(0.0, 2.0)
            self.wind_kts = np.random.normal(0.0, 10.0)
            self._set_tail_profile(None)

        self.tat, self.cas = self._compute_atmos_state(self.altitude, self.mach, self.temp_dev)
        self.state = self._normalize_obs(
            np.array(
                [self.altitude, self.weight, self.tat, self.cas, self.temp_dev, self.wind_kts, self.phase, self.target_altitude],
                dtype=np.float32,
            )
        )
        self.current_step = 0
        
        return self.state, {}

    def step(self, action):
        # Convert normalized action [-1, 1] back to Mach [0.70, 0.86]
        action = np.clip(action, -1.0, 1.0)
        self.mach = 0.78 + (action[0] * 0.08)
        self.mach = float(np.clip(self.mach, self.mach_min, self.mach_max))

        fuel_flow_kg_hr = self._fuel_flow_model(self.altitude, self.weight, self.mach, self.temp_dev)
        fuel_flow_kg_hr += np.random.normal(0.0, 15.0)
        fuel_flow_kg_hr = max(fuel_flow_kg_hr, 500.0)

        # Update weight based on fuel burned this step
        self.weight = max(self.weight - fuel_flow_kg_hr * self.dt_hours, 55000.0)

        # Altitude dynamics with climb/cruise/descent phases
        if self.phase == 0.0:  # climb
            climb_rate_fpm = np.random.uniform(1500.0, 2500.0)
            self.altitude += climb_rate_fpm * self.dt_minutes
            if self.altitude >= self.target_altitude - self.cruise_window_ft:
                self.phase = 1.0
        elif self.phase == 2.0:  # descent
            descent_rate_fpm = np.random.uniform(1500.0, 2500.0)
            self.altitude -= descent_rate_fpm * self.dt_minutes
            if self.altitude <= self.target_altitude + self.cruise_window_ft:
                self.phase = 1.0
        else:  # cruise
            self.altitude += np.random.normal(0.0, 30.0)

        # Enforce hard altitude limits
        if self.altitude < self.min_altitude_ft or self.altitude > self.max_altitude_ft:
            self.altitude = float(np.clip(self.altitude, self.min_altitude_ft, self.max_altitude_ft))
            constraint_violation = True
        else:
            constraint_violation = False

        # Temperature and wind profiles (slow variation)
        self.temp_dev = float(np.clip(0.95 * self.temp_dev + np.random.normal(0.0, 0.2), -8.0, 8.0))
        self.wind_kts = float(np.clip(0.90 * self.wind_kts + np.random.normal(0.0, 2.0), -60.0, 60.0))

        # Recompute observable state from physics
        self.tat, self.cas = self._compute_atmos_state(self.altitude, self.mach, self.temp_dev)
        self.state = self._normalize_obs(
            np.array(
                [self.altitude, self.weight, self.tat, self.cas, self.temp_dev, self.wind_kts, self.phase, self.target_altitude],
                dtype=np.float32,
            )
        )

        # Reward is negative fuel burn per distance (kg per NM)
        gs_kts = max(self.cas + self.wind_kts, 100.0)
        fuel_per_nm = fuel_flow_kg_hr / gs_kts
        alt_error = abs(self.altitude - self.target_altitude)
        alt_penalty = max(0.0, (alt_error - 1000.0) / 10000.0)
        energy_penalty = self._energy_management_penalty()
        reward = -fuel_per_nm / 10.0 - alt_penalty - energy_penalty

        self.current_step += 1
        terminated = self.current_step >= self.episode_len or constraint_violation
        truncated = False

        info = {
            "mach": self.mach,
            "fuel_flow_kg_hr": fuel_flow_kg_hr,
            "altitude_ft": self.altitude,
            "weight_kg": self.weight,
            "tat_c": self.tat,
            "cas_kts": self.cas,
            "temp_dev_c": self.temp_dev,
            "wind_kts": self.wind_kts,
            "phase": self.phase,
            "target_altitude_ft": self.target_altitude,
            "constraint_violation": constraint_violation,
        }

        return self.state, reward, terminated, truncated, info

    def _compute_atmos_state(self, altitude_ft, mach, temp_dev_c):
        alt_m = altitude_ft * 0.3048
        temp_k, _, rho = isa_atmosphere(alt_m)
        temp_k = temp_k + temp_dev_c
        tas_mps = mach_to_tas(mach, temp_k)
        tat_c = tat_from_mach(temp_k, mach)
        cas_kts = tas_to_cas(tas_mps, rho)
        return float(tat_c), float(cas_kts)

    def _fuel_flow_model(self, altitude_ft, weight_kg, mach, temp_dev_c):
        alt_m = altitude_ft * 0.3048
        temp_k, _, rho = isa_atmosphere(alt_m)
        temp_k = temp_k + temp_dev_c
        tas = mach_to_tas(mach, temp_k)

        q = 0.5 * rho * tas**2
        weight_n = weight_kg * G0
        cl = weight_n / (q * self.s_ref)

        wave = max(0.0, (mach - self.mach_crit) / 0.08)
        cd = self.cd0 + self.k * cl**2 + self.cd_wave * wave**2

        drag_n = q * self.s_ref * cd

        # TSFC increases with altitude and colder temps (simplified)
        tsfc = self.tsfc_base * (1.0 + 0.12 * (alt_m / 11000.0)) * (1.0 + 0.01 * (T0 - temp_k))
        fuel_flow_kg_s = drag_n * tsfc
        return fuel_flow_kg_s * 3600.0

    def _energy_management_penalty(self):
        # Penalize excessive Mach in climb/descent, and low-altitude overspeed
        penalty = 0.0
        if self.phase == 0.0 and self.mach > self.mach_climb_max:
            penalty += (self.mach - self.mach_climb_max) * 2.0
        if self.phase == 2.0 and self.mach > self.mach_descent_max:
            penalty += (self.mach - self.mach_descent_max) * 1.5
        if self.altitude < 18000.0 and self.mach > 0.80:
            penalty += (self.mach - 0.80) * 2.0
        return penalty

    def normalize_obs(self, obs):
        return self._normalize_obs(obs)

    def _normalize_obs(self, obs):
        return (obs - self.obs_mean) / self.obs_std

    def _set_tail_profile(self, tail_name):
        # Apply small per-tail deltas to reflect variability
        if isinstance(tail_name, str) and tail_name:
            rng = np.random.default_rng(abs(hash(tail_name)) % (2**32))
        else:
            rng = np.random.default_rng()

        self.cd0 = 0.02 + rng.normal(0.0, 0.002)
        self.tsfc_base = 1.6e-5 * (1.0 + rng.normal(0.0, 0.03))
        self.mach_crit = 0.78 + rng.normal(0.0, 0.01)
        self.s_ref = 125.0 * (1.0 + rng.normal(0.0, 0.01))
        self.tail_profile = {
            "cd0": self.cd0,
            "tsfc_base": self.tsfc_base,
            "mach_crit": self.mach_crit,
            "s_ref": self.s_ref,
        }

    def render(self):
        pass

    def close(self):
        pass
