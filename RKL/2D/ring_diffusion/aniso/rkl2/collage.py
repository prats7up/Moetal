import os
import pyPLUTO as pp
import numpy as np
import pylab as pl
import matplotlib.colors as colors
import matplotlib as mpl
from matplotlib.ticker import NullFormatter,MultipleLocator, FormatStrFormatter
pc = 3.08567758E18
mu = 0.602
mH = 1.008
amu= 1.6605402E-24
pl.close('all')
fig = pl.figure(figsize=[10,10])
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)


mpl.rc('xtick',labelsize=14)
mpl.rc('ytick',labelsize=14)

from matplotlib import rc, rcParams
rcParams['ps.useafm'] = True
rcParams['pdf.use14corefonts'] = True



def truncate_colormap(cmap, minval, maxval, n):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

cmap=mpl.cm.jet

rho_min = -5.5132890389390967
rho_max = 0.58457492228922914

limit1 =  -427.78/1E2
limit2 =  +427.78/1E2
wdir= "/run/media/ny/PS/multiple-sne-data-04-09-2015/315/"


D = pp.pload(30,w_dir=wdir)
n0=315
L=2.2e+21/pc
x1=np.linspace(-1.0*L,L,n0)
y1=np.linspace(-1.0*L,L,n0)
ax1.set_xlim([limit1,limit2])
ax1.set_ylim([limit1,limit2])
v1 = np.min(np.log10(D.rho[:,:,157]/(mu*mH*amu)))
v2 = np.max(np.log10(D.rho[:,:,157]/(mu*mH*amu)))
frac= np.abs((v2-v1)/(rho_max-rho_min))
frac1 = np.abs(v1-rho_min)/(rho_max - rho_min)
frac2 = np.abs(v2-rho_min)/(rho_max - rho_min)
cmap=mpl.cm.jet
cmap = truncate_colormap(cmap, frac1, frac2, 100*frac)
norm=mpl.colors.Normalize(vmin=v1, vmax=v2)
data = np.log10(np.transpose(D.rho[:,:,157])/(mu*mH*amu))
im=ax1.contourf(x1/1E2,y1/1E2,data,40,cmap=cmap,norm=norm)
ax1.set_ylabel(r'$\rm y [10^2\ pc]$')
sn=np.loadtxt('sn_loc.dat')
ax1.plot(sn[:30,0]/1E2,sn[:30,1]/1E2,'o',color='yellow',markersize=4)
minorLocator   = MultipleLocator(0.2)
ax1.xaxis.set_minor_locator(minorLocator)
minorLocator   = MultipleLocator(0.2)
ax1.yaxis.set_minor_locator(minorLocator)
ax1.xaxis.set_major_formatter(NullFormatter())
ax1.text(100/1E2,320/1E2,r'$\delta L = 4.53\ \rm pc$',fontsize=14,bbox=dict(fc='none',ec="none"))
del D


wdir= "/run/media/ny/PS/multiple-sne-data-04-09-2015/400/"
D = pp.pload(30,w_dir=wdir)
n0=400
L=2.2e+21/pc
x1=np.linspace(-1.0*L,L,n0)
y1=np.linspace(-1.0*L,L,n0)
ax2.set_xlim([limit1,limit2])
ax2.set_ylim([limit1,limit2])
v1 = np.min(np.log10(D.rho[:,:,200]/(mu*mH*amu)))
v2 = np.max(np.log10(D.rho[:,:,200]/(mu*mH*amu)))
frac= np.abs((v2-v1)/(rho_max-rho_min))
frac1 = np.abs(v1-rho_min)/(rho_max - rho_min)
frac2 = np.abs(v2-rho_min)/(rho_max - rho_min)
cmap=mpl.cm.jet
cmap = truncate_colormap(cmap, frac1, frac2, 100*frac)
norm=mpl.colors.Normalize(vmin=v1, vmax=v2)
data = np.log10(np.transpose(D.rho[:,:,200])/(mu*mH*amu))
im=ax2.contourf(x1/1E2,y1/1E2,data,40,cmap=cmap,norm=norm)
sn=np.loadtxt('sn_loc.dat')
ax2.plot(sn[:30,0]/1E2,sn[:30,1]/1E2,'o',color='yellow',markersize=4)
minorLocator   = MultipleLocator(0.2)
ax2.xaxis.set_minor_locator(minorLocator)
minorLocator   = MultipleLocator(0.2)
ax2.yaxis.set_minor_locator(minorLocator)
ax2.xaxis.set_major_formatter(NullFormatter())
ax2.yaxis.set_major_formatter(NullFormatter())
ax2.text(100/1E2,320/1E2,r'$\delta L = 3.57\ \rm pc$',fontsize=14,bbox=dict(fc='none',ec="none"))
del D


wdir= "/run/media/ny/PS/multiple-sne-data-04-09-2015/512/"
D = pp.pload(30,w_dir=wdir)
n0 = 512
L=2.0e+21/pc
x1=np.linspace(-1.0*L,L,n0)
y1=np.linspace(-1.0*L,L,n0)
ax3.set_xlim([limit1,limit2])
ax3.set_ylim([limit1,limit2])
v1 = np.min(np.log10(D.rho[:,:,256]/(mu*mH*amu)))
v2 = np.max(np.log10(D.rho[:,:,256]/(mu*mH*amu)))
frac= np.abs((v2-v1)/(rho_max-rho_min))
frac1 = np.abs(v1-rho_min)/(rho_max - rho_min)
frac2 = np.abs(v2-rho_min)/(rho_max - rho_min)
cmap=mpl.cm.jet
cmap = truncate_colormap(cmap, frac1, frac2, 100*frac)
norm=mpl.colors.Normalize(vmin=v1, vmax=v2)
data = np.log10(np.transpose(D.rho[:,:,256])/(mu*mH*amu))
im=ax3.contourf(x1/1E2,y1/1E2,data,40,cmap=cmap,norm=norm)
ax3.set_xlabel(r'$\rm x [10^2\ pc]$')
ax3.set_ylabel(r'$\rm y [10^2\ pc]$')
sn=np.loadtxt('sn_loc.dat')
ax3.plot(sn[:30,0]/1E2,sn[:30,1]/1E2,'o',color='yellow',markersize=4)
minorLocator   = MultipleLocator(0.2)
ax3.xaxis.set_minor_locator(minorLocator)
minorLocator   = MultipleLocator(0.2)
ax3.yaxis.set_minor_locator(minorLocator)
ax3.text(100/1E2,320/1E2,r'$\delta L = 2.54\ \rm pc$',fontsize=14,bbox=dict(fc='none',ec="none"))


filename = "/run/media/ny/PS/multiple-sne-data-04-09-2015/1024/data.0030.dbl"
n0=1024
f = open(filename, "rb")
L=2.0e+21/pc
x1=np.linspace(-1.0*L,L,n0)
y1=np.linspace(-1.0*L,L,n0)
ax3.set_xlim([limit1,limit2])
ax3.set_ylim([limit1,limit2])
#read the data
import struct as st
dbl = 8
rho = np.zeros((n0,n0))
f.seek(n0*n0*n0*dbl/2)
count = 0
I = 0
J = 0
while count < n0*n0:
   a = f.read(dbl)
   rho[I,J] = st.unpack('d',a)[0]
   J = J+1
   if (count+1)%n0 == 0:
      I = I+1
      J = 0
   count = count+1
f.close()
#----------
ax4.set_xlim([limit1,limit2])
ax4.set_ylim([limit1,limit2])
v1 = np.min(np.log10(rho/(mu*mH*amu)))
v2 = np.max(np.log10(rho/(mu*mH*amu)))
frac= np.abs((v2-v1)/(rho_max-rho_min))
frac1 = np.abs(v1-rho_min)/(rho_max - rho_min)
frac2 = np.abs(v2-rho_min)/(rho_max - rho_min)
cmap=mpl.cm.jet
cmap = truncate_colormap(cmap, frac1, frac2, 100*frac)
norm=mpl.colors.Normalize(vmin=v1, vmax=v2)
data = np.log10(rho/(mu*mH*amu))
im=ax4.contourf(x1/1E2,y1/1E2,data,40,cmap=cmap,norm=norm)
ax4.set_xlabel(r'$\rm x [10^2\ pc]$')
sn=np.loadtxt('sn_loc.dat')
ax4.plot(sn[:30,0]/1E2,sn[:30,1]/1E2,'o',color='yellow',markersize=4)
minorLocator   = MultipleLocator(0.2)
ax4.xaxis.set_minor_locator(minorLocator)
minorLocator   = MultipleLocator(0.2)
ax4.yaxis.set_minor_locator(minorLocator)
ax4.yaxis.set_major_formatter(NullFormatter())
ax4.text(100/1E2,320/1E2,r'$\delta L = 1.27\ \rm pc$',fontsize=14,bbox=dict(fc='none',ec="none"))
#fig_coord = [0.445,0.93,0.32,0.015]
fig_coord = [0.128,0.94,0.56,0.018]
cbar_ax = fig.add_axes(fig_coord)
cbar=pl.colorbar(im,cax=cbar_ax,orientation='horizontal',format='%.1f')
cbar.ax.tick_params(labelsize=14)
cbar.ax.yaxis.set_label_position("right")
cbar.ax.set_ylabel(r'$\log_{10}\ n_{\rm g}\ \rm (cm^{-3})$',rotation=0,labelpad=60)


pl.subplots_adjust(wspace=0,hspace=0)
pl.show()
