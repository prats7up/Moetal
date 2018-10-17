#posterior probability for phase phi if photon arrival times from a periodic source are given.
 
import numpy as np
import matplotlib.pyplot as plt
import math
from pynverse import inversefunc

def lc(t): #lightcurve
    return (5./3.)*( 0.1 + np.sin(math.pi*(t+phi0))*np.sin(math.pi*(t+phi0)) ) #normalized
    '''s = (t+phi0)%1.0; x=0.0
    if (s < 0.6  and s >= 0.4):
        x = 5.0
    return x   ''' 
def cpdf(t):
    return (5./3.)*( 3.*t/5. - (np.sin(2.*math.pi*(t+phi0))-np.sin(2.*math.pi*phi0))/(4.*math.pi) ) #normalized CPDF to generate arrival times
    '''
    sz = np.size(t); x=np.zeros(sz); s = (t+phi0)%1.0 
    print('here')
    if (s >= 0.4 and s < 0.6):
        x = (s-0.4)*5.
    if s >= 0.6:
        x = 1.0
    return x'''
    
# generate photon arrival times, assuming that the probability is proportional to lum, assume period is 1 and phi0=0.25
global phi0
phi0=0.0
num_ph=400
inv_cpdf = inversefunc(cpdf)
yunif = np.random.uniform(0.0,1.0,num_ph)
Tarr = inv_cpdf(yunif)

num=300
phi = np.linspace(0,1,num)
'''
lnP = np.zeros(num)
for i in range(num_ph):
    lnP = lnP + np.log(lc(Tarr[i] + phi))
'''
T_plus_phi = np.outer(Tarr,np.ones(num)) + np.outer(np.ones(num_ph),phi)
P = lc(T_plus_phi); #P_phi = np.prod(P,axis=0)
lnP = np.sum( np.log(P), axis=0 )
plt.figure()
plt.plot(phi, lnP)#, 'o',phi, np.log(P_phi))
plt.show()
plt.grid()