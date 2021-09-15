#20PCM53 Manav Madan Rawal
from sympy import*
x = Symbol('x')
y = log(sin(x))/cot(x)
z = limit(y,x,0)
print(z)
