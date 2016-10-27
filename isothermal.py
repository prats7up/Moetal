import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def solvr(Y, t):
	return[Y[1], -2.*Y[1]/t - np.exp(-Y[0]) ]
#	return[Y[1], -2.*Y[1]/t + np.exp(-Y[0]) ] #original

def main():
	a_t = np.arange(0.0001, 100.0, 0.001)
	asol = integrate.odeint(solvr, [0.0, 0.0], a_t)
#	line1, = plt.loglog( a_t, np.exp(-asol[:,0]), label="numerical solution",   \
#	a_t, 1./np.power(1.+np.multiply(a_t/3.,a_t/3.), 1.5), label="King profile", \
#	a_t, 2./np.multiply(a_t,a_t), label="SIS"  )
        plt.loglog( a_t, np.exp(-asol[:,0]),  \
        a_t, 1./np.power(1.+np.multiply(a_t/3.,a_t/3.), 1.5), \
        a_t, 2./np.multiply(a_t,a_t) )
	plt.xlim([0.1, 100.])
	plt.ylim([1.e-5, 10.])
	plt.xlabel(r'$r/c_Tt_0$')
	plt.ylabel(r'$\rho/\rho_0$')
	plt.show()
	#astack = np.c_[a_t, asol[:,0], asol[:, 1]]
	#np.savetxt('approx.csv', astack, delimiter=',', header='t, y, yd', comments='')

if __name__ == '__main__':
	main()
