"""
author: Ariel Suil Aravena [asuil]
date: 05-10-2020

a basic implementation of a Sigmoid Neuron
"""


# class for a Sigmoid Neuron
class SigmoidNeuron:

    # init method
    # weight1 (float), weight2 (float), bias (float) => Perceptron
    def __init__(self, weight1, weight2, bias):
        self.__w1 = weight1
        self.__w2 = weight2
        self.__b = bias

    # evaluation method
    # x1 (int), x2 (int) => int
    def eval(self, x1, x2):
        res = x1 * self.__w1 + x2 * self.__w2 + self.__b
        return 1/(1+2.71**-res)  # sigmoid function

