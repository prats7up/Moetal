import numpy as np
from scipy import special
import matplotlib.pyplot as plt

n=1000000
xmean=0.0; ymean=0.0; d1=0; d2=0
for i in range(n):
    x = np.random.uniform()
    y = np.random.uniform()
    d1 = d1 + abs(x-y)
    d2 = d2 + (x-y)*(x-y)
d1 = d1/n
d2=d2/n