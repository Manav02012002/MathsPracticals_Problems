from sympy import*
a = 3
var('x y')
plot_implicit(y**2-x**2*(a+x)/(a-x))
