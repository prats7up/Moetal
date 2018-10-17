import numpy as np
from scipy import special
import matplotlib.pyplot as plt

mu, sigma = 0.0, 1.0

np.random.seed(42)

s = np.random.normal(mu, sigma, 10000)
s1 = np.random.normal(mu, sigma, 10000)
s2 = np.random.normal(mu, sigma, 10000)
s3 = np.random.normal(mu, sigma, 10000)
s4 = np.random.normal(mu, sigma, 10000)
s5 = np.random.normal(mu, sigma, 10000)
s6 = np.random.normal(mu, sigma, 10000)
s7 = np.random.normal(mu, sigma, 10000)
s8 = np.random.normal(mu, sigma, 10000)
s9 = np.random.normal(mu, sigma, 10000)

final = s*s + s1*s1 + s2*s2 + s3*s3 + s4*s4 + s5*s5 + s6*s6 + s7*s7 + s8*s8 + s9*s9

count, bins, ignored = plt.hist(final, 30, normed=True)
num=10
plt.plot(bins, 0.5**(num/2.)*bins**(num/2.-1.)*np.exp(-bins/2.)/special.gamma(num/2.), linewidth=2, color='r')
plt.xscale('log')
plt.yscale('log')
#count, bins, ignored = plt.hist(s, 30, normed=True) #normalized
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()