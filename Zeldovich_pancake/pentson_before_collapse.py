import numpy as np
import matplotlib.pyplot as plt

beta = np.logspace(-3,2,100)
r = np.sqrt(beta)*(1.+beta)**(2./3.) #by r0
rho = 3./(3.+10.*beta+7.*beta*beta) #by rho0
v = np.sqrt(beta)/(1.+beta)**(1./3.) #by v0
plt.plot(r,rho,label='density')
plt.plot(r,v,label='velocity')
plt.show()
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel (r'$r/r_0$')