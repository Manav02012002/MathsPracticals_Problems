from numpy import*
import matplotlib.pyplot as plt
a = 3
angle = arange(0, (2*pi), 0.01)
for theta in angle:
    r = a*(cos(2*theta)**1/2)
    plt.polar(theta, r, 'g.')
plt.show()