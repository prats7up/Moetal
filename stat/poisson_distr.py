import numpy as np
from scipy import special
import matplotlib.pyplot as plt

lam = 1.0

np.random.seed(42)

s = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam) #now it has zero mean like the standard normal distr.
s1 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s2 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s3 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s4 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s5 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s6 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s7 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s8 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)
s9 = (np.random.poisson(lam, 10000) - lam)/np.sqrt(lam)

final = s*s + s1*s1 #+ s2*s2 + s3*s3 + s4*s4 + s5*s5 + s6*s6 + s7*s7 + s8*s8 + s9*s9

count, bins, ignored = plt.hist(final, 30, normed=True)
num=2
chi2=0.5**(num/2.)*bins**(num/2.-1.)*np.exp(-bins/2.)/special.gamma(num/2.)
plt.plot(bins, chi2, linewidth=2, color='r')

#count, bins, ignored = plt.hist(s, 14, normed=True)
#plt.plot(bins, lam**bins*np.exp(-lam)/special.gamma(1.+bins), linewidth=2, color='r')
#sigma=np.sqrt(lam); mu=lam;
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='k')
plt.show()
#plt.yscale('log')
#plt.xscale('log')