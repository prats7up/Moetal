import math
import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if (n<2):
        print ("try a number >=2")
        return
    sqrtn = int(math.ceil(math.sqrt(n)))+1
    print(sqrtn)
    out = 1
    for i in range(2,sqrtn):
        if ( n%i==0 ):
            out = 0
            break
    return out
    
nprime = np.zeros(100,dtype=int)
num = 0
for j in range(100):
    if (j==0):
        jbeg = 2
    else:
         jbeg = j*1000   
    for k in range(jbeg,(j+1)*1000):
        num = num + 1
        if (is_prime(k)==1):
            nprime[j] = nprime[j]+1

x = np.linspace(1,100*100,100)
plt.plot(x,nprime,'o',label='actual distribution')
plt.plot(x,1000./np.log(x),label='expected distribution, 1000/log(n)')
plt.title('distribution of prime numbers till 100000, bin-size=1000')
plt.legend()
plt.xlabel('n')
plt.ylabel('number of primes in each bin')
plt.show()