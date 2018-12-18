import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

x = np.linspace(-1,1,100)
ftanh = 0.5*(1.+np.tanh(10*x))
fatan = 0.5 + np.arctan(10.*x)/np.pi 
ferf = 0.5*(1.+erf(10.*x))

plt.plot(x,ftanh,x,fatan,x,ferf)

#f = 0.5 + np.arctan(10.*x)/np.pi 

'''
f1by5 = f**(1./5.)
f5 = f**5

df = np.diff(f)/np.diff(x)
df1by5 = np.diff(f1by5)/np.diff(x)
df5 = np.diff(f5)/np.diff(x)

x1 = x[:-1]; x2 = x1[:-1]

d2f = np.diff(df)/np.diff(x1)
d2f1by5 = np.diff(df1by5)/np.diff(x1)
d2f5 = np.diff(df5)/np.diff(x1)

plt.plot(x,f, x, f1by5, x, f5)
plt.plot(x1,df, x1, df1by5, x1, df5)
plt.plot(x2,d2f, x2, d2f1by5, x2, d2f5)
'''

plt.grid()
plt.show()