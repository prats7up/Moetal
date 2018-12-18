import math

def coeff(n,j):
    return math.factorial(2*n-j)*math.factorial(n)/(math.factorial(j)*math.factorial(n-j)*math.factorial(2*n))