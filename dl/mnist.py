from keras import Sequential
from keras.activations import relu, softmax
from keras.layers import Dense, Input
from keras.losses import CategoricalCrossentropy
from keras.metrics import (
    CategoricalAccuracy,
    CategoricalCrossentropy as CategoricalCrossentropyMetric,
    F1Score
)
from keras.optimizers import Adam

from matplotlib import pyplot as plt
from numpy import array, load as load_npz
from numpy.random import default_rng

from pathlib import Path
from sys import path


def one_hot_encoder(x):
    return (0,) * x + (1,) + (0,) * (9 - x)


def one_hot_decoder(x):
    ...


script_dir = Path(path[0])
data_path = script_dir / 'mnist.npz'

with open(data_path, 'rb') as fileout:
    x_test, x_train, y_train, y_test = load_npz(fileout).values()


# графический вывод подвыборки из тренировочной
# m, n = 10, 16
# randgen = default_rng()
# sample = randgen.choice(x_train, m*n)
# 
# fig = plt.figure(figsize=(17, 11), layout='tight')
# axs = fig.subplots(m, n)
# 
# for i in range(m):
#     for j in range(n):
#         axs[i][j].imshow(sample[i*n+j], cmap='gray', vmin=0, vmax=255)
#         axs[i][j].set_axis_off()
# 
# fig.show()


input_vector_len = x_train.shape[1] * x_train.shape[2]

# изменение размерности
x_train = x_train.reshape((x_train.shape[0], input_vector_len))
x_test = x_test.reshape((x_test.shape[0], input_vector_len))
# масштабирование — приведение к диапазону [0; 1]
x_train = x_train / 255
x_test = x_test / 255
# перекодирование
y_train = array([one_hot_encoder(y) for y in y_train])
y_test = array([one_hot_encoder(y) for y in y_test])

# one-hot encoding
# 0 -> 1 0 0 0 0 0 0 0 0 0
# 1 -> 0 1 0 0 0 0 0 0 0 0
# 2 -> 0 0 1 0 0 0 0 0 0 0
# 3 -> 0 0 0 1 0 0 0 0 0 0
# 4 -> 0 0 0 0 1 0 0 0 0 0
# 5 -> 0 0 0 0 0 1 0 0 0 0
# 6 -> 0 0 0 0 0 0 1 0 0 0
# 7 -> 0 0 0 0 0 0 0 1 0 0
# 8 -> 0 0 0 0 0 0 0 0 1 0
# 9 -> 0 0 0 0 0 0 0 0 0 1


model = Sequential()

model.add(Input(shape=(input_vector_len,), dtype='float64'))
model.add(Dense(400, activation=relu), )
# model.add(Dense(100, activation=relu), )
model.add(Dense(10, activation=softmax, name='output'))

model.summary()
# Model: "sequential"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
# │ dense (Dense)                        │ (None, 400)                 │         314,000 │
# ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
# │ output (Dense)                       │ (None, 10)                  │           4,010 │
# └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
#  Total params: 318,010 (1.21 MB)
#  Trainable params: 318,010 (1.21 MB)
#  Non-trainable params: 0 (0.00 B)

breakpoint()

model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(learning_rate=0.01),
    metrics=[
        CategoricalAccuracy(name='acc'),
        CategoricalCrossentropyMetric(name='cce'),
        # F1Score(name='f1'),
    ]
)

print('\nОБУЧЕНИЕ\n')

epochs = 15
training_results = model.fit(
    x_train,
    y_train,
    epochs=epochs,
    validation_split=0.15,
    verbose=1
)

print('\nТЕСТИРОВАНИЕ\n')

scores = model.evaluate(
    x_test,
    y_test,
    return_dict=True,
    verbose=1
)


fig = plt.figure(figsize=(10, 5))
axs = fig.subplots(1, 2)

axs[0].plot(
    range(1, epochs+1), 
    training_results.history['loss'], 
    label='loss'
)
axs[0].plot(
    range(1, epochs+1), 
    training_results.history['val_loss'],
    label='val_loss'
)
axs[0].scatter(
    epochs+1, 
    scores['loss'], 
    s=15, 
    c='#c80608', 
    label='test_loss'
)
axs[0].set_xticks(range(1, epochs+2))
axs[0].legend()

axs[1].plot(
    range(1, epochs+1), 
    training_results.history['acc'], 
    label='accuracy'
)
axs[1].plot(
    range(1, epochs+1), 
    training_results.history['val_acc'], 
    label='val_accuracy'
)
axs[1].scatter(
    epochs+1, 
    scores['acc'], 
    s=15, 
    c='#c80608', 
    label='test_accuracy'
)
axs[1].set_xticks(range(1, epochs+2))
axs[1].legend()

fig.show()

