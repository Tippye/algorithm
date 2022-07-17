from collections import Counter
from math import sqrt
import numpy as np
from sklearn.metrics import accuracy_score


class KNNClassifier:
    def __init__(self, k):
        """
        初始化kNN分类器

        :param k:
        """
        assert k >= 1, "k must be valid"
        self.k = k
        self._X_train = None
        self._Y_train = None

    def fit(self, X_train, Y_train):
        """
        根据训练数据集X_train和Y_train训练kNN分类器

        :param X_train: X训练集
        :param Y_train: Y训练集
        :return:
        """
        assert X_train.shape[0] == Y_train.shape[0], "训练集大小必须相同"
        assert self.k <= X_train.shape[0], "k值必须小于训练集大小"
        self._X_train = np.array(X_train)
        self._Y_train = np.array(Y_train)
        return self

    def predict(self, X_predict):
        """
        给定待预测数据集X_predict， 返回表示X_predict的结果向量
        :param X_predict: 待预测数据集
        :return:
        """
        assert self._X_train is not None and self._Y_train is not None, "预测前必须先训练"
        assert X_predict.shape[1] == self._X_train.shape[1], "待预测数据与训练集特征必须相同"
        y_predict = [self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def _predict(self, x):
        """
        对单个数据进行预测
        :param x: 待预测数据
        :return:
        """
        assert x.shape[0] == self._X_train.shape[1], "待预测数据与训练集特征必须相同"
        distances = [sqrt(np.sum((x_train - x) ** 2)) for x_train in self._X_train]
        nearest = np.argsort(distances)
        topK_y = [self._Y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    def score(self, x_test, y_test):
        y_predict = self.predict(x_test)
        return accuracy_score(y_test, y_predict)
