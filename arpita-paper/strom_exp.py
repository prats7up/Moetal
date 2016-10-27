import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def solvr(Y, t):
        return np.exp(Y/y0)*(1./3. - y0**3*(1. - np.exp(-2.*Y/y0)*(1.+2.*Y/y0+2.*(Y/y0)**2))/4.)/(Y*Y)



global y0
y0 = 10.0
a_t = np.linspace(0.0, 8.0, 1000)
asol1 = integrate.odeint(solvr, 1.e-10 , a_t)

y0 = 1000.0
asol2 = integrate.odeint(solvr, 1.e-10 , a_t)

y0 = 1.0
asol3 = integrate.odeint(solvr, 1.e-10 , a_t)

a_t4 = np.linspace(0.0, 0.5, 1000)
y0 = 0.5
asol4 = integrate.odeint(solvr, 1.e-10 , a_t)

plt.loglog( a_t, asol1, a_t, asol2, a_t, asol3, a_t4, asol4)
plt.legend( ['$y_0=10$','$y_0=10^3$','$y_0=1$','$y_0=0.5$'],loc='best' )
plt.ylim([1.e-1,5])
plt.xlabel (r'$t/t_{\rm rec,0}$')
plt.ylabel (r'$z_+/r_{S0}$')

plt.show()
