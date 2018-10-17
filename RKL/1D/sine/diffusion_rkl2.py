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
	s = 20 #number of substages
	w1 = 4./(s*s+s-2.)
	dt_rkl = 0.25*(s*s+s-2.)*dt_exp 
	tend = 0.1
	#initialize temperature
	eps = 0.01
	#T0 = np.exp(-x*x/(2.*D*eps))/np.sqrt(2.*np.pi*D*eps)
	T0 = np.sin(2.*np.pi*x)
	T=T0
	while (time<tend):
		if ( time+dt_rkl <tend):
			time = time+dt_rkl
			dt = dt_rkl
		else:
			dt = tend-time
			time = tend
		print time, dt
		#now start rkl substeps
		Ys = np.zeros([3,nx])
		Ys[0,:] = T; Ys0 = T
		j = 1
		mujt = w1/3.
		bjm1 = bjm2 = 1./3.
		Ys[1,:] = Ys[0,:] + solvr(Ys[0,:], mujt*dt)
		for j in range(2,s+1):
			bj = (j*j+j-2.)/(2.*j*(j+1.))
			muj = (2.*j-1.)*bj/(j*bjm1)
			nuj = -(j-1.)*bj/(j*bjm2)
			mujt = muj*w1
			gt = -(1.-bjm1)*mujt 
			Ys[2] = muj*Ys[1] + nuj*Ys[0] + (1.-muj-nuj)*Ys0 + solvr(Ys[1], mujt*dt) + solvr(Ys0, gt*dt)
			Ys[0] = Ys[1]
			Ys[1] = Ys[2]
			bjm2 = bjm1
			bjm1 = bj
		T = Ys[2]
	kw = 2.*np.pi
	plt.plot(x,T0,x,T,x,np.exp(-D*kw*kw*tend)*T0)
	plt.show()
	print np.mean(T0), np.mean(T), s
	#fname = "data_rkl2_s5_dtby4"+str(s)+".out"
	fname = "data_rkl2_s20_dt.out"
	np.savetxt(fname, np.column_stack((x,T)) )

if __name__ == '__main__':
	main()
