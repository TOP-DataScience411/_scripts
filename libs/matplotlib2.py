from matplotlib import pyplot as plt
from numpy import linspace
from numpy.random import default_rng

from pathlib import Path
from sys import path


rg = default_rng()

x = linspace(0, 10, 21)
y1 = 2*x - 1
y2 = -0.5*x + 1
y3 = x

rand_field = rg.integers(-10, 10, 21)


fig = plt.figure(figsize=(9.6, 6), dpi=200)
axs = fig.subplots(1, 2)

axs[0].plot(x, y1)
axs[0].plot(x, y2)
axs[0].plot(x, y3)

axs[1].scatter(x, rand_field)

fig.savefig(Path(path[0]) / 'line_scatter_plots.png')

