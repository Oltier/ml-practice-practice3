import numpy as np
import pandas as pd
from numpy.core.umath_tests import inner1d

from excercises.T31GettingHandsOnTheData import get_labels
from excercises.T32LogisticRegression import logisticRegression_func, sigmoid_func
from excercises.T34Accuracy import calculate_accuracy


def get_labels_k(N=55, k=0):
    ### STUDENT TASK ###
    ## Generate the label vector which has value 1 for the pictures of the category we are currently looking at (indicated by k)
    ## and 0 for the other two categories.
    ## Hints: See the 2. Dataset-section where the picture order is defined
    # YOUR CODE HERE
    y = get_labels(N, k)
    return y


def multiclass():
    step_size = 1e-5
    num_iter = 3000
    X = np.array(pd.read_csv("feature_map.csv"))
    probabilities = np.zeros((55, 3))
    y_true_matrix = np.empty((55, 3))
    for i in range(0, 3):
        ### STUDENT TASK ###
        # YOUR CODE HERE
        y_true = get_labels_k(k=i)
        e_list, w_opt = logisticRegression_func(X, y_true, step_size, num_iter)
        probability = sigmoid_func(inner1d(w_opt.T, X))
        probabilities[:, i] = probability
        y_true_matrix[:, i] = y_true.reshape((55,))
    y_hat = np.argmax(probabilities, axis=1)
    y = np.argmax(y_true_matrix, axis=1)
    accuracy = calculate_accuracy(y, y_hat)
    return y, y_hat, accuracy


y, y_hat, acc = multiclass()
