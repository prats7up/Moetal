import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

gamma=5./3.
M1=np.linspace(1.005, 10, 100)

D = 1. + 1./M1**4 - 2.*gamma*gamma/M1/M1

y1 = (gamma-1+2./M1/M1)/(gamma+1)

y2 = M1**0

#plt.plot(M1,y1,M1,y2)
#plt.grid()
#plt.show()

cs2bycs1 = np.sqrt(y1*(1+gamma*M1**2*(1-y1)))
M2 = y1*M1/cs2bycs1


#plt.plot(M1,cs2bycs1,M1,M2,M1,np.sqrt(2*gamma*(gamma-1)*M1**2/(gamma+1)**2),M1,np.sqrt((gamma-1)*M1**0/(2*gamma)))
#plt.grid()
#plt.show()

#frame transformation

vbycs=np.linspace(-10,10,150)
M1p = np.outer(np.ones(150),M1) + np.outer(vbycs,np.ones(100))
M2p = np.outer(np.ones(150),M2) + np.outer(vbycs,1./cs2bycs1)
one = np.ones((150,100))
plt.contourf(M1,vbycs,np.log10(np.maximum(np.maximum(np.abs(M1p),np.abs(M2p)),one)),20)
plt.xlabel(r'${\cal M}_1$')
plt.ylabel(r'$v/c_{s1}$')
plt.colorbar(label=r'$\log_{10}[{\rm max}(|{\cal M}_1^\prime|, |{\cal M}_2^\prime|,1)]$')
plt.show()