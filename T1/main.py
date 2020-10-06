"""
author: Ariel Suil Aravena [asuil]
date: 06-10-2020 (last modified on: 06-10-2020)

main script to run the resolution of Tarea 1
    load dataset
    prepare data
    separate train and test data
    train model
    test model
    display results
"""


import csv
import numpy as np
from NeuralNetwork import model, predict


# normalize n(number), m(number), M(number) => number
# normalizes n from range [m, M] to range [0, 1]
def normalize(n, m, M):
    return (n-m)/(M-m)


# LOAD DATA
with open('ionosphere.data', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#   maybe count 'g's and 'b's to match 50/50 outputs and ensure good training without bias

#   separate category to predict from input data
ALL_INPUTS = [row[:-1] for row in data]
ALL_OUTPUTS = [row[-1] for row in data]


# CLEAN THE INPUTS
#   remove second column as it's always 0
CLEANED_INPUTS = [[row[0]] + row[2:] for row in ALL_INPUTS]
#   convert strings to float
CLEANED_INPUTS = [[float(n) for n in row] for row in CLEANED_INPUTS]
#   normalize to range [0, 1] (some have range [-1, 1] and others [0, 1])
#       get max for each column
maxs = CLEANED_INPUTS[0].copy()
for row in CLEANED_INPUTS:
    for i in range(len(row)):
        if row[i] > maxs[i]:
            maxs[i] = row[i]
#       get min for each column
mins = CLEANED_INPUTS[0].copy()
for row in CLEANED_INPUTS:
    for i in range(len(row)):
        if row[i] < mins[i]:
            mins[i] = row[i]
#       normalize
for row in CLEANED_INPUTS:
    for i in range(len(row)):
        row[i] = normalize(row[i], mins[i], maxs[i])


# CLEAN THE OUTPUTS
#   one hot encoding
CLEANED_OUTPUTS = [[1, 0] if value == 'g' else [0, 1] for value in ALL_OUTPUTS]


# SEPARE TRAIN AND TEST DATA
"""
===============
IMPORTANT TO-DO
===============
"""


# START SETUP FOR THE MODEL

# Set the seed to make result reproducible
np.random.seed(42)

# The prepared input data
X = np.array(CLEANED_INPUTS).transpose()

# The outputs for all input data
Y = np.array(CLEANED_OUTPUTS).transpose()

# Set the hyperparameters
n_x = X.shape[0]    # No. of neurons in first layer (33 inputs)
n_h = 17            # No. of neurons in hidden layer (17 felt right)
n_y = Y.shape[0]    # No. of neurons in output layer (2 outputs)

# The number of times the model has to learn the dataset
number_of_iterations = 1000
learning_rate = 0.01

# define a model
trained_parameters = model(X, Y, n_x, n_h, n_y, number_of_iterations, learning_rate)


# RUN TESTS AND RECORD PERFORMANCE
"""
===============
IMPORTANT TO-DO
===============
"""


# DISPLAY PERFORMANCE RESULTS
"""
===============
IMPORTANT TO-DO
===============
"""


# simple temporary starter test
# (run on training data, just to check parameters do work)
test_row = CLEANED_INPUTS[42]
X_test = np.array([[n] for n in test_row])
y_predict = predict(X_test, trained_parameters)

# Print the result
print(f"Expected: {CLEANED_OUTPUTS[42]}\nGot: {y_predict}")