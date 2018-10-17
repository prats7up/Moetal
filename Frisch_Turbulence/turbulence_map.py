import numpy as np
import matplotlib.pyplot as plt

def turb_map(x):
    return 1. - 2*x*x
    
num = 50000
x = np.zeros(num)
x[0] = 0.9
for i in range(1, num):
    x[i] = turb_map(x[i-1])
    
plt.hist(x[0:num/5],normed=True,bins=np.arange(-1.5,1.5,0.01))
plt.hist(x[num/5:2*num/5],normed=True,bins=np.arange(-1.5,1.5,0.01))
plt.show()