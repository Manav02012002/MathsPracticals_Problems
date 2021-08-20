from sympy import *
x = Symbol('x')
y = Function('y')
y0 = {y(pi/3):0}
x1=pi
DE = Eq(y(x).diff(x) + 2*tan(x)*y(x), sin(x))
sol = dsolve (DE, y(x), ics=y0)

print(f"The solution of the given ODE is:{sol.rhs}")
print(f"The value of y at {x1} is: {sol.rhs.subs(x,x1)}")

plot (sol.rhs, (x,pi/2, 2*pi), ylabel="y(x)")
