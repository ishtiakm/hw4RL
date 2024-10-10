HW4 --- Reinforcement Learning ---ECSE 6965
Mountain Car Problem


--To execute the hardcoded policy to achieve the  95 reward, open up a terminal, go to the program directory and type:
python3 mountain_car_bandit_95.py

This will print up the average reward for 1000 episodes of this policy.
The output looks like this:
"Total average reward for our policy_95 is 98.8803"


--To execute the UCB policy , open up a terminal, go to the program directory and type:
python3 mountain_car_bandit_ucb.py

This will print up the necessary instructions and keep on searching the controllers to get the desired controller which generates more than 98.5 error
The output shows something like this:

"A total of 28000 controllers are created

This algorithm usually takes less than 5  minutes to run

Update about the best reward till now will be given after every 1000 episodes:

Searching for a better controller

Cuurent episode: 1 ; Best Result till now: At episode 0, Controller 0, produces Reward of : 0.0

Searching for a better controller........

Cuurent episode: 1001 ; Best Result till now: At episode 0, Controller 0, produces Reward of : 0.0

Searching for a better controller........

Cuurent episode: 2001 ; Best Result till now: At episode 0, Controller 0, produces Reward of : 0.0

Searching for a better controller........

Cuurent episode: 3001 ; Best Result till now: At episode 2277, Controller 2250, produces Reward of : 97.01100000000001

Searching for a better controller........

Cuurent episode: 4001 ; Best Result till now: At episode 3203, Controller 3040, produces Reward of : 98.08

Searching for a better controller........

Cuurent episode: 5001 ; Best Result till now: At episode 3203, Controller 3040, produces Reward of : 98.08

Searching for a better controller........

Cuurent episode: 6001 ; Best Result till now: At episode 3203, Controller 3040, produces Reward of : 98.08

Searching for a better controller........

Cuurent episode: 7001 ; Best Result till now: At episode 3203, Controller 3040, produces Reward of : 98.08

Searching for a better controller........

Cuurent episode: 8001 ; Best Result till now: At episode 7954, Controller 4030, produces Reward of : 98.40700000000001

Searching for a better controller........

Cuurent episode: 9001 ; Best Result till now: At episode 7954, Controller 4030, produces Reward of : 98.40700000000001

Searching for a better controller........

Cuurent episode: 10001 ; Best Result till now: At episode 7954, Controller 4030, produces Reward of : 98.40700000000001

Searching for a better controller........

Cuurent episode: 11001 ; Best Result till now: At episode 7954, Controller 4030, produces Reward of : 98.40700000000001

Searching for a better controller........

Cuurent episode: 12001 ; Best Result till now: At episode 7954, Controller 4030, produces Reward of : 98.40700000000001

Searching for a better controller........

Cuurent episode: 13001 ; Best Result till now: At episode 7954, Controller 4030, produces Reward of : 98.40700000000001

Searching for a better controller........

Best controller index: 5020
Total time taken: 106.99329996109009 seconds

Generating average reward for the best controller......

The average reward of the best controller is:  98.75228799999931"
