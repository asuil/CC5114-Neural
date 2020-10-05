"""
author: Ariel Suil Aravena [asuil]
date: 05-10-2020

a basic test of a Perceptron
"""


from ej1 import Perceptron
from random import randrange as random
import matplotlib.pyplot as mpl


N_TRAINS = [10*i for i in range(100)]  # number of iterations of learning
LR = 0.1  # learning rate
N_TEST = 100  # number of testing to decide success_rate
RESULTS = []  # container for results


# curve to imitate using perceptron
def curve(x, y):
    if 2*x + 5 < y:
        return 1
    return 0


if __name__ == '__main__':

    w1, w2, b = (random(-2, 2), random(-2, 2), random(-2, 2))  # random starting point

    # run on every N_TRAIN
    for N_TRAIN in N_TRAINS:

        # perceptron to use
        p = Perceptron(w1, w2, b)

        # learning section
        for dummy in range(N_TRAIN):

            # get input data
            test_x = random(-20, 20)
            test_y = random(-20, 20)

            # improve model
            diff = curve(test_x, test_y) - p.eval(test_x, test_y)
            p.update_weight_x(LR * test_x * diff)
            p.update_weight_y(LR * test_y * diff)
            p.update_bias(LR * diff)

        # test of results
        N_OF_WINS = 0
        for dummy in range(N_TEST):

            # get input data
            test_x = random(-20, 20)
            test_y = random(-20, 20)

            # record successful tests
            N_OF_WINS += (curve(test_x, test_y) == p.eval(test_x, test_y))

        # success_rate for this perceptron
        success_rate = N_OF_WINS / N_TEST

        # save success_rate for this N_TRAIN
        RESULTS += [success_rate]

    # plot results
    mpl.plot(N_TRAINS, RESULTS)
    mpl.show()