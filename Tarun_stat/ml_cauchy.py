import numpy as np
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
Gamma = 1.0

N=100
y = stats.cauchy.rvs(loc=0.0,scale=Gamma,size=N);
#print (fn(y,np.median(y)), fp(y,np.median(y)))
#set up NR root-finding of ML estimator
rg=np.median(y)
err=1.e10; tol=1.e-4
while (err>tol):
    err = - fn(y,rg)/fp(y,rg)
    rg = rg + err
    print (err)
    err = np.abs(err/rg)