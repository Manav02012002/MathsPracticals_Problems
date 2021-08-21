from numpy import double
from sympy import*
x = Symbol('x')
a,b=2,1
y_square = b**2*(1-x**2/a**2)
vol = double(Integral(2*pi*y_square,(x,0,a)))
print("Volume of Revolution is",vol)