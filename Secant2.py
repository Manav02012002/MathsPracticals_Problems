from sympy import *
x = Symbol('x')
f = x*exp(x)-2
a=0
b=1
r=0
while True:
    fa = float(f.subs({x:a}))
    fb = float(f.subs({x:b}))
    c = (a*fb - b*fa)/(fb-fa)
    if(round(c,4)==r):
        break
    r =round(c,4)
    a=b
    b=c
print("The root is ", c)
