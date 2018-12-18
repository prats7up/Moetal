import numpy as np
import matplotlib.pyplot as plt
import math

G=6.67e-8; c=4.7; H0=70.*1.e5/(3.086e24); rho_cr0=3.*H0*H0/(8.*math.pi*G)
M200=7.e14*2.e33;
z=0; Om=0.3; Ol=0.7; Ez = np.sqrt(Om*(1.+z)**3+Ol); rho_cr=Ez*Ez*rho_cr0
r200 = (3.*M200/(800.*math.pi*rho_cr0*Ez*Ez))**(1./3.)
x=np.logspace(-3,0,100)
rho_NFW=(200./3.)*(c*c*c/(np.log(1.+c)-c/(1.+c)))*rho_cr/(c*x*(1.+c*x)**2)
phi_NFW=-(G*M200/(np.log(1.+c)-c/(1.+c)))/r200
phi_NFW=phi_NFW*np.log(1.+c*x)/x
rho_enc_rhocr = 200*( -c/(1.+c*x) + np.log(1.+c*x)/x )/(x**2*(np.log(1.+c)-c/(1.+c)))
#plt.loglog(x,rho_NFW/rho_cr0)
#plt.loglog(x,-phi_NFW/(G*M200/r200))
#plt.loglog(x,-phi_NFW)
plt.loglog(x, rho_enc_rhocr)
plt.xlabel('$r/r_{200}$')
#plt.ylabel(r'$-\Phi_{DM}/[GM_{200}/r_{200}]$')
#plt.title('NFW potential (negative) profile for c=1, 4, 10')
plt.show()
plt.grid('on')