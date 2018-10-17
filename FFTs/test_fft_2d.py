import numpy as np
import math
import itertools
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft, fft2

np.random.seed(1001)
xmin = 0.0; xmax = 1.0; nx = 300 #choose to be even
ymin = 0.0; ymax = 1.0; ny = 200
x = np.linspace(xmin,xmax,nx); y = np.linspace(ymin,ymax,ny);
dx = (xmax-xmin)/nx; dy = (ymax-ymin)/ny
f = np.zeros((nx,ny))
nmin_x = 2; nmax_x = 10; nmin_y = 2; nmax_y = 10
kmin_x = nmin_x*2*math.pi/(xmax-xmin); kmax_x = nmax_x*2*math.pi/(xmax-xmin)
kmin_y = nmin_y*2*math.pi/(ymax-ymin); kmax_y = nmax_y*2*math.pi/(ymax-ymin)

for kx, ky in itertools.product(range(nmin_x, nmax_x+1), range(nmin_y, nmax_y+1)):
    k_x = kx*2*math.pi/(xmax-xmin); k_y = ky*2*math.pi/(ymax-ymin)
    A_k = np.abs(1./math.sqrt(k_x*k_x+k_y*k_y))
    phi_k = np.random.uniform(0.0,2.*math.pi)
    for j in range(ny):
        f[:,j] =  f[:,j] + A_k*np.cos(k_x*x+k_y*y[j]+phi_k) 
    k_x = -kx*2*math.pi/(xmax-xmin); k_y = ky*2*math.pi/(ymax-ymin)
    A_k = np.abs(1./math.sqrt(k_x*k_x+k_y*k_y))
    phi_k = np.random.uniform(0.0,2.*math.pi)
    for j in range(ny):
        f[:,j] =  f[:,j] + A_k*np.cos(k_x*x+k_y*y[j]+phi_k)#2-D field; must have both kxky>0 and kxky<0
#plt.figure()
#plt.contourf(f)
#plt.colorbar()
#plt.show()
print ( 'power in real space=', sum(sum(abs(f)*abs(f)))/(nx*ny) )

fft_f = fft2(f)
fft_fs = fftshift(fft_f) #arranges ks in correct order -N/2,..,0,..N/2
plt.figure()
kx = 2*math.pi*np.linspace(-nx/2,nx/2,nx); ky = 2*math.pi*np.linspace(-ny/2,ny/2,ny)
KX, KY = np.meshgrid(kx,ky,indexing='ij')
#plt.contourf(KX, KY, np.log10(np.abs(fft_fs)*np.abs(fft_fs)/(nx*nx*ny*ny)),40)
#plt.colorbar()
#plt.show()
print ( 'power in k-space=', sum(sum(abs(fft_f)*abs(fft_f)))/(nx*ny*nx*ny) )
kabs = np.zeros(nx*ny/2); Energy = np.zeros(nx*ny/2)
#cnt=0
delk = 1.01*0.5*math.pi/max(xmax-xmin,ymax-ymin); kmax = math.pi/min(dx,dy)
nbins = int(math.ceil(kmax/delk))
kbins = np.linspace(0, kmax,  nbins)
cnt = np.zeros(nbins); Ek = np.zeros(nbins)
for l in range(nx):
    for m in range(int(ny/2)):
        kabs[m+l*ny/2] = 2.*math.pi*math.sqrt( (l-nx/2)*(l-nx/2)/(xmax-xmin)**2 +  m*m/(ymax-ymin)**2 )
        Energy[m+l*ny/2] = 2.*np.abs(fft_fs[l,m+ny/2])*np.abs(fft_fs[l,m+ny/2])/(nx*ny*nx*ny) #both half-planes
        for k in range(nbins-1):
            if ( kabs[m+l*ny/2]< kbins[k+1] and kabs[m+l*ny/2]>=kbins[k] ):
                cnt[k] = cnt[k] + 1
                Ek[k] = Ek[k] + Energy[m+l*ny/2]
        #if (Energy[m+l*ny/2]>1.e-5):
         #   cnt=cnt+1
plt.loglog(kabs,Energy,'o',kabs,1.e-1*kabs**-2,kbins,Ek,'-+',kabs,.1*kabs**-1)
plt.grid()
plt.show()
