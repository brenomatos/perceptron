import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data_points = np.array([[1,0,1], [1,1,0], [1,1,1], [1,0,0]]).astype('float')
classes = [-1,-1,1,-1]

def init_weights(lower_boun,upper_bound):
    w0 = random.randint(lower_boun,upper_bound) #Initializing weights at random
    w1 = random.randint(lower_boun,upper_bound)
    w2 = random.randint(lower_boun,upper_bound)

    weights = np.array([w0,w1,w2]).astype('float')
    return weights


def signal(x):
    if x>=0:
        return 1
    else:
        return -1


def perceptron(data_points, weights,learning_rate):
    while 1:
        counter = 0
        for i in range(len(data_points)):
            signal_output = signal(np.dot(data_points[i],weights))
            if signal_output==classes[i]:
                counter = counter+1
            else:
                if signal_output==-1:
                    weights = weights+(data_points[i])*learning_rate # multiply by learning rate
                else:
                    weights = weights-(data_points[i])*learning_rate # multiply by learning rate

        if counter==len(data_points):
            break
    return weights #return final weights


learning_rate = 0.1 #learning rate
weights = init_weights(-9,9)
final_weights = perceptron(data_points,weights,learning_rate)

print("Final Weights",final_weights)
