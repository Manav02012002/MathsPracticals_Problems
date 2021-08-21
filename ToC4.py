from sympy import*
a = 3
var('x y')
plot_implicit(y-a*cosh(x/a))