import numpy
from keras import models

from train import F1
from train import Recall

numpy.set_printoptions(precision=4, suppress=True)

if __name__ == '__main__':
    model = models.load_model('caloriesModel.nn', custom_objects={'F1': F1, 'Recall': Recall})
    print(model.predict([0, 25, 35, 105, 307, 405, 1000]))
