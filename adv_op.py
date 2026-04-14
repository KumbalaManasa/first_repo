import math

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def square_root(n):
    if n < 0:
        return "Error! Negative number"
    return math.sqrt(n)

def cube_root(n):
    return n ** (1/3)


