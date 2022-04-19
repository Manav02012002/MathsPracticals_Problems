from sympy import*
def f(x):
    return x*exp(x)-cos(x)
a = 0.5
b = 0.6
r=0
while True:
    c = (a*f(b)-b*f(a))/(f(b)-f(a))
    if(round(c,4)==r):
        break
    r = round(c,4)
    if f(a)>0 and f(b)<0:
        if f(c)<0:
            b=c
        else:
            a=c
    else:
        if f(c)<0:
            a=c
        else:
            b=c
print("The root is ", round(c,4))
