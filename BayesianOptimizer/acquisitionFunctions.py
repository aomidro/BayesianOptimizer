#  coding=utf-8
"""
"""

import numpy as np


class AcquisitionFunction(object):
    """
    alternate function class
    """

    def __init__(self):
        pass

    def get_value(self, mean, variance):
        """
        return function value
        """
        pass

    def update_state(self, mean, variance):
        """
        update parameters based on measurement
        :return: None
        """
        pass


class UpperConfidenceBound(AcquisitionFunction):
    """
    upper confidence bound
    """

    def __init__(self, beta=10):
        super(UpperConfidenceBound, self).__init__()
        self.beta = beta
        ''' beta '''

    def get_value(self, mean, variance):
        """

        :param mean:
        :param variance:
        :return:
        """
        return mean + np.sqrt(self.beta * variance)


class MutualInformation(AcquisitionFunction):
    """
    mutual information
    """

    def __init__(self, delta=np.power(10.0, -300.0)):
        """
        constructor
        """
        super(MutualInformation, self).__init__()

        self.gamma = 0.0
        ''' gamma '''

        self.delta = delta
        ''' delta '''

    def get_value(self, mean, variance):
        """
        get value
        :param mean:
        :param variance:
        :return: value
        """
        alpha = np.log(2.0 / self.delta)
        value = mean + np.sqrt(alpha) * variance / (np.sqrt(variance + self.gamma) + np.sqrt(self.gamma))

        return value

    def update_state(self, mean=None, variance=None):
        """
        update gamma
        :param mean: mean at optimal point
        :param variance: variance at optimal point
        :return: None
        """
        self.gamma += variance
