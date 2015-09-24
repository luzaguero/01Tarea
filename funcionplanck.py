__author__ = 'Luz'

import numpy
import matplotlib
from pylab import *

# the function to be integrated
def func(x):
    return ((tan(x))**3)/(((exp(tan(x)))-1)*((cos(x))**2))

a = 0.
b = pi/2.
dx = 0.01

n = int((b - a) / dx)


Integ = 0
for i in range(2, n+1):

    x0 = a+(i-1)*dx
    x1 = a+i*dx

    Ai = dx * (func(x0) + func(x1))/ 2.

    Integ = Integ + Ai


print "Integral = ", Integ
print "P =", Integ*(2*pi*(6.62606957*10**-34)/(299792458)**2)*((((1.3806488*10**-23)*5776)/(6.62606957*10**-34))**4)