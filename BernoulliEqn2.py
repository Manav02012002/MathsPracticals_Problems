from sympy import *
x = Symbol('x')
y = Function('y')
y0 = {y(1):1}
x1=2
DE = Eq(x*y(x).diff(x) + y(x), (y(x)**2)*log(x))
sol = dsolve (DE, y(x), ics=y0)

print(f"The solution of the given ODE is:{sol.rhs}")
print(f"The value of y at {x1} is: {sol.rhs.subs(x,x1)}")

plot (sol.rhs, (x, 1, 2), ylabel="y(x)")