from numpy import double
from sympy import*
t = Symbol('t')
a = 2
r = a*(1 + cos(t))
arc_lt = sqrt(r**2 + (diff(r,t))**2)
sur_area = double(Integral(2*pi*(r*sin(t))*arc_lt,(t,0,pi)))
print("Surface Area of revolution is,", sur_area)
