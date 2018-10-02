import numpy as np
import pandas as pd

from excercises.T32LogisticRegression import logisticRegression_func, predict_output


def calculate_accuracy(y, y_hat):
    ### STUDENT TASK ###
    # YOUR CODE HERE
    accuracy = np.mean(y == y_hat)
    return accuracy


X = np.array(pd.read_csv("feature_map.csv"))
y = np.array(pd.read_csv("labels.csv"))
step_size = 1e-5
num_iter = 3000

e_list, w_opt = logisticRegression_func(X, y, step_size, num_iter)
y_hat = predict_output(X, w_opt).reshape((len(X), 1))

print('Accuracy of the result is: %f%%' % calculate_accuracy(y, y_hat))
