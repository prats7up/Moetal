import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def ret_fn(x1):
#        return 0.5*(1./x1+x1) 
	return 0.5*x1 - 5.0

x = 1.4
err = 1.e10
tol = 1.e-6
a = np.array(x)

while err>tol :
  y = ret_fn(x)
  err = np.abs(x-y)/np.abs(x)
  print x, y, err
  a = np.append(a,y)
  x = y

plt.plot(np.linspace(-10,10,100), 5.*np.linspace(-10,10,100)-2, np.linspace(-10,10,100), np.linspace(-10,10,100))

plt.plot(a)
plt.show()
