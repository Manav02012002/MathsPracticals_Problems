from sympy import*
from numpy import *
def simp(a,b,n,f):
    h=(b-a)/n
    c=1
    w=0
    t=0
    y0=f.subs({x:a})
    yn=f.subs({x:b})
    for i in arange(a+h,b,h):
        s=f.subs({x:i})
        if c%3==0:
            w+=s
        else:
            t+=s
        c+=1
    z=(3*h/8)*(y0+yn+3*t+2*w)
    print("The approx value of the integral is ",z)
x=Symbol('x')
y=1/(1+x**2)
simp(0,6,6,y)