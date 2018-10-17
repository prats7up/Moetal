import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def vel0(num):
    return np.sin(2.*np.pi*np.linspace(0.,1.,num))

def dxbydt(y0, t0):
    return vel0(np.size(y0))

#initialize particles
n = 10000 #number of particles
x = np.linspace(0,1,n)
v = vel0(n)
#plt.plot(x,v,'o')
#plt.show()

t=np.linspace(0,2./(2.*np.pi),2)

sol = odeint(dxbydt, x, t)
#plt.plot(sol[1,:],v,'+')
#plt.grid()

#plt.figure()
plt.hist(x,bins=np.arange(0,1,0.005))
plt.hist(sol[1,:],bins=np.arange(0,1,0.005))
#plt.plot(x,10.*(x-0.5)**-.5,'-')
plt.show()
plt.xscale('linear')
plt.yscale('linear')