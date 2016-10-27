import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def g_NFW(rad):
	x = np.divide(rad,r200)
	Menc = M200*( np.log(1.+c200*x) - c200*x/(1.+c200*x) )
	Menc = Menc/( np.log(1.+c200) - c200/(1.+c200) )
	return np.divide(G*Menc,np.multiply(rad,rad))

def phi_NFW(rad):
        x = np.divide(rad,r200)
        pot = -G*M200*np.divide(np.log(1.+c200*x),( (np.log(1.+c200) - c200/(1.+c200))*r200*x ))
        return pot 

def ent_X(rad):
	return K0+K100*(rad/(100*kpc))**alpha

def cooling_fn(TkeV):
	if TkeV>0.02:
		lam = 1.e-22* ( 8.6e-3*TkeV**-1.7 + 0.058*np.sqrt(TkeV) + 0.063)
	if TkeV>=0.0017235 and TkeV<=0.02:
		lam = 6.72e-22*(TkeV/0.02)**0.6
	if TkeV<0.0017235:
		lam = 1.544e-22*(TkeV/0.0017235)**6.
	return lam

#global constants
global r200, M200, c200, G
Msun = 1.9891e33; H0 = 23.9610e-19; G = 6.67e-8;
dcrit = 3.*H0*H0/(8.*np.pi*G)
c200 = 3.3; #M200 = 5.24e14*Msun; r200 = (3.*M200/(4.*np.pi*200.*dcrit))**(1./3.)
M200 = 5.24e13*Msun; r200 = (3.*M200/(4.*np.pi*200.*dcrit))**(1./3.) #group paramaters
kpc = 3.086e21

num = 1000; rout = r200; rin = r200/num
r = np.logspace(np.log10(rin), np.log10(rout), num)
g_acc = g_NFW(r)

#entropy profile
global K0, K100, alpha

K0 = 37.9; K100 = 117.9; alpha = 1.11
keVtoK = 1.1604e7; mu = 0.62; mu_e = 1.17; mu_i = 1./(1./mu-1./mu_e)
mp = 1.67e-24; kB = 1.38e-16

ent_fac = mu*mp*(mu_e*mp)**0.6666667/(kB*keVtoK)

n_out = 1.e-4; p_out = ent_X(rout)*(mu*mp*n_out)**1.666667/ent_fac
p = np.zeros(num); p[num-1] = p_out

for i in range(num-2,-1,-1):
	pg = p[i+1];
	err = 1.e5
	while (err > 1.e-5): #Newton Raphson solver for pressure
		fn = p[i+1] - pg + ent_fac**0.6*( (p[i+1]+pg)/(ent_X(r[i+1])+ent_X(r[i])) )**0.6*( phi_NFW(r[i+1])-phi_NFW(r[i]) )	
		fp = -1.0 + 0.6*ent_fac**0.6*( phi_NFW(r[i+1])-phi_NFW(r[i]) )*(p[i+1]+pg)**-0.4/(ent_X(r[i+1])+ent_X(r[i]))**0.6
		err = -fn/fp
		pg = pg + err
		err = abs(err)/pg
	p[i] = pg
n = ent_fac**0.6*(np.divide(p,ent_X(r)))**0.6/(mu*mp)
ne = n*mu/mu_e; ni = n*mu/mu_i; TkeV = np.multiply( ent_X(r), ne**0.6666667 )
#tcool = 1.5*np.divide(p, ne*ni*cooling_fn(TkeV))
tcool = np.zeros(num)
for i in range(num):
	tcool[i] = 1.5*p[i]/(ne[i]*ni[i]*cooling_fn(TkeV[i]))
tff = np.sqrt( np.divide(2.*r,g_NFW(r)) )

fname = open('profiles.dat','w')
np.savetxt(fname, np.column_stack((r/kpc, ne, TkeV)))
fname.close()

#plt.loglog(r/kpc,g_acc)
#plt.show()
