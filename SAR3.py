from numpy import double
from sympy import*
t = Symbol('t')
a = 2
x = a*(t - sin(t))
y = a*(1 - cos(t))
arc_lt = sqrt((diff(x,t))**2 +(diff(y,t))**2)
sur_area = double(Integral(2*pi*y*arc_lt,(t,0,pi)))
print("Surface Area of revolution is,", sur_area)
