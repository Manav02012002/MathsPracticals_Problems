#20PCM53 Manav Madan Rawal
from sympy import*
from sympy.abc import x
y = Function('y')
y1 = diff(y(x),x)
y2 = diff(y1,x)
y3 = diff(y2,x)
z = dsolve(Eq(y3-4*y2+y1+6*y(x)),y(x))
print("Solution of the Homogenous DE is", z.rhs)