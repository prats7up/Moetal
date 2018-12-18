import numpy as np
import matplotlib.pyplot as plt

def Phi_eff(a):
    return -0.5*a*a*(O_r/a**4 + O_m/a**3 + O_v)

global O_r, O_m, O_v
#actual
#O_m = 0.3089; O_v=0.6911; O_r = 1. - O_m - O_v
O_m = 2.0; O_v = 0.01; O_r = 0.0
num = 100
a = np.linspace(0.1, 10, num)
Phi = Phi_eff(a)
E = 0.5*(1.-O_m-O_r-O_v)*np.ones(num)
plt.plot(a, Phi, '-',label='$\Phi_{eff}$ for $\Omega_m,\Omega_v$ ='+str(O_m)+','+str(O_v) ) 
plt.plot(a, E, '--',label='E='+str(E[0])+'; $\Omega_m+\Omega_v=$'+str(O_m+O_v))
plt.legend()
plt.xlabel('a')
plt.ylabel('effective potential')
plt.grid()
plt.show()