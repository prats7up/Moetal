import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 24,'lines.linewidth':3,'lines.markersize':10})

plt.clf()

#DM in pc cm^{-3}; Galactic < 100

DM = np.array([375, 746, 944.38, 723, 1103.6, 553.3, 790, 1628.76, 1629.18, 557, 557, 779, 562.7, 899.6, 952.4, 469.88, 861, 623.3, 776.2])

#width in ms

width = np.array([4.6, 7.8, 5.6, 0.0, 0.0, 0.0, 9.4, 3.0, 0.0, 3.0, 0.0, 0.0, 2.8, 0.0, 0.0, 0.0, 0.0, 1.73, 0.8])

#flux in Jy

flux = np.array([30, 0.4, 1.3, 0.4, 0.5, 0.5, 0.3, 0.35, 0.0, 0.4, 0.0, 1.12, 0.47, 0.0, 0.0, 0.0, 0.0, 0.6, 2.4])

DM_width_UL = np.array([723, 1103.6, 553.3, 1629.18, 779, 899.6, 952.4, 469.88, 861])

width_UL = np.array([1.4, 4.3, 1.1, 0.3, 0.64, 1.9, 0.12, 0.05, 4]) 

#plt.plot( DM, np.multiply(flux,width), 'o')
#plt.plot( DM, flux, 'o')
#plt.plot( flux, width, 'o' )
plt.plot( width,  np.multiply(flux,np.square(DM)), 'o' )

#plt.xlabel('DM')
#plt.ylabel('flux*width')
#plt.xlabel('flux')
#plt.ylabel('width')

plt.yscale('log')
plt.xscale('log')

plt.show() 
