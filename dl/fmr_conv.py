from keras.activations import (
    relu,
    sigmoid,
    softmax,
)
from keras.layers import (
    Conv2D,
    Dense, 
    Dropout, 
    Flatten,
    Input,
    MaxPooling2D,
)
from keras.losses import CategoricalCrossentropy
from keras.metrics import CategoricalAccuracy
from keras.models import Sequential
from keras.optimizers import Adam

from numpy import load
from sklearn.model_selection import train_test_split

from functools import partial
from pathlib import Path
from sys import path


x_train, x_test, y_train, y_test = train_test_split(
    *load(Path(path[0]) / 'fmr.npz', allow_pickle=True).values(),
    test_size=0.2,
    random_state=1,
)


model = Sequential([
    Input(
        shape=(x_train.shape[1:]),
    ),
    Conv2D(
        filters=10, 
        kernel_size=(2, 2), 
        activation=relu,
        name='low_lvl_features',
    ),
    MaxPooling2D(),
    Conv2D(
        filters=20, 
        kernel_size=(2, 2), 
        activation=relu,
        name='mid_lvl_features',
    ),
    MaxPooling2D(),
    Conv2D(
        filters=50, 
        kernel_size=(3, 3), 
        activation=relu,
        name='high_lvl_features',
    ),
    MaxPooling2D(
        pool_size=(4, 4),
    ),
    Flatten(),
    Dropout(
        rate=1/3,
    ),
    Dense(
        units=50,
        activation=relu,
        name='hidden',
    ),
    Dropout(
        rate=0.5,
    ),
    Dense(
        units=3,
        activation=softmax,
        name='output',
    ),
], name='Ferrari_Mercedes_Renault_reckognition')
model.summary()

model.compile(
    loss=CategoricalCrossentropy(),
    optimizer=Adam(learning_rate=0.01),
    metrics=[
        CategoricalAccuracy(name='acc'),
    ]
)
print('\nОБУЧЕНИЕ\n')
epochs = 25
training_results = model.fit(
    x_train,
    y_train,
    batch_size=64,
    epochs=epochs,
    validation_split=0.2,
    verbose=1
)
print('\nТЕСТИРОВАНИЕ\n')
scores = model.evaluate(
    x_test,
    y_test,
    return_dict=True,
    verbose=1
)
print(
    f'\nloss = {scores["loss"]:.3f}',
    f'\naccuracy = {scores["acc"]:.1%}\n',
)


fig = plt.figure(figsize=(11, 5))
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
    s=30, 
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
    s=30, 
    c='#c80608', 
    label='test_accuracy'
)
axs[1].set_xticks(range(1, epochs+2))
axs[1].legend()

fig.show()

