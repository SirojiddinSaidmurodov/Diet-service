import matplotlib.pyplot as plt
import numpy as np
from keras import models, layers, backend as K
from tqdm.keras import TqdmCallback

from knowledge.visualize_nn import visualize_nn

n_features = 1

inputs = layers.Input(name="input", shape=(n_features,))
h1 = layers.Dense(name="h1", units=5, activation='relu')(inputs)

outputs = layers.Dense(name="output", units=5, activation='softmax')(h1)
caloriesModel = models.Model(inputs=inputs, outputs=outputs, name="DeepNN")

visualize_nn(caloriesModel, description=True, figsize=(10, 8))


# define metrics
def Recall(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def Precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def F1(y_true, y_pred):
    precision = Precision(y_true, y_pred)
    recall = Recall(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))


if __name__ == '__main__':

    # compile the neural network
    caloriesModel.compile(optimizer='adam', loss='categorical_crossentropy',
                          metrics=['accuracy', F1])

    X = np.arange(500)
    Y = np.zeros((500, 5))
    Y[:29] = [1, 0, 0, 0, 0]
    Y[30:69] = [0, 1, 0, 0, 0]
    Y[70:199] = [0, 0, 1, 0, 0]
    Y[200:399] = [0, 0, 0, 1, 0]
    Y[400:] = [0, 0, 0, 0, 1]
    # for i in range(1000):
    #     print(i, "  ", Y[i])
    # train/validation
    training = caloriesModel.fit(x=X, y=Y, batch_size=256, epochs=3600, shuffle=True, verbose=0, validation_split=0.1,
                                 callbacks=[TqdmCallback(verbose=0)])

    # plot
    metrics = [k for k in training.history.keys() if ("loss" not in k) and ("val" not in k)]
    fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(15, 3))

    ## training
    ax[0].set(title="Training")
    ax11 = ax[0].twinx()
    ax[0].plot(training.history['loss'], color='black')
    ax[0].set_xlabel('Epochs')
    ax[0].set_ylabel('Loss', color='black')
    for metric in metrics:
        ax11.plot(training.history[metric], label=metric)
        ax11.set_ylabel("Score", color='steelblue')
    ax11.legend()

    ## validation
    ax[1].set(title="Validation")
    ax22 = ax[1].twinx()
    ax[1].plot(training.history['val_loss'], color='black')
    ax[1].set_xlabel('Epochs')
    ax[1].set_ylabel('Loss', color='black')
    for metric in metrics:
        ax22.plot(training.history['val_' + metric], label=metric)
        ax22.set_ylabel("Score", color="steelblue")
    plt.show()

    caloriesModel.save('caloriesModel.nn')
