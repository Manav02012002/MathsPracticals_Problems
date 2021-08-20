from sympy import *
x = Symbol('x')
y = Function('y')
y0 = {y(1):1}
x1=1.3
DE = Eq(x*y(x).diff(x) - 2*y(x), (1/(x**2)*y(x)**2))
sol = dsolve (DE, y(x), ics=y0)

print(f"The solution of the given ODE is:{sol.rhs}")
print(f"The value of y at {x1} is: {sol.rhs.subs(x,x1)}")

plot (sol.rhs, (x, 1, 2), ylabel="y(x)")