import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

ngrid = 100
r = np.linspace(0.1, 5, ngrid)

#initial condition

r0 = 1.0; dev0 = 0.05
Sigma0 = np.exp( -(r-r0)*(r-r0)/(2.*dev0*dev0) )/np.sqrt(2.*np.pi*dev0)
Sigma = Sigma0; Sigma1 = Sigma0

#update Sigma with time at all r
time = 0.0; dt = (r[1]-r[0])*(r[1]-r[0])*0.5; tend = 0.02
while time < tend:
	print min(dt, tend-time)
	dt = min(dt, tend-time)
	time = time + dt

	for i in range(1, ngrid-1):
		rp = (r[i] + r[i+1])*0.5; drp = r[i+1] - r[i]
		rm = (r[i] + r[i-1])*0.5; drm = r[i] - r[i-1]
		dr = 0.5*(r[i+1]-r[i-1])
		Sigma1[i] = Sigma[i] + dt/(r[i]*dr)*( np.sqrt(rp)/drp*( 
		  Sigma[i+1]*np.sqrt(r[i+1]) - Sigma[i]*np.sqrt(r[i]) )
		 - np.sqrt(rm)/drm*( 
                  Sigma[i]*np.sqrt(r[i]) - Sigma[i-1]*np.sqrt(r[i-1]) ) )

	Sigma1[0] = Sigma1[1]; Sigma1[ngrid-1] = Sigma1[ngrid-2]
	Sigma = Sigma1

plt.plot(r, Sigma0, r, Sigma)
 	 
