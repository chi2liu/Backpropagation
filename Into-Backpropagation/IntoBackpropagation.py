def product(x, y):
    return x * y


def addition(x, y):
    return x + y


def forward(a, b, c):
    d = addition(a, b)
    return product(d, c)


print(forward(5, -6, 7))# output -7


def update(a, b, c):
    d = addition(a, b)
    h = 0.01

    derivative_f_d = c
    derivative_f_c = d
    derivative_d_a = 1
    derivative_d_b = 1

    derivative_f_a = derivative_f_d * derivative_d_a
    derivative_f_b = derivative_f_d * derivative_d_b

    a = a + h * derivative_f_a
    b = b + h * derivative_f_b
    c = c + h * derivative_f_c

    d = addition(a, b)
    return product(d, c)


print(update(5, -6, 7))# output -6.0113999999999965

