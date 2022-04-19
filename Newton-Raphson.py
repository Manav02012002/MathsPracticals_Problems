from sympy import*
x = Symbol('x')
f = x**3-2*x-5
df = f.diff(x)
a=2
r=0
while True:
    fa = float(f.subs({x:a}))
    fd = float(df.subs({x:a}))
    c = a-(fa/fd)
    if(round(c,4)==r):
        break
    r = round(c,4)
    a=c
print("The root is ",c)