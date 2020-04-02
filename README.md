# Behavioural-and-cognitive-robotics

## Task 2a (neural network without training):
* With random weights our neural network does random actions which is of course not enough to make any control

## Task 2b (evolutionary algorithm implementation):
* Implemented algorithm easily solves 'CartPole' task 
* Changing some parameters may decrease performance. For example reducing the populatation size from 10 to 4 reduced rewards. And to achieve the same performance as 10 populations i had to increase the number of epochs from 100 to 1000
* This simple algorithm can not solve every task. For example it couldn't solve 'MountainCar' task, because every population gets the same amount of reward and we cannot choose best from them.

## Task 3 (observing behaviour of evolved robots):
* I checked behaviours of acrobot and humanoid and they are working well

## Task 4 (comparing original(suited for RL) and modified(suited for genetic algorithms) reward functions)
* Original = sum([alive, progress, electricity cost, joints at limit cost, feet collision cost]), Modified = sum([progress,joints at limit cost]), So the difference is that in modified function our reward only consists of 2 parts: we check the progress(distance travelled) and if robot had to reach limits of joints during movements, and in original we take care about much more parameters.
* I think that original reward is not suitable for genetic algorithm because it's too complex
* I trained Salimans algorithm for 10mln steps and results are the following(left - modified, right - original): 
![Results of evolutionary algorithm on half cheetah environment](https://github.com/smileyenot983/Behavioural-and-cognitive-robotics/blob/master/reward_shaping_results.jpg)

## Task 5 (creating new environment)

* Implementation for balancebot_env.py introduced by guidelines returned the error 'Joint index out-of-range' , that's why i replaced this script by scipt from https://github.com/yconst/balance-bot.
* After that i trained agent for 30mln steps and results are pretty good. Robot keeps balancing with a very small inclination.Here are the results
![Results achieved by balancing robot environment](https://github.com/smileyenot983/Behavioural-and-cognitive-robotics/blob/master/balancing_robot_results.jpg)

