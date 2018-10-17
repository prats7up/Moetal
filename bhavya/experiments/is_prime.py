import math
import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if (n<2):
        print ("try a number >=2")
        return
    if (n==2):
        return 1
    sqrtn = int(math.ceil(math.sqrt(n)))+1
    print(sqrtn)
    out = 1
    for i in range(2,sqrtn):
        if ( n%i==0 ):
            out = 0
            break
    return out, i