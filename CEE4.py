#20PCM53 Manav Madan Rawal
from sympy import*
from sympy.abc import x,z
y = Function('y')
y1 = y(z).diff(z)
y2 = y(z).diff(z,2)
def Eulersolve(zeq, zsubs):
    zsol = dsolve(zeq)
    sol = zsol.rhs.subs(z,zsubs)
    print(sol)
Eulersolve(y2-2*y1+y(z)-3*(exp(z))+2,log(x+2))
