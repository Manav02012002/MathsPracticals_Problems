#20PCM53 Manav Madan Rawal
from sympy import sin,pi 
from sympy.abc import x
def taylor(function, x0, n):
    return function.series(x,x0,n).removeO()
print("sin(x)= ",taylor(sin(x),pi,4))
