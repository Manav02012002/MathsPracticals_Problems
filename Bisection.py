from sympy import*
x = Symbol('x')
f = Function('f')
def f(x):
    return x*exp(x)-cos(x)

def bisection(f,a,b,tol):
    itr=0
    while(abs(a-b)>tol):
        itr+=1
        c = (a+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    print("The approximate root of the given function after ", itr, "many iterations is ", c, ".")

bisection(f,0.5,0.6,0.00000001)
