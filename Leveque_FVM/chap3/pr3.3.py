import numpy as np
import matplotlib.pyplot as plt

Amat = np.array([[1,0,2],[0,2,0],[0,0,3]])
ql = np.array([1,1,1]); qr = np.array([3,3,3])

lam, R = np.linalg.eig(Amat)

idx = lam.argsort()[::] #[::-1] for descending order
lam = lam[idx]
R = R[:,idx]

alpha = np.linalg.inv(R).dot(qr-ql)

qm1 = ql + alpha[0]*R[:,0]
qm2 = qm1 + alpha[1]*R[:,1]