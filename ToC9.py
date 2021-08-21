from numpy import*
import matplotlib.pyplot as plt
a = 3
angle = arange(0, (2*pi), 0.01)
for theta in angle:
    r = a*(sin(4*theta))
    plt.polar(theta, r, 'g.')
plt.show()