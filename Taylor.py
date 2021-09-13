#20PCM53 Manav Madan Rawal
from sympy import exp 
from sympy.abc import x
def taylor(function, x0, n):
    return function.series(x,x0,n).removeO()
print("e(x)= ",taylor(exp(x),0,4))
