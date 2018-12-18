import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def fn(Om, Ov):
    return 1.5*Om*(2.*Ov)**(1./3.) - (Om+Ov-1.)*Om**(1./3.)
    
def fp(Om, Ov):
    return 0.5*2.**(1./3.)*Om/Ov**(2./3.) - Om**(1./3.)

num = 100
O_m = np.linspace(0.001,2.0,num); O_v_noBB = np.zeros(num)
O_v_flat = 1.-O_m
tol = 1.e-10
for i in range(num):
    #O_vg = O_m[i]
    O_vg = 0.0001
    err = 1.e10
    while (err>tol):
        func = fn(O_m[i], O_vg); fprime=fp(O_m[i], O_vg)
        err = -func/fprime
        O_vg = O_vg + err
        print(err)
        err = abs(err/O_vg)
    O_v_noBB[i] = O_vg
#plt.figure()
plt.plot(O_m,O_v_noBB)
#plt.plot(O_m,O_v_flat)
plt.ylabel('$\Omega_\Lambda$')
plt.xlabel('$\Omega_m$')
plt.show()