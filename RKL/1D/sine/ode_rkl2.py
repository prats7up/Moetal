import numpy as np
import matplotlib.pyplot as plt

def solvr(Y, tau):
	return -D*kw*kw*Y*tau

def main():
	plt.clf()
	global D, kw
	kw = 2.*np.pi
	D = 1.0
	time = 0.0
	dt_exp = 2./(D*kw*kw)
	s = 2 #number of substages
	w1 = 4./(s*s+s-2.)	
	dt_rkl = 1.e-2*0.25*(s*s+s-2.)*dt_exp 
	tend = 0.1
	#initialize temperature
	T0 = 1.0 
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
		Ys = np.zeros([3])
		Ys[0] = Ys0 = T
		j = 1
                mujt = w1/3.
                bjm1 = bjm2 = 1./3.
		Ys[1] = Ys[0] + solvr(Ys[0], mujt*dt)
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
	print T, T0*np.exp(-tend*D*kw*kw)

if __name__ == '__main__':
	main()
