import unittest

import numpy as np

import kNN


class MyTestCase(unittest.TestCase):
    def test_something(self):
        knn = kNN.KNNClassifier(3)
        X_train = np.array([
            [3.393533211, 2.331273381],
            [3.110073483, 1.781539638],
            [1.343808831, 3.368360954],
            [3.582294042, 4.679179110],
            [2.280362439, 2.866990263],
            [7.423436942, 4.696522875],
            [5.745051997, 3.533989803],
            [9.172168622, 2.511101045],
            [7.792783481, 3.424088941],
            [7.939820817, 0.791637231]
        ])

        Y_train = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

        x = np.array([[8.09367418, 3.365731514]])

        knn.fit(X_train, Y_train)
        y_pred = knn.predict(x)
        self.assertEqual(y_pred, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()