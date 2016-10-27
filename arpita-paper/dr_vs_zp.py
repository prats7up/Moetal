import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

z0 = 100.0
zp = np.linspace(10., 5.*z0, 100)
dr = z0*( 2.*(z0/zp)**2*np.exp(zp/z0) - (1.+2.*z0/zp+2*(z0/zp)**2) )

column = np.exp(-zp/z0)*dr

n0 = 1.e3; eta_10 = 1.0; n=10.*eta_10*n0*np.exp(-zp/z0) #shell density

av_co = 0.1*np.log( 3.3e7*(1.e4**2/(1.7*n)**2 + 1.) )

plt.semilogx( zp/z0, av_co)
#plt.loglog(zp/z0, 0.1*dr/z0, zp/z0, 0.1*column, zp/z0, av_co)
#plt.legend([r'$\eta_{10}\Delta r/z_0$',r'$\eta_{10} n_{\rm sh}\Delta r/(n_0 z_0)$',r'$A_v(CO)$'],loc='best')
#plt.xlabel(r'$z_+/z_0$')
#plt.ylabel(r'$\eta_{10}\Delta r/z_0$')

plt.show()
