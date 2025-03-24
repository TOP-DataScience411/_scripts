from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import arange, linspace
from numpy.random import default_rng

from time import sleep


generator = default_rng()

a = 7
sigma = 6
N = [10, 30, 60, 150, 500, 2000]
S = [50, 50, 40, 30, 20, 10]


rcParams['xtick.bottom'] = False
rcParams['xtick.labelbottom'] = False

plt.ion()

fig = plt.figure(figsize=(8, 8))
axs = fig.subplots()

for i in range(len(N)):
    for _ in range(25):
        rv_values = generator.normal(a, sigma, N[i])
        x = arange(N[i])
        
        axs.clear()
        axs.set(
            title=f'n = {N[i]}',
            ylim=(-11, 25),
            yticks=linspace(-11, 25, 37)
        )
        axs.axline((x[0], a), (x[-1], a), lw=3, c='#000')
        axs.scatter(x, rv_values, s=S[i], c='#e00')
        plt.draw()
        plt.gcf().canvas.flush_events()
        
        sleep(0.001)

plt.ioff()
plt.show()

