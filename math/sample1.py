from numpy import array
from numpy.random import shuffle


X_sample = array([
    [130, 140, 150, 160, 170, 180, 190],
    [5,   10,  30,  25,  15,  10,  5]
])

X_raw = array([ 
    X_sample[0, i]
    for i in range(X_sample.shape[1])
    for _ in range(X_sample[1, i])
])
shuffle(X_raw)


n = len(X_raw)
gamma = 0.95
t_gamma = 1.9839715

mean_X = X_raw.mean()
mean_X = sum(X_sample[0] * X_sample[1]) / n

std_X = X_raw.std()
std_X = (sum((X_raw - mean_X)**2) / (n-1))**.5
std_X = (sum(X_sample[1] * (X_sample[0] - mean_X)**2) / (n-1))**.5

epsilon = t_gamma * std_X / n**.5

conf_interval = (mean_X-epsilon, mean_X+epsilon)


from matplotlib import pyplot as plt


fig = plt.figure(figsize=(15, 5))
axs = fig.subplots(1, 3)

axs[0].plot(X_sample[0], X_sample[1], '.-', ms=20, lw=3, color='#d00')
axs[1].bar(X_sample[0], X_sample[1], width=9, color='#b00')
# axs[2].hist(X_raw, bins=3, rwidth=.9, color='#b00')

X_hist = array([
    [140,   160,     180],
    [30/20, 47.5/20, 22.5/20]
])
axs[2].bar(*X_hist, width=18, color='#b00')

fig.show()

