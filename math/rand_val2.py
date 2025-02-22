from numpy import arange, array


X = array([0, 1, 2, 3, 4])
P = array([.084, .302, .38, .198, .036])

M_X = sum(X * P)

D_X_1 = 0
for k in range(len(X)):
    D_X_1 += (X[k] - M_X)**2 * P[k]
# >>> D_X_1
# np.float64(0.94)

D_X_2 = sum(X**2 * P) - M_X**2
# >>> D_X_2
# np.float64(0.9399999999999995)

std = D_X_1**.5
# >>> std
# np.float64(0.9695359714832658)

