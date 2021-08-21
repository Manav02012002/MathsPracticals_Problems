from numpy import double
from sympy import*
t = Symbol('t')
a=3
r = a*(1-cos(t))
vol = double(Integral(2/3*pi*r**3*sin(t),(t,0,pi)))
print("Volume of Revolution is",vol)