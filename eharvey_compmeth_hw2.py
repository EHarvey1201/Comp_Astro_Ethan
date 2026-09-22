import numpy as np
import argparse as arg
import matplotlib.pyplot as plt

Parser = arg.ArgumentParser()
Parser.add_argument('-i','--input',type=str,help='Input file')
args = Parser.parse_args()
Parser.add_argument('-o','--output',type=str,help='Output file')
Parser.add_argument('-N' '--steps',type=float,help='Number of steps for integral')
Parser.add_argument('-u' '--upper',type=float,help='Upper limit for integral')

# Calculate the integral exp(-t**2) dt

def trap_rule(N, upper):
    a = 0.0
    delta_t = (upper - a)/N
    
    def f(t):
        return np.exp(-t**2)
    
    F = 0.5*f(a) + 0.5*f(upper)
    for k in range(1,N):
        F += f(a+k*delta_t)

    return delta_t*F

# Calling in the trapezoidal rule to solve the integral

trap_rule(300,3)

# iterate the integral from range 0-3 and plot the results

upper = np.linspace(0, 3, 31)

array = trap_rule(300, upper)
for x in upper:
   plt.plot(upper, array)
plt.show()


