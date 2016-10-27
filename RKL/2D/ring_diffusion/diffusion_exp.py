import numpy as np
import matplotlib.pyplot as plt

def solvr(Y, tau):
	MY = np.zeros([nx,ny])
	for k in range(nx):
		for l in range(ny):
			km = k-1
			kp = k+1
			if (k==0):
				km = nx-1
			if (k==nx-1):
				kp = 0
			lm = l-1
			lp = l+1
			if (l==0):
				lm = ny-1
			if (l==ny-1):
				lp = 0
			qxp = -D*(T[kp,l]-T[k,l])/dx
			qxm = -D*(T[k,l]-T[km,l])/dx
			qyp = -D*(T[k,lp]-T[k,l])/dy
			qym = -D*(T[k,l]-T[k,lm])/dy 
			MY[k,l] = -tau*( (qxp-qxm)/dx + (qyp-qym)/dy )
	return MY

def init():
        for k in range(nx):
                for l in range(ny):
                        rad = np.sqrt(x[k]*x[k]+y[l]*y[l])
                        ph = np.arctan(y[l]/x[k])
                        if ( rad<0.7 and rad>0.5 and ph<np.pi/12. and ph>-np.pi/12 and x[k]<0.0):
                                T[k,l] = 12.0
                        else:
                                T[k,l] = 10.0

def main():
	plt.clf()
	global dx, dy, x, y, T, nx, ny, D
	nx = 50; ny = 50
	x = np.linspace(-1.0,1.0,nx); y = np.linspace(-1.0,1.0,ny)
	dx = x[1]-x[0]; dy = y[1]-y[0]; xph = x + 0.5*dx; yph = y + 0.5*dy
	D = 1.0; time = 0.0
	X, Y = np.meshgrid(x,y); Xph, Yph = np.meshgrid(xph,yph)
	dt_exp = 0.25*np.minimum(dx*dx,dy*dy)/D
	#number of substages, timing
	dt_rkl = dt_exp; tend = 0.01
	#initialize temperature
	T = np.zeros([nx,ny])
	init()
	T0 = T
	while (time<tend):
		if ( time+dt_rkl <tend):
			time = time+dt_rkl
			dt = dt_rkl
		else:
			dt = tend-time
			time = tend
		print time, dt
		T1 = T + solvr(T, dt)	
		T = T1
	plt.contourf(X, Y, np.transpose(T))
	plt.colorbar()
	plt.show()
	print np.mean(T0), np.mean(T)

if __name__ == '__main__':
	main()
