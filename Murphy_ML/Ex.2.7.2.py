import numpy as np
import math
import matplotlib.pyplot as plt

lmax = 8; num = np.zeros(lmax,dtype=int); pi_est = np.zeros(lmax); pi_var = np.zeros(lmax)
for l in range(1,lmax):
    num[l] = int(10**l)
    y = np.random.uniform(0,1,num[l])
    z = np.random.uniform(0,1,num[l])
    rsqr = np.square(y) + np.square(z)
    condn = np.where (rsqr<=1.0, 1.0, 0.0)
    pi_est[l] = 4.*np.mean(condn)
    pi_var[l] = 4.*np.var(condn,ddof=1)
plt.plot(num, np.abs(pi_est-math.pi),'o-', label='true error')
x = np.linspace(1.0, num[7], 100)
plt.plot(x, math.pi*x**-0.5,label='error scaling')
plt.legend()
plt.xlabel('sample size')
plt.ylabel(r'error in estimation of $\pi$')
plt.yscale('log')
plt.xscale('log')
plt.show()