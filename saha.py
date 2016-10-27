import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

ngrid = 1000
T = np.logspace(1, 6, ngrid)
Ui = 13.6*1.16e4

#ni = 2.4e15*T**1.5*np.exp(-Ui/T) #from Chen


#plt.loglog(ni, T)
#plt.axis([1.e-5,1.e29,10,1.e6])

#plt.xlabel (r'number density (cm$^{-3}$)')
#plt.ylabel (r'temperature (K)')


me = 9.11e-28; kB=1.38e-16; h=6.63e-27
n = 1.0e20; IP = 13.6*1.16e4; x = np.zeros(ngrid)
#Newton-Raphson
for i in range(ngrid):
    xg=0.99; err=1.e10
    while (err>1.e-5):
        fn = xg*xg - (1.-xg)*(2.*np.pi*me*kB*T[i])**1.5*np.exp(-IP/T[i])/(n*h**3)
        fp = 2.*xg + (2.*np.pi*me*kB*T[i])**1.5*np.exp(-IP/T[i])/(n*h**3)
        xg = xg - fn/fp
        err = abs(fn/fp)/xg
        print err
    x[i] = xg
    
plt.semilogx(T,x, '-')
plt.ylim([0, 1.0])
plt.show()