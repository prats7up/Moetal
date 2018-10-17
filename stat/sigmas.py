import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import erf
from scipy.stats import norm

def gaussian(x,mu,sig):
    return np.exp(-(x-mu)*(x-mu)/(2.*sig*sig))/np.sqrt(2.*np.pi*sig)

x=np.linspace(-5,5,100)
plt.plot(x,erf(x),x,gaussian(x,0.0,1.0))
plt.grid()
plt.show()