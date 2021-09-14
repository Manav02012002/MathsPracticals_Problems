#20PCM53 Manav Madan Rawal
from sympy import*
from sympy.abc import x
y = Function('y')
y1 = diff(y(x),x)
y2 = diff(y1,x)
z = dsolve(Eq(y2+2*y1+2*y(x)-8*exp(2*x)),y(x))
print("Solution of the Non Homogenous DE is", z.rhs)
