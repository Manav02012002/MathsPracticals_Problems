from numpy import double
from sympy import*
a = 2
t = Symbol('t')
r = a*(1+ cos(t))
arc_lt = sqrt(r**2+(diff(r,t))**2)
tot_arc = double(2*Integral(arc_lt, (t,0,pi)))
print("The length of the curve is,",tot_arc)
