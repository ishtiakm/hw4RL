import numpy as np
import gymnasium as gym
import math
import time

class Controller:
    def __init__(self, p1, p2, a1, a2, a3):
        self.p1 = p1
        self.p2 = p2
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def get_action(self, observation):
        pos, vel = observation
        if vel < 0 and pos > self.p1:
            return [self.a1]
        if vel > 0 and pos < self.p2:
            return [self.a2]
        else:
            return [self.a3]

class ControllerManager:
    def __init__(self, p1_values, p2_values, a1_values, a2_values, a3_values, reward_threshold=98.5):
        self.controllers = [
            Controller(p1, p2, a1, a2, a3)
            for p1 in p1_values for p2 in p2_values for a1 in a1_values for a2 in a2_values for a3 in a3_values
        ]
        self.num_controllers = len(self.controllers)
        self.N = [0] * self.num_controllers
        self.Q = [0] * self.num_controllers
        self.reward_threshold = reward_threshold
        self.active_controllers = set(range(self.num_controllers))  # Active controllers

    def select_controller(self, episode):
        t = episode + 1
        UCB = [
            q + 5 * math.sqrt(2 * math.log(t + 1) / (n + 1)) if i in self.active_controllers else -float('inf')
            for i, (q, n) in enumerate(zip(self.Q, self.N))
        ]
        return np.argmax(UCB)

    def update_reward(self, index, reward):
        self.N[index] += 1
        self.Q[index] += (reward - self.Q[index]) / self.N[index]
        if self.N[index] > 10 and self.Q[index] < self.reward_threshold:  # Prune poor controllers
            self.active_controllers.discard(index)

def run_episode(env, controller, num_steps):
    total_reward = 0
    observation = env.reset()[0]
    for step in range(num_steps):
        action = controller.get_action(observation)
        observation, reward, done, _, _ = env.step(action)
        total_reward += reward
        if done:
            break
    return total_reward

if __name__ == '__main__':
    np.random.seed(1)

    num_steps = 1000
    env = gym.make('MountainCarContinuous-v0').env.unwrapped


    start=time.time()

    # Discretize the state and action space into possible values
    p1_values = [-i * 3 / 10 for i in range(4)]
    p2_values = [(j * 3 - 12) / 10 for j in range(7)]
    a1_values = [-j / 10 for j in range(10)]
    a2_values = [j / 10 for j in range(10)]
    a3_values = [j / 10 for j in range(10)]

    manager = ControllerManager(p1_values, p2_values, a1_values, a2_values, a3_values, reward_threshold=98.5)

    total_episodes = 100000

    num_controllers = manager.num_controllers
    print(f"A total of {num_controllers} controllers are created")
    print()
    print("This algorithm usually takes 7-8 minutes to run")
    print()
    print("Update about the best reward till now will be given after every 1000 episodes:")
    print()
    print("Searching for a better controller")
    print()

    # Run multiple episodes and use UCB for controller selection
    prev_controller = None
    flag_count=0
    break_flag=0
    best_case=[-1000,-1000,-1000]
    for episode in range(total_episodes):
        if len(manager.active_controllers) == 0:
            break  # Stop early if no controllers are left

        selected_index = manager.select_controller(episode)
        selected_controller = manager.controllers[selected_index]

        reward = run_episode(env, selected_controller, num_steps)
        if reward>best_case[2]:
            best_case[0]=episode
            best_case[1]=selected_index
            best_case[2]=reward
        manager.update_reward(selected_index, reward)

        if episode%1000==0:
            print(f"Cuurent episode: {episode + 1} ; Best Result till now: At episode {best_case[0]}, Controller {best_case[1]}, produces Reward of : {best_case[2]}")
            print()
            print("Searching for a better controller........")
            print()
        

        #print(f"Episode {episode + 1}/{total_episodes}, Controller {selected_index}, Reward: {reward}")
        if selected_controller==prev_controller:
            flag_count+=1
        else:
            flag_count=0
        if flag_count==3:
          if reward>98.6:
        
            break_flag=1
        if break_flag==1:
          break    

        prev_controller = selected_controller

    # Find the best controller based on estimated rewards
    best_index = np.argmax(manager.Q)
    best_controller = manager.controllers[best_index]
    print(f"Best controller index: {best_index}")
    end=time.time()
    print(f"Total time taken: {end-start} seconds")
    print()
    print("Generating average reward for the best controller......")
    print()
    # Generate average reward for the best controller

    total_reward = 0
    for i in range(1000):
        total_reward += run_episode(env, best_controller, num_steps)
    print("The average reward of the best controller is: ", total_reward / 1000)

