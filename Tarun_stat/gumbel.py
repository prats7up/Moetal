import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

num=10000; ymax = np.zeros(num); ymin = np.zeros(num)
N_sample_size = 100000
for i in range(num):
    l=N_sample_size
    y_normal=np.random.standard_cauchy(size=l)
    #y_normal=np.random.normal(l)
    ymax[i] = np.log(np.max(y_normal))
    #ymin[i] = np.min(y_normal)

#plt.hist(ymax,bins=np.arange(-0.1,6,0.1), normed=True,label='Normal sample size='+str(N_sample_size))
#plt.hist(ymax, normed=True,bins=np.arange(1.0,20,0.1), label='Cauchy sample size='+str(N_sample_size))
plt.hist(ymax, normed=True,bins=np.arange(1.0,20,0.1), label='max of sample size='+str(num))
#plt.hist(ymax,bins=np.arange(-0.1,6,0.1), normed=True,label='Uniform sample size='+str(N_sample_size))
#plt.hist(ymin,normed=True,label='minimum')
plt.legend()
plt.xlabel('x')
plt.ylabel('pdf')
#plt.title('pdf of maximum of Uniform variates in 1000 trials & Gumbel fit')
plt.title('pdf of maximum of log of Cauchy variates in 1000 trials & Gumbel fit')
beta = math.sqrt(6.)*np.std(ymax)/math.pi
EM_const =  0.57721566
mu = np.mean(ymax) - beta*EM_const #relation from Wikipedia
x=np.linspace(0,20,100)
gum = np.exp(-(x-mu)/beta)*np.exp(-np.exp(-(x-mu)/beta))/beta
plt.plot(x,gum)
#plt.yscale('log')
plt.show()