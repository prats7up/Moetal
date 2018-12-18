import numpy as np
import matplotlib.pyplot as plt

Amat = np.array([[0,1],[1, 0]])
ql = np.array([1,0]); qr = np.array([0,0])


lam, R = np.linalg.eig(Amat)

idx = lam.argsort()[::] #[::-1] for descending order
lam = lam[idx]
R = R[:,idx]

alpha = np.linalg.inv(R).dot(qr-ql)

qm = ql + alpha[0]*R[:,0]

plt.plot(ql[0],ql[1],'o',qr[0],qr[1],'o',qm[0],qm[1],'+')
#plt.axis([-1,2,0,2])
plt.show()