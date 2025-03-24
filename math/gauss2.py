from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import arange, linspace
from numpy.random import default_rng

from time import sleep


generator = default_rng()

a = 7
sigma = [6, 5, 4, 3, 2, 1, 0.5, 0.1]
N = 150


rcParams['xtick.bottom'] = False
rcParams['xtick.labelbottom'] = False

plt.ion()

fig = plt.figure(figsize=(8, 8))
axs = fig.subplots()

for s in sigma:
    for _ in range(20):
        rv_values = generator.normal(a, s, N)
        x = arange(N)
        
        axs.clear()
        axs.set(
            title=f'σ = {s}',
            ylim=(-11, 25),
            yticks=linspace(-11, 25, 37)
        )
        axs.axline((x[0], a), (x[-1], a), lw=3, c='#000')
        axs.scatter(x, rv_values, s=30, c='#e00')
        plt.draw()
        fig.canvas.flush_events()
        
        sleep(0.001)

plt.ioff()
plt.show()

