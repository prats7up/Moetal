import numpy as np
import matplotlib.pyplot as plt

s=5; nx=ny=50

fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
	for i in range(nx):
		X[i][j] = Data[i+j*ny][0]
		Y[i][j] = Data[i+j*ny][1]
		T[i][j] = Data[i+j*ny][2]
f, axarr = plt.subplots(3, 3, sharex=True, sharey=True)
plt.subplot(331)
plt.title('s=5')
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
plt.ylabel('N=50')
frame1=plt.gca()
frame1.axes.get_xaxis().set_ticklabels([])
#im = axarr[0,0].contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
#plt.colorbar()
#plt.show()

s=20; nx=ny=50
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(332)
plt.title('s=20')
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
frame1=plt.gca()
frame1.axes.get_xaxis().set_ticklabels([])
frame1.axes.get_yaxis().set_ticklabels([])
#im = axarr[0,1].contourf(X,Y,T,30,vmin=9.9,vmax=10.2)

s=50; nx=ny=50
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(333)
plt.title('s=50')
im1 = plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
frame=plt.gca()
frame.axes.get_xaxis().set_ticklabels([])
frame.axes.get_yaxis().set_ticklabels([])
#im1 = axarr[0,2].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

s=5; nx=ny=100
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(334)
plt.ylabel('N=100')
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
#plt.yabel('N=100')
frame1=plt.gca()
frame1.axes.get_xaxis().set_ticklabels([])
#frame1.axes.get_yaxis().set_ticklabels([])
#im = axarr[1,0].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

s=20; nx=ny=100
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(335)
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
frame1=plt.gca()
frame1.axes.get_xaxis().set_ticklabels([])
frame1.axes.get_yaxis().set_ticklabels([])
#im = axarr[1,1].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

s=50; nx=ny=100
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
#plt.subplot(336)
#plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
#frame1=plt.gca()
#frame1.axes.get_xaxis().set_ticklabels([])
#frame1.axes.get_yaxis().set_ticklabels([])
im = axarr[1,2].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

s=5; nx=ny=200
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(337)
plt.ylabel('N=200')
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
frame1=plt.gca()
#im = axarr[2,0].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

s=20; nx=ny=200
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(338)
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
frame1=plt.gca()
#frame1.axes.get_xaxis().set_ticklabels([])
frame1.axes.get_yaxis().set_ticklabels([])
#im = axarr[2,1].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

s=50; nx=ny=200
fname = open('T_rkl2_'+str(s)+'_'+str(nx)+'_'+str(ny)+'.dat','r')
print fname
Data = np.loadtxt(fname)
fname.close()
X = np.zeros((nx,ny)); Y =  np.zeros((nx,ny)); T = np.zeros((nx,ny))
for j in range(ny):
        for i in range(nx):
                X[i][j] = Data[i+j*ny][0]
                Y[i][j] = Data[i+j*ny][1]
                T[i][j] = Data[i+j*ny][2]
plt.subplot(339)
plt.contourf(X,Y,T,30,vmin=9.9,vmax=10.2)
frame1=plt.gca()
#frame1.axes.get_xaxis().set_ticklabels([])
frame1.axes.get_yaxis().set_ticklabels([])
#im = axarr[2,2].contourf(X,Y,T,30,vmin=9.9, vmax=10.2)

f.subplots_adjust(right=0.88)
cbar_ax = f.add_axes([0.88, -0.1, 0.05, 0.8])
#cbar=plt.colorbar(im, cax=cbar_ax)
#cbar.set_clim(9.9, 10.2)
cbar=f.colorbar(im1, ticks=[9.9, 10, 10.1, 10.2], cax=cbar_ax)
#cbar.set_ticklabels([9.9, 10, 10.1, 10.2])
cbar.ax.set_title('  T')
#f.subplots_adjust(hspace=0,wspace=0)
#plt.axis('equal')
plt.xlim((-1,1))
plt.ylim((-1,1))
plt.suptitle('RKL(2) without limiters')
plt.show()