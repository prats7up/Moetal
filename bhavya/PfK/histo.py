import numpy as np
from scipy import special
import matplotlib.pyplot as plt

#histogram of children's marks in Bhavya's class
final = np.array([11, 24, 54, 69, 32, 82, 94, 39, 66, 75, \
        62, 46, 57, 77, 8, 33, 45, 58, 68, 62, 69, 55])
#count, bins, ignored = plt.hist(final, (0,10,20,30,40, 50, 60, 70, 80, 90, 100), normed=False)
#plt.hist(final)
cricket_score = np.array([59, 136, 254, 309, 111, 123, 49, 157, 199, 167, 198, 101, 205, 211, 219])
count, bins, ignored = plt.hist(cricket_score, 5, normed=False)
plt.show()