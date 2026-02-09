---
tags : [drl]
title : notes on drl 
---

### Introduction 
There is this **agent** that moves from one **state** to another by taking an **action**, as an outcome of taking the action, it gets a **reward**. The goal is to maximize the reward. the rewards are provided as per a **policy**  
![](/PYTHON/drl/drl-intro.excalidraw.png)

**policy** - map from state to possible actions from that particular state. Policy might be deterministic naming exact actions or stochastic - a probability distribution of all hte possible actions. 

**Trajectory** - ((s1,a1),(s2,a2),(s3,a3)) - a **sequence** of all states and actions in an **episode** 

**Episode** - a collection of states and actions, whose cumulative reward is calculated and returned. 

$$R_r = \sum_{t=0}^{T} \gamma^t r_t $$

$\gamma$ = discount factor 
$r_t$ = instantaneous reward at time t
$R_r$ = total discounted sum of rewards accumulated along a trajectory $\tau$
There can be multiple trajectories. 

### Setting up the environment 

```python
import gymnasium as gym

# Initialise the environment
env = gym.make("LunarLander-v3", render_mode="human")

# Reset the environment to generate the first observation
observation, info = env.reset(seed=42)
for _ in range(1000):
    # this is where you would insert your policy
    action = env.action_space.sample()

    # step (transition) through the environment with the action
    # receiving the next observation, reward and if the episode has terminated or truncated
    observation, reward, terminated, truncated, info = env.step(action)

    # If the episode has ended then we can reset to start a new episode
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```






