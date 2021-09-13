#20PCM53 Manav Madan Rawal
from sympy import *
from sympy.abc import x,h
f = x**2-2*x
c=2
q1=f.subs(x,c-h)
LHD=Limit((q1-f)/h,h,0).doit()
q2=f.subs(x,c+h)
RHD=Limit((q2-f)/h,h,0).doit()
if RHD!=LHD:
    print("Function is not differentiable at the point c = ",c)
else:
    print("Function is differentiable at the point c = ",c)
