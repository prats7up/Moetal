import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N=10000
y=np.zeros(N)
for i in range(N):
    #y[i]=np.mean((np.random.normal(loc=0.0,scale=1.0,size=100)))
    y[i]=np.sum((stats.cauchy.rvs(loc=0.0,scale=1.0,size=1000)))
    #y[i]=np.sum(np.random.standard_cauchy(size=1000))
plt.hist(y,bins=100,normed=True,label='1000')
plt.yscale('log')
#plt.hist(y,normed=True,bins=np.arange(-5,5,0.03),label='50000,finer bins')
#plt.hist(y, bins=np.arange(-1,1,0.003),normed=True)
plt.xlabel('x')
plt.ylabel('pdf')
plt.title('pdf of sum of 10 std. Cauchy rvs, using (10,100,1000,10000) realizations')
plt.show()