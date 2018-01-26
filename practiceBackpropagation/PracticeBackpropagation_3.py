import numpy as np


def addition(x, y):
    return x + y


def product(x, y):
    return x * y


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


# initialization
a = 1
b = -2
c = -3
# forward-propogation
d = addition(a, b)
e = product(c, d)
# step size
h = 0.1
# derivatives
derivative_f_e = derivative_sigmoid(e)
derivative_e_d = c
derivative_e_c = d
derivative_d_a = 1
derivative_d_b = 1
# backward-propogation (Chain rule)
derivative_f_a = derivative_f_e * derivative_e_d * derivative_d_a
derivative_f_b = derivative_f_e * derivative_e_d * derivative_d_b
derivative_f_c = derivative_f_e * derivative_e_c
# update-parameters
a = a + h * derivative_f_a
b = b + h * derivative_f_b
c = c + h * derivative_f_c
d = addition(a, b)
e = product(c, d)
f = sigmoid(e)
print(f)  # prints 0.9563