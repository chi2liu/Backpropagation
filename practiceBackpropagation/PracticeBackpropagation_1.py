import numpy as np


def sigmoid(x):
    return 1./(1+np.exp(-x))


def derivative_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


a = -2
h = 0.1
a = a + h * derivative_sigmoid(a)
f = sigmoid(a)
print(f)  #outputs 0.1203
