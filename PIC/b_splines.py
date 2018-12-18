import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def integrand(x):
        y=0.0
	if abs(x)<=1.5 and abs(x)>0.5:
		y = 0.5*(1.5-abs(x))**2
	if abs(x)<=0.5:
		y = 0.5*(1.5-2.*x**2)

        return y 


order = 3; num = 100
xi = np.linspace(-0.5*order, 0.5*order,num)
b = np.zeros(num, order)
for l in range(order):
	for i in range(num):
		b[i,l] = integrate.quad(integrand, -0.5*order, xi[i])[0]

xax = np.linspace(-2.0, 2.0, num)
spb = np.zeros(num)
for i in range(num):
    spb[i] = fnc(xax[i])
plt.plot( xax, spb )
plt.show()
plt.grid()
