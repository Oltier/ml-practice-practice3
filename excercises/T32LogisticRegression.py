import numpy as np
import pandas as pd
from numpy.core.umath_tests import inner1d


def sigmoid_func(z):
    ### STUDENT TASK ###
    # sigmoid = ...
    # YOUR CODE HERE
    sigmoid = 1 / (1 + np.exp(-z))
    return sigmoid


def gradient(X, y, w):
    ### STUDENT TASK ###
    # grad = ...
    # YOUR CODE HERE
    N = len(X)
    f_deriv_w = ((sigmoid_func(inner1d(w.T, X)[:, np.newaxis]) - y) * X).sum(axis=0).reshape((len(w), 1))
    grad = f_deriv_w / N
    return grad


def empirical_risk(X, y, w):
    N = len(X)
    f_1 = (-y) * np.log(sigmoid_func(inner1d(w.T, X)[:, np.newaxis]))
    f_2 = (1 - y) * np.log(1 - sigmoid_func(inner1d(w.T, X)[:, np.newaxis]))
    f = (f_1 - f_2).sum(axis=0)
    empirical_error = f / N
    return empirical_error


def logisticRegression_func(X, y, step_size, K):
    N = X.shape[0]
    d = X.shape[1]
    # Initialize w as 1xd array.
    w = np.zeros((X.shape[1], y.shape[1]))
    loss_list = []
    for i in range(K):
        ### STUDENT TASK ###
        # YOUR CODE HERE
        w = w - step_size * gradient(X, y, w)
        loss_list.append(empirical_risk(X, y, w))
    return loss_list, w


def predict_output(X, w):
    ### STUDENT TASK ###
    # YOUR CODE HERE
    sigmoids = sigmoid_func(inner1d(w.T, X))
    y = np.where(sigmoids >= 0.5, 1, 0)
    return y


X = np.array(pd.read_csv("feature_map.csv"))
y = np.array(pd.read_csv("labels.csv"))

# Execute this cell. Do not modify.
step_size = 1e-5
num_iter = 3000
e_list, w_opt = logisticRegression_func(X, y, step_size, num_iter)
print('The optimal weight vector is:', w_opt)
y_hat = predict_output(X, w_opt)
