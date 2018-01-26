import random


def product(a, b):
	return a * b


def methodOne():
    a = 5
    b = 6
    step = 0.01
    a = a + step * (random.random())
    b = b + step * (random.random())
    print(product(a, b))

methodOne()

def testTwo():
    a = -5
    b = -6
    step = 0.01
    a = a + step * (random.random())
    b = b + step * (random.random())
    print(product(a, b))

testTwo()

def methodTwo(a, b):
    step = 0.01
    a = a + step * b
    b = b + step * a
    print(product(a, b))

methodTwo(5, 6)
methodTwo(-5, -6)