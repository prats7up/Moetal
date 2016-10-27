import numpy as np
import matplotlib.pyplot as plt

def L2_norm(Y1, Y2):
	err = 0.0
        for l in range(nx):
		err = err + (Y1[l] - Y2[l])*(Y1[l] - Y2[l])
        return np.sqrt(err/nx)

def L1_norm(Y1, Y2):
        err = 0.0
        for l in range(nx):
                err = err + np.abs(Y1[l] - Y2[l])
        return err/nx

def main():
	plt.clf()
	global nx
	nx = 1000
	x = np.linspace(-10.0,10.0,nx)
        dx = x[1]-x[0]
	s = 5
	Dc = 1.0
	dt_exp = 0.5*dx*dx/Dc
	D_dt = np.loadtxt('data_rkl1_s5_dt.out')
	D_dtby2 = np.loadtxt('data_rkl1_s5_dtby2.out')
        D_dtby4 = np.loadtxt('data_rkl1_s5_dtby4.out')
        D_dtby8 = np.loadtxt('data_rkl1_s5_dtby8.out')

 	err = dt = np.zeros(3)
	err[0] = L2_norm(D_dt[:,1],D_dtby2[:,1])
	err[1] = L2_norm(D_dtby2[:,1],D_dtby4[:,1])
	err[2] = L2_norm(D_dtby4[:,1],D_dtby8[:,1]) 
	#dt[0] = 0.25*(s*s+s-2.)*dt_exp
	dt[0] = 0.5*(s*s+s)*dt_exp
	dt[1] = 0.5*dt[0]
	dt[2] = 0.5*dt[1]

        D_dt = np.loadtxt('data_rkl2_s5_dt.out')
        D_dtby2 = np.loadtxt('data_rkl2_s5_dtby2.out')
        D_dtby4 = np.loadtxt('data_rkl2_s5_dtby4.out')
        D_dtby8 = np.loadtxt('data_rkl2_s5_dtby8.out')

        err2 = dt2 = np.zeros(3)
        err2[0] = L2_norm(D_dt[:,1],D_dtby2[:,1])
        err2[1] = L2_norm(D_dtby2[:,1],D_dtby4[:,1])
        err2[2] = L2_norm(D_dtby4[:,1],D_dtby8[:,1])
        dt2[0] = 0.25*(s*s+s-2.)*dt_exp
        #dt2[0] = 0.5*(s*s+s)*dt_exp
        dt2[1] = 0.5*dt2[0]
        dt2[2] = 0.5*dt2[1]

	plt.plot(dt,err,'-o',dt2,err2,'-^')
	plt.yscale('log')
	plt.xscale('log')
	plt.xlabel('super timestep')
	plt.ylabel('Richardson L2 error for s=5')
	plt.legend(('RKL1','RKL2'))
	plt.show()	

if __name__ == '__main__':
	main()
