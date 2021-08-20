from numpy import double
from sympy import*
y = Symbol('y')
x = y**3
arc_lt = sqrt(1+(diff(x,y))**2)
sur_area = double(Integral(2*pi*x*arc_lt,(y,0,2)))
print("Surface Area of revolution is,", sur_area)

