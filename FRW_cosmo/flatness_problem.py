import numpy as np
import matplotlib.pyplot as plt

def Efac(a):
    return np.sqrt(O_r/a**4 + O_m/a**3 + O_v + (1.-O_r-O_m-O_v)/a**2 )    


global O_m, O_v, O_r
O_m = 0.3; O_v=0.69; O_r = 1.e-4
a = np.logspace(-33, 0, 100) #a=1.e-32 corresponds to the Universe compressed to Planck lenght
one_m_O =  (1.-O_m-O_r-O_v)/(a*Efac(a))**2
plt.plot(a, one_m_O)
plt.xscale('log')
plt.yscale('log')
plt.grid('on')
plt.xlabel('scale factor')
plt.ylabel('devitation from $\Omega=1$')
plt.show()