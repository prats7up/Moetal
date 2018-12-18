#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:30:00 2018

@author: prateek

solution of gravitational scattering problem
"""

import numpy as np
import matplotlib.pyplot as plt

b = np.logspace(-2,2,100)
rstar = 0.5*(np.sqrt(4.*b*b+1.)-1.)
alpha = 2.*np.arctan(0.5/b)

plt.subplot(111)
'''
plt.plot(b,rstar,'-',label=r'exact solution for $r_*$')
plt.plot(b,alpha,'-',label=r'exact solution for $\alpha$')
plt.plot(b,b,'--',label='y=x')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlabel(r'$b/r_s$')
plt.ylabel(r'$r_*/r_s,\alpha$')
'''
plt.plot(rstar/b,alpha,'-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$r_*/b$')
plt.ylabel(r'$\alpha$')
plt.grid()