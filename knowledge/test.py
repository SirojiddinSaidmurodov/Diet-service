import matplotlib.pyplot as plt
import numpy
import numpy as np
from keras import models

from train import F1
from train import Recall

numpy.set_printoptions(precision=4, suppress=True)

if __name__ == '__main__':
    model = models.load_model('caloriesModel.nn', custom_objects={'F1': F1, 'Recall': Recall})
    print(model.predict([0, 25, 35, 105, 307, 405, 1000]))

    plt.style.use('bmh')

    results = model.predict(np.arange(1000))
    result = results.T

    with plt.style.context('Solarize_Light2'):
        fig, ax = plt.subplots(figsize=(16, 9), dpi=200)
        ax.plot(result[0], label='very low')
        ax.plot(result[1], label='low')
        ax.plot(result[2], label='average')
        ax.plot(result[3], label='high')
        ax.plot(result[4], label='very high')
        plt.title("Fuzzyfication")
        ax.set_xlabel("Calories")
        ax.set_ylabel("Probability")
        ax.legend()

    plt.show()
