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
	plt.clf()
	global dx, D, nx
	nx = 1000
	x = np.linspace(-10.0,10.0,nx)
	dx = x[1]-x[0]
	D = 1.0
	time = 0.0
	dt_exp = 0.5*dx*dx/D
	s = 5 #number of substages
	w1 = 2./(s*s+s)	
	dt_rkl = 0.125*0.5*(s*s+s)*dt_exp 
	tend = 0.1
	#initialize temperature
	eps = 0.01
	T0 = np.exp(-x*x/(2.*D*eps))/np.sqrt(2.*np.pi*D*eps)
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
		Ys[0,:] = T
		j = 1
		mujt = (2.*j-1.)*w1/j
		Ys[1,:] = Ys[0,:] + solvr(Ys[0,:], mujt*dt)
		for j in range(2,s+1):
			muj = (2.*j-1.)/j
			mujt = (2.*j-1.)*w1/j
			nuj = (1.-j)/j
			Ys[2] = muj*Ys[1] + nuj*Ys[0] + solvr(Ys[1], mujt*dt)
			Ys[0] = Ys[1]
			Ys[1] = Ys[2]	
		T = Ys[2]	
	plt.plot(x,T0,x,T,x,np.exp(-x*x/(4.*tend*D))/np.sqrt(4.*np.pi*D*tend))
	plt.show()
	print np.mean(T0), np.mean(T), s
	fname = "data_rkl1_s5_dtby8"+str(s)+".out"
	np.savetxt(fname, np.column_stack((x,T)) )

if __name__ == '__main__':
	main()
