from numpy import double
from sympy import*
a = 2
x = Symbol('x')
y = (a**(2/3) - x**(2/3))**(3/2)
arc_lt = sqrt(1+(diff(y,x))**2)
tot_arc = double(4*Integral(arc_lt, (x,0,a)))
print("The length of the curve is,",tot_arc)
