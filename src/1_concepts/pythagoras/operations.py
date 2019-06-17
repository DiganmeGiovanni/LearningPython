from math import sqrt


def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return float(a) * b


def division(a, b):
    if b == 0:
        return 0
    return float(a)/b


def square_root(a):
    return sqrt(a)


def power(a, b):
        return pow(a, b)
