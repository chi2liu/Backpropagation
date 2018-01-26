import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))


def derivative_sigmoid(x):
    return np.multiply(sigmoid(x), (1-sigmoid(x)))


# initialization
# X : 1*3
X = np.matrix("2, 4, -2")
# W : 3*2
W = np.random.normal(size=(3, 2))
# label
ycap = [0]
# number of training of examples
num_examples = 1
# step size
h = 0.01
# forward-propogation
y = np.dot(X, W)
y_o = sigmoid(y)
# loss calculation
loss = -np.sum(np.log(y_o[range(num_examples), ycap]))
print(loss)     # outputs 3.6821105514(for you it would be different due to random initialization of weights.)
# backprop starts
temp1 = np.copy(y_o)
# implementation of derivative of cost function with respect to y_o
temp1[range(num_examples), ycap] = 1 / -(temp1[range(num_examples), ycap])
temp = np.zeros_like(y_o)
temp[range(num_examples), ycap] = 1
# derivative of cost with respect to y_o
dcost = np.multiply(temp, temp1)
# derivative of y_o with respect to y
dy_o = derivative_sigmoid(y)
# element-wise multiplication
dgrad = np.multiply(dcost, dy_o)
dw = np.dot(X.T, dgrad)
# weight-update
W -= h * dw
# forward prop again with updated weight to find new loss
y = np.dot(X, W)
yo = sigmoid(y)
loss = -np.sum(np.log(yo[range(num_examples), ycap]))
print(loss)     # 3.45476397276 outpus (again for you it would be different!)
