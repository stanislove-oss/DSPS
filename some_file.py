'''This is a test docstring'''
import random

def calculate(x, kind):
    '''This is a function docstring'''
    if kind == 'square':
        return x**2
    if kind == 'double':
        return x * 2
    if kind == 'hello':
        return 'Hello World'
    return 1

X=0
Y=10
print(random.randint(X, Y))
# wow it's a new comment
