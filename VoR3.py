from numpy import double
from sympy import*
t = Symbol('t')
a=4
x = a*(t-sin(t))
y = a*(1-cos(t))
vol = double(Integral(pi*y**2*diff(x,t),(t,0,2*pi)))
print("Volume of Revolution is",vol)