import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

D100=np.loadtxt('beta_vs_r_mach_100_csrat_1.dat')
D10=np.loadtxt('beta_vs_r_mach_10_csrat_1.dat')
D2=np.loadtxt('beta_vs_r_mach_2_csrat_1.dat')
D10t1e3=np.loadtxt('beta_vs_r_mach_10.dat')

lines = plt.loglog(D2[:,0],D2[:,1],D10[:,0],D10[:,1],D100[:,0],D100[:,1],D10t1e3[:,0],D10t1e3[:,1])
l1, l2, l3, l4 = lines

plt.setp(l4, linewidth=2, linestyle=':', color='k', label='Mach 10, $T_1/T_3=10^3$')
plt.setp(l3, linewidth=2, linestyle='-.', color='b', label='Mach 100, $T_1/T_3=1$')
plt.setp(l2, linewidth=2, linestyle='--', color='g', label='Mach 10, $T_1/T_3=1$')
plt.setp(l1, linewidth=2, linestyle='-', color='r', label='Mach 2, $T_1/T_3=1$')

plt.axis((1.e-2, 1.e3, 1., 1.e3))

plt.xlabel (r'upstream $\beta$=(gas pressure)/(magnetic pressure)')
plt.ylabel ('(shell density)/(upstream density)')

plt.legend(loc=2)
plt.show()

plt.savefig('/Users/prateek/Dropbox/Moetal/comp_vs_beta1.eps', format='eps', dpi=1000)
