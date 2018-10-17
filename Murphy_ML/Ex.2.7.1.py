import numpy as np
import math
import matplotlib.pyplot as plt

lmax = 5; num=np.zeros(lmax,dtype=int)
for l in range(1,lmax):
    num[l]=int(10**l)
    y=np.random.uniform(0,1,num[l])
    ysqr = np.square(y)
    plt.hist(ysqr,normed=True, bins=np.arange(0,1,0.01), label=str(10**l))
y = np.linspace(0.001,1,1000)
plt.plot(y, 1.0/np.sqrt(4.*y),label=r'$(4 y)^{-1/2}$')
plt.legend()
plt.show()