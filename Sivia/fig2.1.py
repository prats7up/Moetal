#Sivia's problem corresponding to Fig. 2.1

import numpy as np
import matplotlib.pyplot as plt
import math
from pynverse import inversefunc

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

ntrials = 1000
nx = 1000
x = np.linspace(0,1,nx)
#prior = np.ones(nx) #uniform prior
#prior = normalize(np.exp(-(x-0.5)**2/(2.*.1*.1))) # Gaussian prior with width 0.1
prior = normalize(1./(np.sin(np.pi*(x))+1.e-2)) #large prior at edges

for i in range(ntrials):
    y=np.random.binomial(1,0.25) #toss a head with probabiblity 0.25
    print (y)
    if (y==1):
        L = x
    else:
        L = 1.-x    
    P = normalize(L*prior)
    prior = P
plt.plot(x,P,x,max(P)*np.ones(nx)*0.242,'--',label=str(ntrials))
plt.xlabel('probability of getting a head')
plt.ylabel('normalized posterior')
plt.grid('on')
plt.show()