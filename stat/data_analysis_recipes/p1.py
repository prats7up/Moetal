import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

num=10

K = np.zeros(num, dtype=int)
y_mean = np.zeros(num, dtype=float); y_median = np.zeros(num, dtype=float)
y_var = np.zeros(num, dtype=float); y_skew = np.zeros(num, dtype=float)
y_kurt = np.zeros(num, dtype=float); #y_mode = np.zeros(num, dtype=float)

for l in range(num):
    K[l] = 4**(l+1)
    y = np.random.uniform(size=K[l])
    y_mean[l] = np.mean(y); y_median[l] = np.median(y); y_var[l] = np.var(y)
    y_skew[l] = stats.skew(y); y_kurt[l] = stats.kurtosis(y); #y_mode[l] = stats.mode(y)[0]
    
plt.figure()
y_mean_anal = 0.5*np.ones(num); y_var_anal = 1./12.*np.ones(num)
y_skew_anal = np.zeros(num); y_kurt_anal = -1.2*np.ones(num)
plt.plot(1/K, y_mean, '-o', label='mean'); plt.plot(1/K, y_mean_anal)
plt.plot(1/K, y_var,'-+', label='variance'); plt.plot(1/K, y_var_anal)
plt.plot(1/K, y_skew,'-^', label='skewness'); plt.plot(1/K, y_skew_anal)
plt.plot(1/K, y_kurt, '-s', label='kurtosis'); plt.plot(1/K, y_kurt_anal)
plt.xlabel('1/K'); plt.ylabel('statistic')
plt.xscale('log')
plt.legend()
plt.show()

plt.figure()
plt.plot(np.log2(K), y_mean, '-o', label='mean'); plt.plot(np.log2(K), y_mean_anal)
plt.plot(np.log2(K), y_var, '-+', label='variance'); plt.plot(np.log2(K), y_var_anal)
plt.plot(np.log2(K), y_skew, '-^', label='skewness'); plt.plot(np.log2(K), y_skew_anal)
plt.plot(np.log2(K), y_kurt, '-s', label='kurtosis'); plt.plot(np.log2(K), y_kurt_anal)
plt.xlabel(r'$\log_2 K$'); plt.ylabel('statistic')
plt.legend()
plt.show()