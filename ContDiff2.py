#20PCM53 Manav Madan Rawal
from sympy import *
from sympy.abc import x,h
f = x**2-2*x+3
c=3
p=f.subs(x,c)
q1=f.subs(x,c-h)
LHL=Limit(q1,h,0).doit()
q2=f.subs(x,c+h)
RHL=Limit(q2,h,0).doit()
if RHL!=LHL or RHL!=p:
    print("Function is not continuous at the point c = ",c)
else:
    print("Function is continuous at the point c = ",c)
print("LHL= ",LHL," and RHL= ",RHL)
