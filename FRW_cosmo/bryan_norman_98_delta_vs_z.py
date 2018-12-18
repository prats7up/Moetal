import numpy as np
import matplotlib.pyplot as plt

#Bryan & Norman (1998) (Eq. 6) fit for virial overdensity as a function of redshift

def delc(x):
    return 18.*np.pi**2 + 82.*x - 39.*x*x
    
def Ezsqr(z):
    return Om*(1.+z)**3+(1.-Om)

global Om
Om = 0.3089

z = np.linspace(0,10,100)
Omz = Om*(1+z)**3/Ezsqr(z)
plt.plot(z,delc(Omz-1),label='w.r.t. critical density')
plt.plot(z,(delc(Omz-1))/Omz,label='w.r.t. matter density')
plt.xlabel(r'$z$')
plt.ylabel(r'$\Delta$')
plt.legend()
plt.grid()
plt.show()