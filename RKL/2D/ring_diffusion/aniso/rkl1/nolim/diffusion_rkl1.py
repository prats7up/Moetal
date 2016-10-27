import numpy as np
import matplotlib.pyplot as plt
import time

def lim(x1,x2):
	#if ( x1*x2>0):
	#	lab = 2.*x1*x2/(x1+x2)
	#else:
	#	lab = 0.0
	lab = 0.5*(x1+x2)
	return lab

def solvr(Y, tau, nx, ny):
	MY = np.zeros([nx,ny]); qx = np.zeros([nx,ny]); qy = np.zeros([nx,ny])
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
			bya = np.mean([byf[k,l], byf[km,l], byf[k,lp], byf[km,lp]])
			qx[k,l] = -D*bxf[k,l]*( bxf[k,l]*(Y[k,l]-Y[km,l])/dx \
			+ bya*lim( lim(Y[k,lp]-Y[k,l],Y[k,l]-Y[k,lm]), \
			lim(Y[km,lp]-Y[km,l],Y[km,l]-Y[km,lm]) )/dy )
			bxa = np.mean([bxf[k,l], bxf[k,lm], bxf[kp,l], bxf[kp,lm]])	
                        qy[k,l] = -D*byf[k,l]*( byf[k,l]*(Y[k,l]-Y[k,lm])/dy \
                        + bxa*lim( lim(Y[kp,l]-Y[k,l],Y[k,l]-Y[km,l]), \
                        lim(Y[kp,lm]-Y[k,lm],Y[k,lm]-Y[km,lm]) )/dx )
        for k in range(nx):
                for l in range(ny):
                        kp = k+1
                        if (k==nx-1):
                                kp = 0
                        lp = l+1
                        if (l==ny-1):
                                lp = 0
			MY[k,l] = -tau*( (qx[kp,l]-qx[k,l])/dx + (qy[k,lp]-qy[k,l])/dy )
	return MY

def init(nx,ny):
        for k in range(nx):
                for l in range(ny):
                        rad = np.sqrt(x[k]*x[k]+y[l]*y[l])
                        ph = np.arctan(y[l]/x[k])
                        if ( rad<0.7 and rad>0.5 and ph<np.pi/12. and ph>-np.pi/12 and x[k]<0.0):
                                T[k,l] = 12.0
                        else:
                                T[k,l] = 10.0

def main(s,nx,ny):
	plt.clf()
	global dx, dy, x, y, T, D, bxf, byf
	#nx = 200; ny = 200
	x = np.linspace(-1.0,1.0,nx); y = np.linspace(-1.0,1.0,ny)
	dx = x[1]-x[0]; dy = y[1]-y[0] 
	xmh = x - 0.5*dx; ymh = y - 0.5*dy
	D = 1.0; tcode = 0.0
	X, Y = np.meshgrid(x,y,indexing='ij'); Xmh, Ymh = np.meshgrid(xmh,ymh,indexing='ij')
	rad = np.sqrt(Xmh*Xmh+Y*Y); bxf = np.divide(Y,rad) #face-centered bx
	rad = np.sqrt(X*X+Ymh*Ymh); byf = -np.divide(X,rad) #face-centered by
	rad = np.sqrt(X*X+Y*Y); bxc = Y/rad; byc = -X/rad #cell-centered b
	dt_exp = 0.25*np.minimum(dx*dx,dy*dy)/D
	#number of substages, timing
	#s = 100; 
	w1 = 2./(s*s+s); dt_rkl = 0.5*(s*s+s)*dt_exp; 
	tend = 1.0
	#initialize temperature
	T = np.zeros([nx,ny])
	init(nx,ny)
	T0 = T
	'''
	plt.contourf(X, Y, T)
	skx = 8; sky = 4
	Xp, Yp = X[::skx,::sky], Y[::skx,::sky]
	bxp = bxc[::skx,::sky]
	byp = byc[::skx,::sky]
	plt.quiver(Xp, Yp, bxp, byp,scale=10.)
	plt.show()
	exit()
	'''
	beg_time = time.time()
	while (tcode<tend):
		if ( tcode+dt_rkl <tend):
			tcode = tcode+dt_rkl
			dt = dt_rkl
		else:
			dt = tend-tcode
			tcode = tend
		print tcode, dt
		#now start rkl substeps
		Ys = np.zeros([3,nx,ny])
		Ys[0,:,:] = T
		j = 1
		mujt = (2.*j-1.)*w1/j
		Ys[1] = Ys[0] + solvr(Ys[0], mujt*dt,nx,ny)
		for j in range(2,s+1):
			muj = (2.*j-1.)/j
			mujt = (2.*j-1.)*w1/j
			nuj = (1.-j)/j
			Ys[2] = muj*Ys[1] + nuj*Ys[0] + solvr(Ys[1], mujt*dt,nx,ny)
			Ys[0] = Ys[1]
			Ys[1] = Ys[2]
		T = Ys[2]	
	end_time = time.time()
	print 's, tend, Wall-time = ', s, tend, (end_time-beg_time), ' s'
	plt.contourf(X, Y, T)
	plt.colorbar()
	fname = 'T_rkl1_nolim'+str(s)+'_'+str(nx)+'_'+str(ny)+'.pdf'
	plt.savefig(fname, format='pdf')
	fname = open('T_rkl1_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','w')
	for j in range(ny):
		np.savetxt(fname, np.column_stack((X[:,j], Y[:,j], T[:,j], bxc[:,j], byc[:,j])))
	fname.close()
	fname = open('timing_rkl1_nolim.dat','a')
	np.savetxt(fname, np.column_stack((s, nx, ny, end_time-beg_time)), fmt='%d %d %d %e' )
	fname.close()
'''
skx = 4; sky = 4
Xp, Yp = X[::skx,::sky], Y[::skx,::sky]
bxp = bxc[::skx,::sky]
byp = byc[::skx,::sky]
plt.quiver(Xp, Yp, bxp, byp,scale=5.)
plt.show()
print np.mean(T0), np.mean(T), s
'''
