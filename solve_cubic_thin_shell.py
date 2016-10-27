import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def fnewton(x, b, csrat, mach): #csrat<<1
	return x*x*x/b + csrat*csrat*x*x - (1.+mach*mach+1./b)*x + mach*mach

def fpnewton(x, b, csrat, mach): #csrat<<1
        return 3.*x*x/b + 2.*csrat*csrat*x - (1.+mach*mach+1./b)

ngrid = 100
beta = np.logspace(-4, 20, ngrid)
csrat = 1.; mach = 100.0

for i in range(1, ngrid):
	err = 1.e10
	x = 1.e10
	while (err>1.e-6):
		err = -fnewton(x, beta[i], csrat, mach)/fpnewton(x, beta[i], csrat, mach)
		x = x + err
		err = abs(err/x)

	print beta[i], x
