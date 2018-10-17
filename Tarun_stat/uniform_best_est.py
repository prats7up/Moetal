import numpy as np
import math
import matplotlib.pyplot as plt

lmax=8; num=np.zeros(lmax,dtype=int); sm=np.zeros(lmax); sd=np.zeros(lmax)
sig=np.zeros(lmax); be=np.zeros(lmax); med=np.zeros(lmax)
for l in range(1,lmax):
    num[l]=int(10**l)
    y=np.random.uniform(0,1,num[l])
    sm[l] = np.mean(y)
    sd[l] = np.std(y,ddof=1)
    ymax=max(y); ymin=min(y)
    be[l] = 0.5*(ymax+ymin)
    med[l] = np.median(y)
    sig[l] = 0
    for i in range(num[l]):
        sig[l] = sig[l] + (y[i]-be[l])*(y[i]-be[l])
    sig[l] = math.sqrt(sig[l]/(num[l]-1))
    #print (num, sm-0.5, sd, be-0.5, sig)
    #np.savetxt ('data.out',(sm-0.5, sd, be-0.5, sig))
plt.loglog(num[1:lmax],abs(be[1:lmax]-.5),'+',label='|best estimator-0.5|')
plt.loglog(num[1:lmax],sd[1:lmax],'+',label='standard deviation')
plt.loglog(num[1:lmax],abs(sm[1:lmax]-.5),'o',label='|arithematic mean-0.5|')
plt.loglog(num[1:lmax],abs(med[1:lmax]-.5),'^',label='|median-0.5|')
plt.loglog(num[1:lmax],sig[1:lmax],'o',label='standard dev with mu=best estimator')
plt.legend()
#plt.loglog(num[1:lmax], -sm[1:lmax]+0.5, num[1:lmax], -be[1:lmax]+0.5)
plt.grid()
plt.xlabel('sample size')
plt.ylabel('absolute value of (mean-0.5), standard deviation')
plt.title('Best estimator for uniform distribution')
plt.show()