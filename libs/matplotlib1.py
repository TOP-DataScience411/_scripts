from matplotlib import pyplot as plt
from numpy import linspace
from numpy.random import default_rng


rg = default_rng()

x = linspace(0, 10, 21)
y1 = x**2
y2 = x**3
y3 = x**4

rand_field = rg.integers(-10, 10, 21)


fig = plt.figure()
axs = fig.subplots()

axs.set(
    xlim=(0, 10),
    ylim=(0, 1000),
)

axs.plot(x, y1)
axs.plot(x, y2)
axs.plot(x, y3)

fig.show()

