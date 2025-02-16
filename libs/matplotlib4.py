from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import linspace
from numpy.random import default_rng


rg = default_rng()

x = range(33)
rand1 = rg.integers(-5, 5, 33)
rand2 = rg.integers(-10, 10, 33)
rand3 = rg.integers(-2, 2, 33)


rcParams['xtick.bottom'] = False
rcParams['xtick.labelbottom'] = False

fig = plt.figure(figsize=(10, 3.5), dpi=150, layout='tight')
axs = fig.subplots(1, 3, sharey=True)

axs[0].set(
    ylim=(-10, 10),
    yticks=linspace(-10, 10, 11),
)
axs[0].scatter(x, rand1, c='#440000', marker='^', label='-5...5')
# axs[0].legend()

axs[1].scatter(x, rand2, c='#550505', marker='^', label='-10...10')
# axs[1].hlines(linspace(-10, 10, 11), -5, 40, linestyles='dashed')
axs[1].grid(visible=True, axis='y', lw=rcParams['axes.linewidth']/2, ls='--')
# axs[1].legend()

axs[2].scatter(x, rand3, c='#661010', marker='^', label='-2...2')
# axs[2].legend()

fig.legend(loc='lower right')
fig.show()

