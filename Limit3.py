#20PCM53 Manav Madan Rawal
from sympy import*
x = Symbol('x')
y = (1/x - 1/sin(x))
z = limit(y,x,0)
print(z)
