import numpy as np
import matplotlib.pyplot as plt

l=10000
y_normal=np.random.standard_normal(l)
y_cauchy=np.random.standard_cauchy(l)
y_uniform=np.random.uniform(0,1,l)
#plt.hist(y_cauchy,normed=True,range=(-50,50), label='Cauchy')
plt.hist(y_cauchy,normed=True, label='Cauchy')
plt.hist(y_normal,normed=True,label='Normal')
plt.hist(y_uniform,normed=True,label='Uniform')
plt.yscale('log')
plt.xlabel('x'); plt.ylabel('probability density histograms'); plt.legend()
#plt.grid()
plt.show()