import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

def fn(xi,x0):
    num=np.size(xi); sum1=0.0
    for i in range(num):
        sum1 = sum1 + (xi[i]-x0)/(Gamma*Gamma+(xi[i]-x0)*(xi[i]-x0))
    return sum1

def fp(xi,x0):
    num=np.size(xi); sum1=0.0
    for i in range(num):
        sum1 = sum1 -1.0/(Gamma*Gamma+(xi[i]-x0)*(xi[i]-x0))
        sum1 = sum1 + 2.*(xi[i]-x0)*(xi[i]-x0)/(Gamma*Gamma+(xi[i]-x0)*(xi[i]-x0))/(Gamma*Gamma+(xi[i]-x0)*(xi[i]-x0))
    return sum1

global Gamma
Gamma=1.0
num = 9; mn = np.zeros(num); st = np.zeros(num)
n = np.zeros(num, dtype=int); med = np.zeros(num); mle = np.zeros(num)
for l in range(1,num):
    n[l]=10**l
    y=np.random.standard_cauchy(n[l])
    mn[l]=np.mean(y)
    st[l]=np.std(y,ddof=1)
    med[l]=np.median(y)
    rg=med[l]
    err=1.e10; tol=1.e-4
    while (err>tol):
        err = - fn(y,rg)/fp(y,rg)
        rg = rg + err
        #print (err)
        err = np.abs(err/rg)
    mle[l] = rg
plt.loglog(n[1:num], np.abs(mn[1:num]), '+',label='|mean|')
plt.loglog(n[1:num], np.abs(med[1:num]), '^',label='|median|')
plt.loglog(n[1:num], np.abs(mle[1:num]), 'v',label='|MLE|')
plt.loglog(n[1:num], st[1:num],'o',label='std')
plt.legend()
plt.grid()
plt.xlabel('sample size')
plt.ylabel('absolute value of mean, standard deviation')
plt.title('Cauchy distribution properties')
plt.show()