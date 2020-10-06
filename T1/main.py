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
# for now we'll use 50% as train data and 50% as test data
# luckily our dataset intercalates g and b results, so we can ensure 50/50 data and reduce bias
split_index = int(len(CLEANED_INPUTS)*0.5)
X_TRAIN, X_TEST = CLEANED_INPUTS[:split_index], CLEANED_INPUTS[split_index:]
Y_TRAIN, Y_TEST = CLEANED_OUTPUTS[:split_index], CLEANED_OUTPUTS[split_index:]

# START SETUP FOR THE MODEL

# Set the seed to make result reproducible
np.random.seed(42)

# The prepared input data
X = np.array(X_TRAIN).transpose()

# The outputs for all input data
Y = np.array(Y_TRAIN).transpose()

# Set the hyperparameters
n_x = X.shape[0]    # No. of neurons in first layer (33 inputs)
n_h = 17            # No. of neurons in hidden layer (17 felt right)
n_y = Y.shape[0]    # No. of neurons in output layer (2 outputs)

# The number of times the model has to learn the dataset
number_of_iterations = 10000
learning_rate = 0.01

# define a model
trained_parameters = model(X, Y, n_x, n_h, n_y, number_of_iterations, learning_rate)


# RUN TESTS AND RECORD PERFORMANCE
results = []
for i in range(len(X_TEST)):
    test_row = X_TEST[i]
    x_test = np.array([[n] for n in test_row])
    y_predict = predict(x_test, trained_parameters)
    results += [y_predict]

# TURN RESULT DATA INTO READABLE RESULTS
true_g = 0  # pred G, actual G
false_g = 0  # pred G, actual B
true_b = 0  # pred B, actual B
false_b = 0  # pred B, actual G
not_determined = 0  # output [0, 0] or [1, 1]
actual_g = sum([out[0] for out in Y_TEST])  # number of real gs
actual_b = sum([out[1] for out in Y_TEST])  # number of real bs

for i in range(len(results)):
    if results[i] == Y_TEST[i]:  # true
        if results[i] == [1, 0]:  # g
            true_g += 1
        else:  # b
            true_b += 1
    elif results[i][0] == results[i][1]:  # [0, 0] or [1, 1] => not determined
        not_determined += 1
    else:  # false
        if results[i] == [1, 0]:  # g
            false_g += 1
        else:  # b
            false_b += 1

# DISPLAY RESULTS
print(f"           | pred 'g' \t| pred 'b' \t| total")
print(f"actual 'g' | {true_g} \t\t| {false_b} \t\t| {actual_g}")
print(f"actual 'b' | {false_g} \t\t\t| {true_b} \t\t| {actual_b}")
print(f"not determined: {not_determined}\n")
prec_g = true_g / (true_g + false_g)
reca_g = true_g / actual_g
prec_b = true_b / (true_b + false_b)
reca_b = true_b / actual_b
print(f"Results for 'g' class")
print(f"precision: {str(prec_g)[:6]}\trecall: {str(reca_g)[:6]}")
print(f"Results for 'b' class")
print(f"precision: {str(prec_b)[:6]}\trecall: {str(reca_b)[:6]}")
