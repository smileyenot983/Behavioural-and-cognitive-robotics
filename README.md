# Behavioural-and-cognitive-robotics

## Task 2a (neural network without training):
* With random weights our neural network does random actions which is of course not enough to make any control

## Task 2b (evolutionary algorithm implementation):
* Implemented algorithm easily solves 'CartPole' task 
* Changing some parameters may decrease performance. For example reducing the populatation size from 10 to 4 reduced rewards. And to achieve the same performance as 10 populations i had to increase the number of epochs from 100 to 1000
* This simple algorithm can not solve every task. For example it couldn't solve 'MountainCar' task, because every population gets the same amount of reward and we cannot choose best from them.

## Task 3 (observing behaviour of evolved robots):
* I checked behavious of acrobot and humanoid and they are working well
