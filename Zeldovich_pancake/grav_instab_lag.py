import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def derv_cold_norot(y, t):
    rhobyrho0 = np.exp(y[0])
    return [ y[1], rhobyrho0 ]

def derv_cold_wrot(y, t):
    rhobyrho0 = np.exp(y[0])
    return [ y[1], rhobyrho0*(1. - Omega*Omega*rhobyrho0) ]

nt = 100
t = np.linspace(0.0, 2.22, nt)
y0 = [0.0, 0.0] #some initial condition
#sol = odeint(derv_cold_norot, y0, t)

global Omega
Omega=0.0
sol = odeint(derv_cold_wrot, y0, t)

plt.plot(t, np.exp(sol[:,0]),'-',label=r'$\Omega=$'+str(Omega))
#plt.plot(t/1.924, np.exp(sol[:,0]),'-',t, (1-t**2)**(-1.8614))
plt.show()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('time')
plt.ylabel(r'$\rho/\rho_0$')
plt.grid()