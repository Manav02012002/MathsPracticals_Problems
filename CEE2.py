#20PCM53 Manav Madan Rawal
from sympy import*
from sympy.abc import x,z
y = Function('y')
y1 = y(z).diff(z)
y2 = y(z).diff(z,2)
def Cauchysolve(zeq, zsubs):
    zsol = dsolve(zeq)
    sol = zsol.rhs.subs(z,zsubs)
    print(sol)
Cauchysolve(y2-9*y(z),log(x))
