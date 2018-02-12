import numpy as np
import loss_functions as distance
import picture


class NearestNeighbor(object):
    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def train(self, X, y):
        """

        :param X: X is an N x D array where each row i in N is an example. Each example (image) consists of D / 3
        pixels. Each pixel contains an R, G, and B value where each is between 0 and 255.
        :param y: A 1 dimensional array of size N.
        :return: None
        """

        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """

        :param X: X is an N x D array where each row i in N is an example. Each example (image) consists of D / 3
        pixels. Each pixel contains an R, G, and B value where each is between 0 and 255.
        :param y: A 1 dimensional array of size N.
        :return: None
        """
        num_test = len(X)                                           # number of rows (i.e. examples)
        Ypred = [0 * num_test]
        for i in range(num_test):
            # find the nearest training image to the i'th test image
            # Using either Manhattan or Euclidian distance as a metric.
            p1 = picture.Picture(self.X_train[i])
            distances = distance.Manhattan()



