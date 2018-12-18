import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def psi(z):
    return 0.015*(1+z)**2.7/(1.+((1+z)/2.9)**5.6)

def Ez(z):
    return np.sqrt(Om*(1.+z)**3+(1.-Om)) 

def integrand(z):
    return -psi(z)/(H0*(1.+z)*Ez(z))
    
global Om, H0
Om = 0.3; H0 = 70.e5/3.086e24/3600./24./365. #Hubble constant in yr^-1
num = 500
z = np.linspace(0., 8., num)
MspercV = np.zeros((num,2))
for i in range(num):
    MspercV[i,:] = integrate.quad(integrand,10000.,z[i])

#plt.plot(z,MspercV[:,0])
#plt.plot(z[1:num],-np.diff(MspercV[:,0]))
plt.plot(z,np.log10(psi(z)))
#plt.xlim([0.,8])
plt.xscale('log')
#plt.yscale('log')
plt.show()