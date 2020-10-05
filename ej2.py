from ej1 import Perceptron
from random import randrange as random


N_TRAIN = 1000  # number of iterations of learning
LR = 0.1  # learning rate
N_TEST = 100


# curve to imitate using perceptron
def curve(x, y):
    if 2*x + 5 < y:
        return 1
    return 0


if __name__ == '__main__':

    # perceptron to use initialized randomly
    p = Perceptron(random(-2, 2), random(-2, 2), random(-2, 2))

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

    print(f"got {N_OF_WINS/N_TEST*100}% success")