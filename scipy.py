__author__ = 'Luz'
import numpy as np
import scipy
import matplotlib.pyplot as plt

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

fsolution = integrate.quad(PW, WV[0], WV[:])
dsolution = integrate.trapz(PW, x=0.5)
print('fsolution = ' + str(fsolution[0]))
print('dsolution = ' + str(dsolution))
print('The difference is ' + str(np.abs(fsolution[0] - dsolution)))