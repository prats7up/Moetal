import numpy as np
import matplotlib.pyplot as plt
import time

def lim(x1,x2):
        if ( x1*x2>0):
                lab = 2.*x1*x2/(x1+x2)
        else:
                lab = 0.0
        #lab = 0.5*(x1+x2)
        return lab

def solvr(Y, tau):
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
			lp = l+1
			if (k==nx-1):
                                kp = 0
			if (l==ny-1):
                                lp = 0
			MY[k,l] = -tau*( (qx[kp,l]-qx[k,l])/dx + (qy[k,lp]-qy[k,l])/dy )
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


plt.clf()
global dx, dy, x, y, T, nx, ny, D, bxf, byf
nx = 200 ; ny = 200
x = np.linspace(-1.0,1.0,nx); y = np.linspace(-1.0,1.0,ny)
dx = x[1]-x[0]; dy = y[1]-y[0]; xmh = x - 0.5*dx; ymh = y - 0.5*dy
D = 1.0; tcode = 0.0
X, Y = np.meshgrid(x,y,indexing='ij'); Xmh, Ymh = np.meshgrid(xmh,ymh,indexing='ij')
rad = np.sqrt(Xmh*Xmh+Y*Y); bxf = Y/rad #face-centered bx
rad = np.sqrt(X*X+Ymh*Ymh); byf = -X/rad #face-centered by
rad = np.sqrt(X*X+Y*Y); bxc = Y/rad; byc = -X/rad #cell-centered b
#bxf = np.ones([nx,ny])/np.sqrt(2.); byf = -np.ones([nx,ny])/np.sqrt(2.); bxc=bxf; byc=byf
dt_exp = 0.25*np.minimum(dx*dx,dy*dy)/D
#number of substages, timing
dt_rkl = dt_exp; tend = 1.0
#initialize temperature
T = np.zeros([nx,ny])
init()
#plt.contourf(X, Y, T)
T0 = T
beg_time = time.time()
while (tcode<tend):
	if ( tcode+dt_rkl <tend):
		tcode = tcode+dt_rkl
		dt = dt_rkl
	else:
		dt = tend-tcode
		tcode = tend
	print tcode, dt
	T1 = T + solvr(T, dt)	
	T = T1
	#break
end_time = time.time()
print 'Wall-time = ', (end_time-beg_time), ' s'
plt.contourf(X, Y, T)
plt.colorbar()
skx = 4; sky = 4
Xp, Yp = X[::skx,::sky], Y[::skx,::sky]
bxp = bxc[::skx,::sky]
byp = byc[::skx,::sky]
plt.quiver(Xp, Yp, bxp, byp,scale=5.)
plt.show()
print np.mean(T0), np.mean(T)
