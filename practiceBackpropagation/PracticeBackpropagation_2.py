import numpy as np


def addition(x,y):
	return x+y


def product(x, y):
    return x * y


def sigmoid(x):
    return 1 / (1 + np.exp( -x ))


a=1
b=-2
c=-3
d=addition(a,b)
e=product(c,d)
f=sigmoid(e)
print(f)  #outputs 0.952574
