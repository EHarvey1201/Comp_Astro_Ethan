import numpy as np

# Using the trapezoidal rule to calculate the integral x^4-2x+1 from 0 to 2
a = 0.0
b = 2.0 
N = 100
delta_x = (b - a)/N

def f(x):
    return x**4 - 2*x + 1

F = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    F += f(a+k*delta_x)

print(delta_x*F)
    
# Using the trapezoidal rule to calculate the integral x^4-2x+1 from 0 to 2
a = 0.0
b = 2.0 
N = 1000
delta_x = (b - a)/N

def f(x):
    return x**4 - 2*x + 1

def trap_rule(N):
    F = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        F += f(a+k*delta_x)
    return delta_x*F

   

# Using the Simpson's method to solve the same integral (x^4-2x+1) from 0 to 2

def simp_rule(a, b, N):
    delta_x = (b - a)/N
    F = (delta_x/3) * f(a) + f(b)
    for k in range(1, N/2):
        F += 4*f(a + (2*k-1) * delta_x)
    for k in range(1, N/2-1):
        F += 2*f(a + 2*k * delta_x)

    return F

simp_rule(0.0, 2.0, 10)




