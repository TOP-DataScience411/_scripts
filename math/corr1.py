from matplotlib import pyplot as plt
from numpy import array, average, corrcoef


fig = plt.figure(figsize=(8, 8))
axs = fig.subplots()


X = array([
    [60, 70, 80, 90, 100],
    [ 8, 23, 35, 20,  14]
])

# X_raw = []
# for i in range(X.shape[1]):
#     for _ in range(X[1,i]):
#         X_raw.append(X[0,i])
# X_raw = array(X_raw)

Y = array([
    [25, 30, 35, 40, 45, 50],
    [ 3, 20, 42, 19, 14,  2]
])

# X = array([X[0]*12-5, X[1]])
# Y = array([Y[0]*0.78+9, Y[1]])

XY = array([
    [3,  0,  0,  0,  0],
    [5, 12,  3,  0,  0],
    [0, 11, 28,  3,  0],
    [0,  0,  4, 13,  2],
    [0,  0,  0,  4, 10],
    [0,  0,  0,  0,  2],
])


X_mean = average(X[0], weights=X[1])
Y_mean = average(Y[0], weights=Y[1])

axs.scatter(X_mean, Y_mean, s=250, c='#a00', marker='p')


regr_empiric_Y = []
for i in range(XY.shape[1]):
    regr_empiric_Y.append(sum(XY[:,i] * Y[0]) / X[1,i])
regr_empiric_Y = array(regr_empiric_Y)

axs.plot(X[0], regr_empiric_Y, '^-', c='#222', lw=2.5, ms=12)


X_var = average(X[0]**2, weights=X[1]) - X_mean**2
X_std = X_var**0.5

Y_var = average(Y[0]**2, weights=Y[1]) - Y_mean**2
Y_std = Y_var**0.5

XY_mean = sum(sum(XY[:,i] * Y[0] * X[0,i]) for i in range(X.shape[1])) / sum(X[1])

corr_moment = XY_mean - X_mean*Y_mean
corr_coeff = corr_moment / (X_std*Y_std)


slope = corr_coeff * Y_std / X_std
shift = Y_mean - slope*X_mean

axs.axline((X_mean, Y_mean), slope=slope, lw=2.5, c='#2a0')


XY_raw = array([
    (X[0,i], Y[0,j])
    for i in range(X.shape[1])
    for j in range(Y.shape[1])
    for _ in range(XY[j,i])
]).T

axs.scatter(*XY_raw, s=25, c='#ddd')

# >>> corrcoef(XY_raw).round(2)
# array([[1.  , 0.88],
#        [0.88, 1.  ]])


fig.show()

