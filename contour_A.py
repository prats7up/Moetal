import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

gamma = np.linspace(0,3,100)
alpha = np.linspace(0,3,150)

n = 1./(gamma-1.)

A = np.outer( np.divide( (2.*n+1.), np.multiply(n, (3.-2.*n)) ), alpha ) - 4.*np.outer( np.divide(n, np.multiply(n, (3.-2.*n)) ), np.ones(150) ) 


log10A = np.maximum( np.minimum( np.log10(np.exp(1.))*np.multiply( np.outer( np.divide(np.ones(100), n), alpha ) - np.ones((100,150)), np.log(A) ), 5.0*np.ones((100,150)) ), -1.*np.ones((100,150)) )

plt.contourf( alpha, gamma, log10A, 400)
#plt.clim((-2, 4))
plt.title (r'$\log_{10} A$')
plt.xlabel (r'$\alpha$')
plt.ylabel (r'$\gamma$')
plt.colorbar()
plt.show()
