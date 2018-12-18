#code to solve one-zone model for relativistic electron PDF

import numpy as np
import matplotlib.pyplot as plt
plt.rc('lines', linewidth=3, color='r')
plt.rcParams.update({'font.size': 18})

def tc_s(gm):
    return 1./gm

def tc_i(gm):
    return 1.e60/gm    

def tc_a():
    return 1.e60

def gamma_dot(gm): #note that gb_dot is negative
    return -gm*(1./tc_s(gm)+1./tc_i(gm)+1./tc_a())

num_g = 40
g = np.logspace(0, 8, num_g)
ng = np.zeros(num_g); ngp = np.zeros(num_g) #initialize ng
s = 2.2
ng = 0.*g**-s
Sg = g**-s

time = 0.0
while (time < 1.e-6):
    dt = 1.e50
    for i in range(num_g-1):
        dt = min(dt, (g[i+1]-g[i])/np.abs(gamma_dot(g[i])) )
    dt = 0.2*dt
    for i in range(num_g):
        if (i==0):
            ngp[i] = ng[i] + Sg[i]*dt - dt*( gamma_dot(g[i+1])*ng[i+1]-gamma_dot(g[i])*ng[i] )/(g[i+1]-g[i])
        elif (i==num_g-1):
            ngp[i] = ng[i] + Sg[i]*dt - dt*( 0.0 - gamma_dot(g[i])*ng[i] )/(g[i]-g[i-1])
        else:
            ngp[i] = ng[i] + Sg[i]*dt - dt*( gamma_dot(g[i+1])*ng[i+1]-gamma_dot(g[i])*ng[i] )/(0.5*(g[i+1]-g[i-1]))
    time = time + dt
    ng = ngp