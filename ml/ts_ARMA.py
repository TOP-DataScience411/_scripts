# AR — AutoRegression
# 
# AR(p=1)
# y(t) = const + phi * y(t-1)
# 
# MA — Moving Average
# 
# MA(q=1)
# y(t) = mean + phi * error(t-1)
# 
# ARMA(p, q)
# ARIMA(p, d, q)

from matplotlib import pyplot as plt
from numpy import diff
from pandas import read_csv
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA


from pathlib import Path
from sys import path

from ts_to_stationary import p_flat, to_stationary


script_dir = Path(path[0])
births = read_csv(
    script_dir / 'births.csv',
    index_col='date',
    parse_dates=True
)


fig = plt.figure(figsize=(9, 12))
axs = fig.subplots(2, 1)

plot_acf(to_stationary(p_flat, 12), ax=axs[0])
plot_pacf(to_stationary(p_flat, 12), ax=axs[1])

fig.show()

# p = 1, d = 0, q = 1
model1 = ARIMA(to_stationary(p_flat, 12), order=(1, 0, 1))
model2 = ARIMA(to_stationary(p_flat, 12), order=(2, 0, 2))

model_results1 = model1.fit()
p_predicted1 = model_results1.predict(end=140)

model_results2 = model2.fit()
p_predicted2 = model_results2.predict(end=140)


fig = plt.figure(figsize=(9, 12))
axs = fig.subplots(2, 1)

axs[0].plot(to_stationary(p_flat, 12))
axs[0].plot(p_predicted1)

axs[1].plot(to_stationary(p_flat, 12))
axs[1].plot(p_predicted2)

fig.show()



