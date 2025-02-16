from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import array

from pathlib import Path
from sys import path


data = array([1, 2, 5, 12, 25, 27, 31, 30, 28, 22, 19, 9, 6, 3, 1])
x = range(len(data))

rcParams['axes.facecolor'] = '#85b2b0'
rcParams['xtick.bottom'] = False
rcParams['xtick.labelbottom'] = False

fig = plt.figure(figsize=(7, 7.5), dpi=150, layout='tight')
axs = fig.subplots(1, 2, sharey=True)

axs[0].set(title='Демонстрационная\nстолбчатая диаграмма')
axs[0].bar(x, data)

axs[1].set(title='Уменьшенная\nстолбчатая диаграмма')
axs[1].bar(x, data / 2)

fig.show()

