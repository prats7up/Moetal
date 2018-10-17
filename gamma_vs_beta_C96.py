import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

beta = np.linspace(0.0, 1.0, 100) #ratio of gas and total (gas+radiation) pressure
gamma = 5./3. #adiabatic index of gas
gamma_1 = beta + (4. - 3.*beta)**2*(gamma-1.)/(beta+12.*(gamma-1.)*(1.-beta))
gamma_3 = 1. + (gamma_1-beta)/(4.-3.*beta)
plt.plot(beta, gamma_1, beta, gamma_3)
plt.legend([r'$\Gamma_1$',r'$\Gamma_3$'],loc='best')
plt.xlabel('gas pressure/total pressure')
plt.show()
