import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

sum1 = 0.0
for i in np.arange(100):
	sum1 = sum1 + i**1.2

print sum1
