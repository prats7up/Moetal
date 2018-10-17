import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

N_sample_size = 100000
l=N_sample_size
#plt.figure()
y_cauchy=np.random.standard_cauchy(size=l)
#plt.hist(y_cauchy,normed=True, label='log-Cauchy')
plt.figure()
#log_cauchy = np.log10(np.maximum(0.001,y_cauchy))
log_cauchy = np.log10(np.abs(y_cauchy))
plt.hist(log_cauchy,normed=True, bins=np.arange(-3.1,6,0.1), label='log-Cauchy')
x=np.linspace(0,3,100)
plt.plot(x,0.3*np.exp(-x*x),label=r'$0.3*e^{-x^2}$')
plt.plot(x,0.3*np.exp(-x),label=r'$0.3*e^{-x}$')
plt.plot(x,np.exp(x)/math.pi/(1.+np.exp(2*x)),label=r'$\frac{e^x}{\pi(1+e^{2x})}$')
plt.legend()
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('')
plt.show()