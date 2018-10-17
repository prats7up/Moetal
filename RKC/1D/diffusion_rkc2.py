import numpy as np
import matplotlib.pyplot as plt

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
	s = 3 #number of substages
	dt_rkc = 2.*s*s*dt_exp 
	tend = 0.1
	#initialize temperature
	eps = 0.01
	#T0 = np.exp(-x*x/(2.*D*eps))/np.sqrt(2.*np.pi*D*eps)
	T0 = np.sin(2.*np.pi*x)
	T=T0
	while (time<tend):
		if ( time+dt_rkc <tend):
			time = time+dt_rkc
			dt = dt_rkc
		else:
			dt = tend-time
			time = tend
		print time, dt
		#now start rkc substeps
		Ys = np.zeros([3,nx])
		Ys[0,:] = T; Ys0 = T
		j = 1
		mujt = 1./(s*s)
		Ys[1,:] = Ys[0,:] + solvr(Ys[0,:], mujt*dt)
		for j in range(2,s+1):
			muj = 2.0 
			nuj = -1.0
			mujt = 2./(s*s)
			Ys[2] = muj*Ys[1] + nuj*Ys[0] + (1.-muj-nuj)*Ys0 + solvr(Ys[1], mujt*dt)
			Ys[0] = Ys[1]
			Ys[1] = Ys[2]
		T = Ys[2]
	kw = 2.*np.pi
	plt.plot(x,T0,x,T,x,np.exp(-D*kw*kw*tend)*T0)
	plt.show()
	print np.mean(T0), np.mean(T), s
	#fname = "data_rkc2_s5_dtby4"+str(s)+".out"
	fname = "data_rkc2_s20_dt.out"
	np.savetxt(fname, np.column_stack((x,T)) )

if __name__ == '__main__':
	main()
