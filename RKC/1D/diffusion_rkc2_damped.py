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
	s = 20 #number of substages
	eps = 2./13.
	dt_rkc = (1./3.)*(s*s-1.)*(1.-2.*eps/15.)*dt_exp 
	w0 = 1. + eps/(s*s)
	der = s*eval_chebyu(s-1, w0) #T derivative expressed in terms of U
	dder = s*( (s+1.)*eval_chebyt(s,w0) - eval_chebyu(s,w0) )/(w0*w0-1.0) #second derivative
	w1 = der/dder 
	tend = 0.1
	#initialize temperature
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
		j = 2
		der = j*eval_chebyu(j-1, w0)
		dder = j*( (j+1)*eval_chebyt(j,w0) - eval_chebyu(j,w0) )/(w0*w0-1.0)
		bjm1 = bjm2 = bj = dder/(der*der) 
		mujt = bjm1*w1 
		Ys[1,:] = Ys[0,:] + solvr(Ys[0,:], mujt*dt)
		for j in range(2,s+1):
			der = j*eval_chebyu(j-1, w0)
			dder = j*( (j+1)*eval_chebyt(j,w0) - eval_chebyu(j,w0) )/(w0*w0-1.0)
			bj = dder/(der*der) 
			muj = 2.*w0*bj/bjm1 
			nuj = -bj/bjm2
			#print muj+nuj
			mujt = 2.*w1*bj/bjm1
			gt = -(1.-bjm1*eval_chebyt(j-1,w0))*mujt 
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
	#fname = "data_rkc2_s5_dtby4"+str(s)+".out"
	fname = "data_rkc2_s20_dt.out"
	np.savetxt(fname, np.column_stack((x,T)) )

if __name__ == '__main__':
	main()