from sympy import*
from sympy.abc import x,y
f=x**2+x*y+y**2+3*x-3*y+4
cp=solve((Eq(diff(f,x)), Eq(diff(f,y))), (x,y))
print("The critical point is ({},{}) ".format(cp[x],cp[y]))
a = diff(f,x,2).subs({x:cp[x], y:cp[y]})
b = diff(f,x,y).subs({x:cp[x], y:cp[y]})
c = diff(f,y,2).subs({x:cp[x], y:cp[y]})
delta=a*c-b**2
if(delta>0 and a<0):
    print("The given function is maximum at the critical point.")
elif(delta>0 and a>0):
    print("The given function is minimum at the critical point.")
elif(delta<0):
    print("The critical point is a saddle point.")
else:
    print("Further tests required")