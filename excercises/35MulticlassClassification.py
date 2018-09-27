import numpy as np


def get_labels_k(N=55,k=0):
    y = np.zeros((N,1));
    ### STUDENT TASK ###
    ## Generate the label vector which has value 1 for the pictures of the category we are currently looking at (indicated by k)
    ## and 0 for the other two categories.
    ## Hints: See the 2. Dataset-section where the picture order is defined
    # YOUR CODE HERE
    raise NotImplementedError()
    return y


def multiclass():
    y_predict = []
    step_size = 1e-5
    num_iter = 3000
    for i in range(0,3):
        ### STUDENT TASK ###
        # YOUR CODE HERE
        raise NotImplementedError()
    return y, y_hat, accuracy


y, y_hat,acc = multiclass()