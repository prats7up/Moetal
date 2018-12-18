import numpy as np
import matplotlib.pyplot as plt

def Ez(z):
    return np.sqrt(Om*(1.+z)**3+(1.-Om))

global Om
Om = 0.3089; Ov=0.6911

zred = np.logspace(-3,1,100)

rho_m = Om*(1+zred)**3
rho_cr = Ez(zred)*Ez(zred)
plt.plot(zred,rho_m,label=r'$\rho_m$')
plt.plot(zred,rho_cr,label=r'$\rho_{cr}$')
plt.plot(zred,(1+zred)**3,label=r'$(1+z)^3$')
plt.xscale('log'); plt.yscale('log')
plt.legend()
plt.xlabel(r'$z$')
plt.ylabel(r'$\rho/\rho_{cr,0}$')
plt.show()
plt.grid()