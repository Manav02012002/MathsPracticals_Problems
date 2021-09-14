#20PCM53 Manav Madan Rawal
from sympy import*
from sympy.abc import x
y = Function('y')
y1 = diff(y(x),x)
y2 = diff(y1,x)
z = dsolve(Eq(y2-1*y(x)-((x**2+1)*exp(x)),y(x)))
print("Solution of the Non Homogeneous DE is", z.rhs)
