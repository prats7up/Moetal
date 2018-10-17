import numpy as np
import math
import matplotlib.pyplot as plt

nb = 100
beta = np.logspace(-3,3,nb)
na = 120
alpha = np.logspace(-3,3,na)

gamma = 5./3.; dlnLdlnT = 0.5

cub = (2.+ np.outer(gamma*np.ones(na),beta))*1j
sqr = (-2*dlnLdlnT - np.outer( (dlnLdlnT-2)*np.ones(na), beta))
lin = -gamma*np.outer(alpha**2,beta)*1j
const = (dlnLdlnT-2.)*np.outer(alpha**2,beta)
#coeff = [cub, sqr, lin, const]
y = np.zeros((3,na,nb),dtype=complex)
for j in range(nb):
    for i in range(na):
        coeff = [ cub[i,j], sqr[i,j], lin[i,j], const[i,j] ]
        y[:,i,j] = np.roots(coeff)
#sigma = np.maximum( np.maximum(np.imag(y[0,:,:]),np.imag(y[1,:,:])), np.imag(y[2,:,:]) )
#sigma = np.minimum( np.minimum(np.imag(y[0,:,:]),np.imag(y[1,:,:])), np.imag(y[2,:,:]) )
omega = np.maximum( np.maximum(np.real(y[0,:,:]),np.real(y[1,:,:])), np.real(y[2,:,:]) )
plt.plot(np.log10(alpha),np.log10(omega[:,nb-1]),label=r'$\beta=1000$')
plt.plot(np.log10(alpha),np.log10(omega[:,0]),label=r'$\beta=0.001$')
#omega = np.minimum( np.minimum(np.real(y[0,:,:]),np.real(y[1,:,:])), np.real(y[2,:,:]) )
#plt.contourf(np.log10(beta),np.log10(alpha),np.log10(sigma),40)
#plt.contourf(np.log10(beta),np.log10(alpha),np.log10(-sigma),40)
#plt.contourf(np.log10(beta),np.log10(alpha),np.log10(-omega),40)
#plt.subplot(326)
#plt.contourf(np.log10(beta),np.log10(alpha),np.log10(-np.real(y[2,:,:])),40)
#plt.contourf(np.log10(beta),np.log10(alpha),np.log10(np.real(y[2,:,:])),40)
#plt.colorbar(label=r'$\log_{10} (-\omega t_{\rm cool})$')
#plt.colorbar(label=r'$\log_{10} (\omega t_{\rm cool})$')
#plt.colorbar()
#plt.xlabel(r'$\log_{10} \beta $')
#plt.ylabel(r'$\log_{10} (k_\parallel v_A t_{\rm cool}) $')
#plt.plot(np.log10(beta),np.log10(sigma[na-1,:]),label=r'$k_\parallel v_A t_{\rm cool}=1000$')
#plt.plot(np.log10(beta),np.log10(sigma[0,:]),label=r'$k_\parallel v_A t_{\rm cool}=0.001$')
#plt.plot(np.log10(beta),np.log10(sigma[na/2,:]),label=r'$k_\parallel v_A t_{\rm cool}=1$')
#plt.plot(np.log10(beta),np.log10(sigma[na/3,:]),label=r'$k_\parallel v_A t_{\rm cool}=0.1$')
#plt.plot(np.log10(beta),np.log10(sigma[2*na/3,:]),label=r'$k_\parallel v_A t_{\rm cool}=10$')
#plt.plot(np.log10(alpha),np.log10(sigma[:,nb-1]),label=r'$\beta=1000$')
#plt.plot(np.log10(alpha),np.log10(sigma[:,0]),label=r'$\beta=0.001$')
#plt.plot(np.log10(alpha),np.log10(sigma[:,nb/2]),label=r'$\beta=1$')
#plt.plot(np.log10(alpha),np.log10(sigma[:,nb/3]),label=r'$\beta=0.1$')
#plt.plot(np.log10(alpha),np.log10(sigma[:,2*nb/3]),label=r'$\beta=10$')
#plt.legend()
#plt.grid()
#plt.xlabel(r'$\log_{10} (k_\parallel v_A t_{\rm cool}) $')
#plt.xlabel(r'$\log_{10} \beta $')
#plt.ylabel(r'$\log_{10} (\sigma t_{\rm cool})$')
#plt.title(r'TI growth rate as a function of $\beta$ for different $k_\parallel v_A t_{\rm cool}$s')
#plt.title(r'TI growth rate as a function of $k_\parallel v_A t_{\rm cool}$ for different $\beta$s')
plt.show()