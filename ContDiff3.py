#20PCM53 Manav Madan Rawal
from sympy import *
from sympy.abc import x,h
f = Piecewise((1/x,x!=0),(0,x==0))
c=0
q1=f.subs(x,c-h)
LHD=Limit((q1-f)/h,h,0).doit()
q2=f.subs(x,c+h)
RHD=Limit((q2-f)/h,h,0).doit()
if RHD!=LHD:
    print("Function is not differentiable at the point c = ",c)
else:
    print("Function is differentiable at the point c = ",c)
