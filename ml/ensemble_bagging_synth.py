from matplotlib import pyplot as plt
from numpy import (
    array,
    linspace,
    ndarray, 
    sin,
)
from numpy.random import normal
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

from random import sample


def f(x: ndarray):
    """Функция возвращает истинные и смещённые значения."""
    return x * sin(x), x * sin(x) + normal(size=x.shape)


def train_model(model_class, x_sample, y_sample, test_size=1/3, **model_params):
    x_train, x_test, y_train, y_test = train_test_split(
        x_sample, 
        y_sample,
        test_size=test_size
    )
    model = model_class(**model_params)
    model.fit(x_train, y_train)
    return model, x_test, y_test



n = 200
x = linspace(-10, 10, n)
f_true, f_biased = f(x)


# количество моделей в ансамбле
N = 50

predictions_1 = []
for _ in range(N):
    # формирование подвыборки с возвращением (бутстреп)
    data_sample = sample(array([x, f_biased]).T.tolist(), int(n*0.4))
    x_sample, f_sample = array(data_sample).T
    x_sample = x_sample.reshape(-1, 1)
    f_sample = f_sample.reshape(-1, 1)
    # обучение очередной модели на подвыборке
    model, _, _ = train_model(
        DecisionTreeRegressor,
        x_sample,
        f_sample,
        max_depth=5
    )
    # предсказание для исходной выборки
    f_pred = model.predict(x.reshape(-1, 1))
    predictions_1.append(f_pred)

f_pred_mean_1 = array(predictions_1).mean(axis=0)

K = 20
predictions_2 = []
for _ in range(K):
    # формирование подвыборок производится специализированным классом BaggingRegressor
    model, _, _ = train_model(
        BaggingRegressor,
        x.reshape(-1, 1),
        f_biased,
        # экземпляр BaggingRegressor в свою очередь использует модель DecisionTreeRegressor для обучения на каждой подвыборке
        estimator=DecisionTreeRegressor(max_depth=5),
        # количество подвыборок и, соответственно, моделей DecisionTreeRegressor
        n_estimators=N,
        n_jobs=-1
    )
    f_pred = model.predict(x.reshape(-1, 1))
    predictions_2.append(f_pred)

f_pred_mean_2 = array(predictions_2).mean(axis=0)


fig = plt.figure(figsize=(19, 7))
axs = fig.subplots(1, 3)

axs[0].plot(x, f_true, lw=3, c='#000')
axs[0].scatter(x, f_biased, s=10, c='#d2b48c')

axs[1].plot(x, f_true, lw=3, c='#000')
for pred in predictions_1:
    axs[1].plot(x, pred, lw=0.15, c='#da70d6')
axs[1].plot(x, f_pred_mean_1, lw=2, c='#ffa500')

axs[2].plot(x, f_true, lw=3, c='#000')
for pred in predictions_2:
    axs[2].plot(x, pred, lw=0.3, c='#da70d6')
axs[2].plot(x, f_pred_mean_2, lw=2, c='#ffa500')

fig.show()


