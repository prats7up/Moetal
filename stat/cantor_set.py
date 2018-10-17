import numpy as np
#from scipy import special
import matplotlib.pyplot as plt

#create Cantor set by splitting the unit interval into thirds
n=10; ivl=np.zeros((n,2**n))
ivl[0,0] = 1./3.; ivl[0,1] = 2./3.; #ivl[1,0]=1./3**2; ivl[1,1]=2./3**2
for i in range(1,n): #more elegant was of doing it must be there!
    dl=1./3.**(i+1); dl2=2*dl
    for k in range(2**(i+1)):
        print (i, k)
        if (np.mod(k,4)==2):
            ivl[i,k] = ivl[i-1,k/2]+dl
        if (np.mod(k,4)==3):
            ivl[i,k] = ivl[i-1,k/2]+dl2
        if (np.mod(k,4)==0):
            ivl[i,k] = ivl[i-1,(k+2)/2]+dl-2./3.**i
        if (np.mod(k,4)==1):
            ivl[i,k] = ivl[i-1,(k+2)/2]+dl2-2./3.**i           
#plt.plot(np.abs(ivl[3,:]-0.5),'o') 
plt.plot(ivl,'o',np.linspace(0,n+1,100),0.25*np.ones(100),'-')
plt.show()
plt.grid()