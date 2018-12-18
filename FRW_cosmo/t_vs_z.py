import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math

def Ez(z):
    return np.sqrt(Om*(1.+z)**3+(1.-Om)) 
    
def integrand_dtbydz(z):
    return -1./(H0*(1.+z)*Ez(z))
    
global Om, H0
Om = 0.3; H0 = 70.e5/3.086e24
num = 500
z = np.linspace(0., 8., num)
MspercV = np.zeros((num,2))
for i in range(num):
    MspercV[i,:] = integrate.quad(integrand_dtbydz,10000.,z[i])

tanal = np.zeros(num)
for i in range(num):
    tanal[i] = (2./3./H0/np.sqrt(1.-Om))*math.asinh(np.sqrt((1.-Om)/(Om*(1.+z[i])**3)))

plt.plot(z,MspercV[:,0]/np.pi/1.e16,z,tanal/np.pi/1.e16)
#plt.plot(z,tanal/np.pi/1.e16)
#plt.plot(z[1:num],-np.diff(MspercV[:,0]))
#plt.xlim([0.,8])
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('z')
plt.ylabel('cosmic time (Gyr)')
plt.title(r'$\Omega_m=0.3, \Omega_\Lambda=0.6$')
plt.grid('on')
plt.show()