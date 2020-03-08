import gym
import numpy as np
# import pybulletgym

env = gym.make('CartPole-v0')

pvariance= 0.1
ppvariance = 0.02
nhiddens = 5

weights=[]
rewards=np.zeros(10)

ninputs = env.observation_space.shape[0]
noutputs = 2


# generating weights for the first time
for population in range(10):
    W1 = np.random.randn(nhiddens,ninputs) * pvariance #5,4
    W2 = np.random.randn(noutputs,nhiddens) * pvariance #2,5

    b1 = np.zeros(shape=(nhiddens,1))
    b2 = np.zeros(shape=(noutputs,1))

    w = (W1,W2,b1,b2)
    weights.append(w)

#main training part 
for _ in range(100):
    #population = 10
    for population in range(10):
       
        observation = env.reset()
        #forward propagation of neural network
        for t in range(201):
            
            observation = observation.reshape(observation.shape[0],1)
            Z1 = np.dot(weights[population][0],observation) + weights[population][2]
            A1 = np.tanh(Z1) #shape = (5,1)
            Z2 = np.dot(weights[population][1],A1) + weights[population][3] 
            A2 = np.tanh(Z2) #shape = (2,1)
            
            action = np.argmax(A2)
            
            observation,reward,done,info = env.step(action)
            if done:
                break
            rewards[population]+=reward
    # print(_)
    # print(rewards)
    # now we have 10 rewards for 10 types of configuration
    # we should take 5 best and mutate them
    new_weights = []
    for i in range(5):
        #take argmax
        best = np.argmax(rewards)
        #add weights of argmax to weights for next iteration
        new_weights.append(weights[best])
        #write to argmax min to not write it's weights again
        rewards[best] = min(rewards)
    
    
    # now we have weights for 5 best populations
    mutation_step = 0.02
    for w in new_weights.copy():
        #mutate each weight with random normal noise multiplied by mutation step
        w0 = w[0] + np.random.randn(w[0].shape[0],w[0].shape[1])*mutation_step
        w1 = w[1] + np.random.randn(w[1].shape[0],w[1].shape[1])*mutation_step
        w2 = w[2] + np.random.randn(w[2].shape[0],w[2].shape[1])*mutation_step
        w3 = w[3] + np.random.randn(w[3].shape[0],w[3].shape[1])*mutation_step 
        
        new_weights.append([w0,w1,w2,w3])

    weights = new_weights
    rewards=np.zeros(10)

#here i am evaluating trained neural network with 
rewards = 0
for i_episode in range(5):
    observation = env.reset()
    
    for t in range(1000):
        env.render()
        observation = observation.reshape(observation.shape[0],1)
        Z1 = np.dot(weights[0][0],observation) + weights[0][2]
        
        A1 = np.tanh(Z1) #shape = (5,1)
        Z2 = np.dot(weights[0][1],A1) + weights[0][3] 
        A2 = np.tanh(Z2) #shape = (2,1)
        
        action = np.argmax(A2)
        

        observation, reward, done, info = env.step(action)
        rewards+=reward
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print(rewards)
            rewards=0
            break
env.close()
    

        

