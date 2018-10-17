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
	nfiles = 32
	#nfiles = 22
	s = 2
	Dc = 1.0
	dt_exp = 0.5*dx*dx/Dc
	fname = "data_rkl2_"+str(s)+".out"
	#fname = "data_"+str(s)+".out"
	Dprev = np.loadtxt(fname)
	Tprev = Dprev[:,1]
	Rerr = Rerr1 = dt_rkl = np.zeros(nfiles+1)
	for s in range(3,nfiles+1):
		fname = "data_rkl2_"+str(s)+".out"
		#fname = "data_"+str(s)+".out"
		D = np.loadtxt(fname)
		x = D[:,0]
		T = D[:,1]
		Rerr[s] = L2_norm(T, Tprev)
		Rerr1[s] = L1_norm(T, Tprev)
		Tprev = T
        	dt_rkl[s] = 0.25*(s*s+s-2.)*dt_exp
		#dt_rkl[s] = 0.5*(s*s+s)*dt_exp
	np.savetxt('err_rkl2.dat', np.column_stack((range(3,nfiles+1),dt_rkl[3:nfiles+1],Rerr[3:nfiles+1])), fmt='%d %e %e')
	#np.savetxt('err.dat', np.column_stack((range(3,nfiles+1),dt_rkl[3:nfiles+1],Rerr[3:nfiles+1])), fmt='%d %e %e')
	#plt.plot(range(3,nfiles+1),Rerr[3:nfiles+1],'-o')
	plt.plot(dt_rkl[3:nfiles+1],Rerr[3:nfiles+1],'-o',dt_rkl[3:nfiles+1],Rerr1[3:nfiles+1],'-^')
	#print Rerr[22]- Rerr1[22]
	plt.yscale('log')
	plt.xscale('log')
	plt.xlabel('super timestep')
	plt.ylabel('Richardson L2 error')
	plt.show()	

if __name__ == '__main__':
	main()
