__author__ = 'Luz'
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

var = np.loadtxt('sun_AM0.dat')

wave = []
power = []
PW=[]
WV=[]
for i in range(0,len(var)):
    wv = var[i][0]
    wave.append(wv)
    WV.append(wv*10)

    pwr = var[i][1]
    power.append(pwr)
    PW.append(pwr*(10**10))

AREA = 0
for i in range(0, len(var)-1):
    #metodo trapecio
    a = wave[i+1] - wave[i]
    b = power[i]
    if b > 0:
        area = a*b

    AREA = AREA + area
print "Potencia sun=",AREA, "[Wm-2]"
print "Luminosidad sun= ", AREA*2.812*10**23, "[W]"

plt.plot(WV, PW, 'r-')

xlabel('Wavelength [Angtrom]')
ylabel('Power [g*cm-1*s-3]')
title('Espectro del Sol')
grid(True)

plt.show()
