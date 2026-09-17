import numpy as np
import math
import matplotlib.pyplot as plt


# Create a user defined function f(x) that returns the value 1 + 1/2tanh(2x)

def f(x):
    return 1 + 1/2*np.tanh(2*x)

# Use the central difference method to calculate the derivative of f(x)

def central_diff(h):
    return (f(x+(h/2)) - f(x-(h/2)))/h


a = -2
b = 2
h = 1e-5

y = np.linspace(a, b, 100)
#print(y)

plt.plot(f(x), central_diff(h))
plt.show()


