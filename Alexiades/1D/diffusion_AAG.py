import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_chebyt, eval_chebyu

def solvr(Y, tau):
	MY = np.zeros(nx)
	for l in range(nx):
		lm = l-1
		lp = l+1
		#periodic BC
		if (l==0):
			lm = nx-1
		if (l==nx-1):
			lp = 0
		MY[l] = D*tau*(Y[lm]-2.*Y[l]+Y[lp])/(dx*dx)
	return MY

def main():
	plt.clf()
	global dx, D, nx
	nx = 100
	x = np.linspace(-1.0,1.0,nx)
	dx = x[1]-x[0]
	D = 1.0
	time = 0.0
	dt_exp = 0.5*dx*dx/D
	s = 50 #number of substages
	nu = 0.05 #stability parameter
	dt_aag = s*dt_exp*( (1.+np.sqrt(nu))**(2.*s)-(1.-np.sqrt(nu))**(2.*s)  )/(2.*np.sqrt(nu)) 
	dt_aag = dt_aag/( (1.+np.sqrt(nu))**(2.*s)+(1.-np.sqrt(nu))**(2.*s)  )
	tend = 0.1
	#initialize temperature
	T0 = np.sin(2.*np.pi*x)
	T=T0
	while (time<tend):
		if ( time+dt_aag <tend):
			time = time+dt_aag
			dt = dt_aag
		else:
			dt = tend-time
			time = tend
		#print time, dt
		#now start aag substeps
		Ys = T; sum_dt = 0.0
		for j in range(s):
			dtj = dt_exp/( (-1.+nu)*np.cos(0.5*(2.*j+1.)*np.pi/s) + 1. + nu )
			sum_dt = sum_dt + dtj
			Ys = Ys + solvr(Ys, dtj)
		T = Ys
		#print sum_dt, dt_aag
	kw = 2.*np.pi
	plt.plot(x,T0,x,T,x,np.exp(-D*kw*kw*tend)*T0)
	plt.show()
	print np.mean(T0), np.mean(T), s
	#fname = "data_aag2_s5_dtby4"+str(s)+".out"
	fname = "data_aag2_s20_dt.out"
	np.savetxt(fname, np.column_stack((x,T)) )

if __name__ == '__main__':
	main()
