import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def integrand(a, w_m, w_r, w_v, w_c):
	return 1./np.sqrt(w_c+ w_m/a + w_r/(a*a) + w_v*a*a)	

#cosmological parameters

n_m = 40; n_v = 50
Omega_m = np.linspace(0.01, 1.0, n_m) #0.31*0.0; 
Omega_r = 0.0 #0.0*1.e-4; 
Omega_v = np.linspace(0.01, 1.0, n_v) #0.0*(0.69-1.e-4)
#Omega_c = 1. - Omega_m - Omega_r - Omega_v; 
H0 = 67.74
tage = np.zeros((n_v, n_m, 2))

for v in range(n_v):
    for m in range(n_m):
        Omega_c = 1. - Omega_m[m] - Omega_r - Omega_v[v]
        tage[v,m,:] = integrate.quad(integrand, 0, 1, args=(Omega_m[m], Omega_r, Omega_v[v], Omega_c))
#print 'age of universe in Gyr=', tage[0]*1.e3/H0
Om, Ov = np.meshgrid(Omega_m, Omega_v)
#plt.contourf(Om, Ov, tage[:,:,0]*1.e3/H0) #in Gyr
plt.contourf(Om, Ov, tage[:,:,0],25)
plt.colorbar(label='age of the Universe in units of $H_0^{-1}$')
plt.xlabel('$\Omega_m$')
plt.ylabel('$\Omega_v$')
plt.show()