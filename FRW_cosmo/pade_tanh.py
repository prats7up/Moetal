import numpy as np
import matplotlib.pyplot as plt
import math

def pade22(x): #Pade approx. of exp(x)
    return (1.+x/2.+x**2/12.)/(1-x/2.+x**2/12.)

def pade33(x):
    return (1.+x/2.+x**2/10.+x**3/120.)/(1-x/2.+x**2/10.-x**3/120.)

def pade44(x):
    return (1.+x/2.+3.*x**2/28.+x**3/84.+x**4/1680.)/(1.-x/2.+3.*x**2/28.-x**3/84.+x**4/1680.)

def pade66(x):
    y=coeff(6,0)+coeff(6,1)*x+coeff(6,2)*x**2+coeff(6,3)*x**3+coeff(6,4)*x**4+coeff(6,5)*x**5+coeff(6,6)*x**6
    return y/(coeff(6,0)-coeff(6,1)*x+coeff(6,2)*x**2-coeff(6,3)*x**3+coeff(6,4)*x**4-coeff(6,5)*x**5+coeff(6,6)*x**6)

def coeff(n,j):
    return math.factorial(2*n-j)*math.factorial(n)/(math.factorial(j)*math.factorial(n-j)*math.factorial(2*n))

x = np.linspace(-1,1,100)
#plt.plot(x,1./(1.+np.exp(-20.*x)),x,0.5*(1.+np.tanh(10*x)))
'''
plt.plot( x,1./(1.+np.exp(-20.*x)),
         x,1./(1.+pade22(-20.*x)), x,1./(1.+pade33(-20.*x)),
         x, 0.5*( 1./(1.+pade22(-20.*x)) + 1./(1.+pade33(-20.*x)) ) )
'''
plt.plot( x,1./(1.+np.exp(-20.*x)), x,1./(1.+pade44(-20.*x)), x,1./(1.+pade22(-20.*x)),x, 1./(1.+pade66(-20.*x)))
plt.show()