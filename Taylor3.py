#20PCM53 Manav Madan Rawal
from sympy import cos 
from sympy.abc import x
def taylor(function, x0, n):
    return function.series(x,x0,n).removeO()
print("cos(x)= ",taylor(cos(x),0,4))
