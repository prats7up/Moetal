#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:39:10 2018

@author: prateek
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fftpack import fft, ifft, fftshift, rfft

def sqr_signal(x,x1,x2):
    if (x<x2 and x>=x1):
        return 1.0
    else:
        return 0.0

def tri_signal(x,x1,x2,xm):
    if (x<xm and x>=x1):
        return (x-x1)/(xm-x1)
    if (x<x2 and x>=xm):
        return 1. - (x-xm)/(x2-xm)
    if (x<x1 or x>=x2):
        return 0.0


n = 100
x = np.linspace(0,1,n); ys = np.zeros(n); yt = np.zeros(n)

for i in range(n):
    ys[i] = 0*sqr_signal(x[i],0.4,0.6) + 0.5*np.sin(x[i])
    yt[i] = 0*tri_signal(x[i],0.4,0.6,0.5) + 0.5*np.sin(4*np.pi*x[i])
    
#fft_y = fft(y)
fft_ys = np.fft.rfftn(ys)  
fft_yt = np.fft.rfftn(yt)  

kx = 2*math.pi*np.linspace(1,n/2,n/2)

#plt.loglog(kx, 2*abs(fft_ys[1:int(n/2)+1])*abs(fft_ys[1:int(n/2)+1])/n/n,label='square wave')
#plt.loglog(kx, 2*abs(fft_yt[1:int(n/2)+1])*abs(fft_yt[1:int(n/2)+1])/n/n,label='pure wave, non-periodic')
#plt.loglog(kx,.1*kx**-1,label=r'$k^{-1}$')
#plt.loglog(kx,3e3*kx**-4,label=r'$k^{-4}$')
#plt.legend()
#plt.title(r'$|y(k)|^2$ for $0.5 \sin(x)$ for [0,1]')

#plt.ylim([1.e-8,1])
#plt.xlabel(r'$k$')
#plt.ylabel(r'$|y(k)|^2$')
#plt.grid()
#plt.plot(x,ys,label='square')
#plt.plot(x,yt,label='triangle')
plt.plot(x,ys,label='non-periodic sin')
plt.plot(x,yt,label='periodic sin')
#plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()