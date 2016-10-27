import numpy as np
import matplotlib.pyplot as plt

def solvr(Y, tau):
	MY = np.zeros(nx)
	for l in range(nx):
		lm = l-1
		lp = l+1
		if (l==0):
			lm = nx-1
		if (l==nx-1):
			lp = 0
		MY[l] = D*tau*(Y[lm]-2.*Y[l]+Y[lp])/(dx*dx)
	return MY

def main():
	global dx, D, nx
	nx = 400
	x = np.linspace(-1.0,1.0,nx)
	dx = x[1]-x[0]
	D = 1.0
	time = 0.0
	dt_exp = 0.5*dx*dx/D
	tend = 0.1
	#initialize temperature
	eps = 0.01
	#T0 = np.exp(-x*x/(2.*D*eps))/np.sqrt(2.*np.pi*D*eps)
	T0 = np.sin(2.*np.pi*x)
	T=T0
	while (time<tend):
		if ( time+dt_exp <tend):
			time = time+dt_exp
			dt = dt_exp
		else:
			dt = tend-time
			time = tend
		print time, dt
		Tnew = T + solvr(T, dt)
		T = Tnew	

	#plt.plot(x,T0,x,T,x,np.exp(-x*x/(4.*tend*D))/np.sqrt(4.*np.pi*D*tend))
	kw = 2.*np.pi
        plt.plot(x,T0,x,T,x,np.exp(-D*kw*kw*tend)*T0)
	plt.show()
	print np.mean(T0), np.mean(T)
if __name__ == '__main__':
	main()
