import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def find_nearest_index(array,value):
        idx = (np.abs(array-value)).argmin()
        return idx

boltz = 1.38e-16
#mu = 0.5 #primordial gas
H0 = 70.*1.e5/3.086e24; zred = 0.0; Om=0.31; Hz = H0*np.sqrt( Om*(1+zred)**3 + (1.-Om) )
tdyn = 1./(10.*Hz); numn = 100; numT = 200
n = np.logspace(-8, 4, numn)
T = np.logspace(3, 9, numT)

Ctab = np.loadtxt('mzero.cie'); size_tab = len(Ctab[:,0]); Ttab = np.power(10.*np.ones(size_tab),Ctab[:,0]); Ltab = np.power(10.*np.ones(size_tab),Ctab[:,5])

lambda_cool = np.zeros(numT)

for i in range(numT):
	if T[i]<Ttab[0]:
		lambda_cool[i] = Ltab[0]*(T[i]/Ttab[0])**6.0
	elif T[i]>Ttab[size_tab-1]:
		lambda_cool[i] = Ltab[size_tab-1]*(T[i]/Ttab[size_tab-1])**0.5
	else:
		lambda_cool[i] = Ltab[find_nearest_index(Ttab,T[i])]
	#print lambda_cool[i]

ncrit = 1.5*boltz*10.*Hz*np.divide(T,lambda_cool)/4. #upstream density
ncrit_hub = ncrit*0.1
guniv = 6.67e-8; mp=1.67262171e-24
#ne_crit = 200.*3.*Hz**2/(8.*np.pi*guniv*mp)
ne_crit = 1.686*2.*2.*2.*3.*Hz**2/(8.*np.pi*guniv*mp)
msun=2.e33; M200_12=1.e12*msun; M200_9=1.e9*msun
#Tvir_crit = 0.5*mp*(guniv*M200*Hz)**.666666/(boltz*3.*2.**.33333*200**.333333)
Tvir_crit12 = guniv*M200_12*0.5*mp/(boltz*(3.*M200_12*1.686*2.**3/(800.*np.pi*0.5*mp*200.*ncrit))**0.33333)
Tvir_crit9 = guniv*M200_9*0.5*mp/(boltz*(3.*M200_9*1.686*2.**3/(800.*np.pi*0.5*mp*200.*ncrit))**0.33333)
dcrit = 3.*Hz*Hz/(8.*np.pi*guniv)
Tv_crit = guniv*M200_9*0.5*mp/(boltz*(3.*M200_9*1.686*2.**3/(800.*np.pi*0.5*200.*dcrit))**0.33333)
plt.loglog(ncrit,T,ncrit_hub,T,ne_crit*np.ones(numT),T,ncrit,Tvir_crit12*np.ones(numT),ncrit,Tvir_crit9*np.ones(numT),ncrit,Tv_crit*np.ones(numT))
plt.xlabel('upstream particle number density (cm$^{-3}$)'); plt.ylabel('halo virial temperature (K)')
#plt.axis([-8, -1, 8, 9])
#plt.plot(lTtab,lLtab)
plt.show()
