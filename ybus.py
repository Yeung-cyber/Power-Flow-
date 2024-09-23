import numpy as np
# Asuming zdata is a module that contains z as a Numpy array
try:
    from zdata import z
    if z.shape[1] < 4:
        print('Array z does not have enough columns.')
        exit()
except ImportError:
    print('Module zdata not found or does not contain z')

R = z[:,2] 
X = z[:,3]
nbr = z.shape[0]
nl = z[:,0].astype(int)
nr = z[:,1].astype(int)
nbus = np.max([np.max(nl),np.max(nr)])
Z = R + 1j*X
y = 1./Z
Y = np.zeros((nbus, nbus), dtype=complex)

for n in range(nbus):
    for k in range(nbr):
        if nl[k] == n+1 or nr[k] == n+1:
            Y[n,n] += y[k]

for k in range(nbr):
    if nl[k] > 0 and nr[k] > 0:
        Y[nl[k]-1,nr[k]-1] = -y[k]
        Y[nr[k]-1,nl[k]-1] = Y[nl[k]-1,nr[k]-1]
print(Y)


