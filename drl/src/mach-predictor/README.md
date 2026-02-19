id: my-first-codelab
summary: Build a sample app with X
categories: web, beginner
tags: web
status: draft
authors: Samrat Kar

# Aircraft Mach Optimization using Deep Reinforcement Learning

This application demonstrates how to use Deep Reinforcement Learning (DRL) to optimize the Mach number for aircraft tails to minimize fuel consumption.

## Problem Statement
Aircraft fuel efficiency depends significantly on the Mach number (speed) flown relative to the aircraft's weight, altitude, and temperature. By analyzing historical QAR (Quick Access Recorder) data, we can learn a policy to recommend the optimal Mach number for specific flight conditions.

## Solution Approach
1. **Data Generation**: Generate synthetic QAR data using a simplified aerodynamic + engine model.
2. **Environment**: A custom Gymnasium environment (`AircraftEnv`) simulates fuel burn and cruise dynamics.
3. **RL Agent**: A PPO (Proximal Policy Optimization) agent learns to pick Mach to minimize fuel flow.
4. **Prediction**: The trained agent predicts Mach for new flight conditions.

## Project Structure
- `data_generator.py`: Generates synthetic flight data CSVs in `data/`.
- `aircraft_env.py`: Custom Gym environment.
- `train_agent.py`: Training script using PyTorch PPO.
- `predict_mach.py`: Inference script to query the trained model.
- `requirements.txt`: Python dependencies.

## Setup
1.  **Install Dependencies**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

### 1. Generate Data
Generate synthetic data for tails (e.g., Tail_X1):
```bash
python data_generator.py
```
This creates `data/Tail_X1.csv`.

### 2. Train the Agent
Train the DRL agent on the generated data/environment:
```bash
python train_agent.py
```
This will train for 100,000 timesteps and save the model to `models/tail_policy.pt`.

### 3. Predict Optimal Mach
Use the trained model to predict the optimal Mach for specific conditions:
```bash
# Usage: python predict_mach.py <Altitude> <Weight> <TAT> <CAS> [TempDevC] [WindKts] [Phase] [TargetAlt]
python predict_mach.py 36000 70000 -45 280 0 10 1 35000
```
Output:
```
Predicted Optimal Mach: 0.7802
```

## How it Works (Updated Design)
- The environment is now a short-horizon **cruise segment** rather than a one-step bandit. Each episode runs multiple steps with weight decreasing as fuel burns.
- Observations are **normalized** `[Altitude_ft, Weight_kg, TAT_C, CAS_kts, TempDev_C, Wind_kts, Phase, TargetAlt_ft]` for stable learning.
- Actions are still normalized to `[-1, 1]` and mapped to Mach `[0.70, 0.86]`.
- The fuel model is based on **aerodynamic drag** and **engine TSFC** instead of a simple quadratic penalty.
- A **wind/temperature profile** evolves slowly during an episode, and **per-tail variability** slightly changes aerodynamic/engine parameters.
- The episode includes **climb, cruise, and descent phases** with altitude targets and constraints.

## Environment Logic (Implementation Details)
1. **Atmosphere (ISA)**
   - Temperature, pressure, and density computed from altitude using a standard ISA approximation (troposphere + isothermal stratosphere).
2. **Airspeed**
   - TAS derived from Mach and local speed of sound.
   - CAS approximated from TAS and density (via EAS relationship).
3. **Drag Model**
   - `CD = CD0 + k * CL^2 + CD_wave * wave^2`
   - `CL = Weight / (q * S)`
   - `q = 0.5 * rho * V^2`
4. **Fuel Flow**
   - `FuelFlow = Drag * TSFC`
   - TSFC increases with altitude and temperature deviation (simplified).
5. **Reward**
   - Negative **fuel burn per distance** (kg per NM) using ground speed (`CAS + wind`).
   - Penalty for large deviations from target altitude.
   - **Energy management penalty** discourages excessive Mach in climb/descent and low-altitude overspeed.
6. **State Update**
   - Weight decreases each step by fuel burned.
   - Altitude follows climb/cruise/descent rates toward a target altitude.
   - Temperature deviation and wind evolve via a low-variance random walk.

## Mathematical Concepts
- **Markov Decision Process (MDP)**:
  - State `s = [alt, weight, TAT, CAS, tempDev, wind, phase, targetAlt]`, action `a = Mach`, reward `r = -fuel_per_nm - altitude_penalty`.
  - Short horizon episode with dynamics in weight, temperature deviation, wind, and altitude phase.
- **Stochastic Profiles**:
  - Temperature deviation and wind are modeled as AR(1) processes to create realistic temporal correlation.
- **Altitude Constraints**:
  - Hard bounds on altitude and a soft penalty around target altitude.
- **Energy Management**:
  - Additional penalties for high Mach in climb/descent and at low altitude.
- **Policy Gradient (PPO)**:
  - Clipped surrogate objective:
    `L = E[min(r_t(θ)A_t, clip(r_t(θ), 1-ε, 1+ε)A_t)]`
  - `r_t(θ) = π_θ(a|s) / π_θ_old(a|s)`
- **Advantage Estimation (GAE-style)**:
  - `δ_t = r_t + γ V(s_{t+1}) - V(s_t)`
  - `A_t = δ_t + γλ δ_{t+1} + ...`
- **Aerodynamics**:
  - `q = 0.5 ρ V^2`
  - `CL = W / (qS)`
  - `CD = CD0 + k CL^2 + CD_wave * wave^2`
  - `Drag = q S CD`
- **Engine Model**:
  - `FuelFlow = Drag * TSFC`
  - TSFC increases with altitude and temperature deviation.
- **Fuel per Distance**:
  - `FuelPerNM = FuelFlow / GroundSpeed`
  - Ground speed includes a wind component.

## Notes
- The physics is still simplified, but it is structured to be consistent and differentiable, which makes it a good DRL training target.
- Inference uses deterministic policy mean for stable Mach predictions.
