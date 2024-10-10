import gymnasium as gym
import random
import numpy as np
from matplotlib import pyplot as plt


# hardcoded policy that achieves a reward of at least 95

    
def policy_95(observation):
    
    pos, vel = observation
    if vel <= 0 and pos > -0.6:
        return [-0.1]  # Push right if velocity is positive but position is still negative (backing up hill)
    if vel >0 and pos <0.4:
        return [0.2]
    else:
        return [0.0]



# this function runs an episode in Mountain Car, using policy pi, for the prescribed num_steps
def run_episode(env, pi, num_steps):
    positions=[]
    observation = env.reset()[0]
    total_reward=0
    for i in range(num_steps):
        action=pi(observation)
        observation, reward, done, _, _ = env.step(action)
        positions.append(observation[0])
        total_reward += reward
        if done:
            break

    return total_reward,positions



if __name__ == '__main__':

    np.random.seed(1)

    # Limit on the number of steps per episode in Mountain Car
    num_steps = 1000

    # use this if you would like to render the environment
    env = gym.make('MountainCarContinuous-v0', render_mode = 'human').env.unwrapped

    # use this is you would like to run multiple runs quickly without rendering
    env = gym.make('MountainCarContinuous-v0').env.unwrapped

    num_episodes=1000
    total_reward=0


    for i in range(num_episodes):
    
        reward, positions=run_episode(env, policy_95, num_steps)
        total_reward=total_reward+reward
    print(f"Total average reward for our policy_95 is: {total_reward/1000}")
  
