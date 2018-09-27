import numpy as np


def sigmoid_func(z):
    ### STUDENT TASK ###
    # sigmoid = ...
    # YOUR CODE HERE
    raise NotImplementedError()
    return sigmoid


def gradient(X, y, w):
    ### STUDENT TASK ###
    # grad = ...
    # YOUR CODE HERE
    raise NotImplementedError()
    return grad


def logisticRegression_func(X, y, step_size, K):
    N = X.shape[0]
    d = X.shape[1]
    # Initialize w as 1xd array.
    w = np.zeros((1, d))
    loss = float('inf')
    loss_list = []
    for i in range(K):
        ### STUDENT TASK ###
        # YOUR CODE HERE
        raise NotImplementedError()
    return loss_list, w


""" Predict Output """


def predict_output(X, w):
    ### STUDENT TASK ###
    # YOUR CODE HERE
    raise NotImplementedError()
    return y


# Execute this cell. Do not modify.
step_size = 1e-5
num_iter = 3000
e_list, w_opt = logisticRegression_func(X, y, step_size, num_iter)
print('The optimal weight vector is:', w_opt)
y_hat = predict_output(X, w_opt)
