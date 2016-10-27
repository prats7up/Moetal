import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq

D = np.loadtxt("tau_20.dat")
time = D[:,0]
KE = D[:,4]+D[:,5]+D[:,6]
signal = KE - np.mean(KE)

#time   = np.linspace(0,1,50)
#signal = np.cos(5.*2.*np.pi*time)

W = fftfreq(signal.size, d=time[1]-time[0])
f_signal = rfft(signal)

import pylab as plt
#plt.subplot(121)
#plt.plot(time,signal)
#plt.subplot(122)
#plt.plot(f_signal,'o-')
plt.plot(W,0.01*np.square(np.abs(f_signal)),'b-')
plt.xlim(0.1,1.e3)
plt.ylim(1.e-10,1.e2)
#plt.plot(time,KE)

'''
D = np.loadtxt("tau_0.02.dat")
time = D[:,0]
KE = D[:,4]+D[:,5]+D[:,6]
signal = KE - np.mean(KE)

#time   = np.linspace(0,1,50)
#signal = np.cos(5.*2.*np.pi*time)

W = fftfreq(signal.size, d=time[1]-time[0])
f_signal = rfft(signal)
plt.plot(W,np.square(np.abs(f_signal)),'ko-')
plt.xlim(0.1,1.e3)
plt.ylim(1.e-10,1.e2)
'''

D = np.loadtxt("tau_2.dat")
time = D[:,0]
KE = D[:,4]+D[:,5]+D[:,6]
signal = KE - np.mean(KE)

#time   = np.linspace(0,1,50)
#signal = np.cos(5.*2.*np.pi*time)

W = fftfreq(signal.size, d=time[1]-time[0])
f_signal = rfft(signal)
plt.plot(W,0.01*np.square(np.abs(f_signal)),'r-')
plt.xlim(0.1,1.e3)
plt.ylim(1.e-10,1.e2)


plt.plot(W, W**-1.6666)

plt.xscale('log')
plt.yscale('log')
plt.show()
