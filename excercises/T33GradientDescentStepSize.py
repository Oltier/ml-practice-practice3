import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from excercises.T32LogisticRegression import logisticRegression_func


def visualize_error(X, y, step_sizes, best=None, num_iter=2000):
    plt.figure(figsize=(12, 4))
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    for step in step_sizes:
        ### STUDENT TASK ###
        # Plot Error against Step Size
        # loss_list, w_opt =
        # YOUR CODE HERE
        loss_list, w_opt = logisticRegression_func(X, y, step, num_iter)
        n = len(loss_list)  # Size of list remains the same.
        x_axes = np.linspace(0, n, n, endpoint=False)
        axes[0].plot(x_axes, loss_list, label=step)
    axes[0].set_xlabel('Number of Iterations')
    axes[0].set_ylabel('Loss Function')
    axes[0].legend()
    axes[0].set_title(r'$\bf{Figure\ 4.}$Converge of GD')

    for step in step_sizes:
        ### STUDENT TASK ###
        # Plot Error against Step Size.
        # Now mark the best converge in red. Use value from best as a correct step size.
        # loss_list, w_opt =
        # YOUR CODE HERE
        loss_list, w_opt = logisticRegression_func(X, y, step, num_iter)
        n = len(loss_list)  # Size of list remains the same.
        x_axes = np.linspace(0, n, n, endpoint=False)
        if step == best:
            axes[1].plot(x_axes, loss_list, label=step, color="red")
        else:
            axes[1].plot(x_axes, loss_list, label=step, color="blue")

    axes[1].set_xlabel('Number of Iterations')
    axes[1].set_ylabel('Loss Function')
    axes[1].legend()
    axes[1].set_title(r'$\bf{Figure\ 5.}$Converge of GD')
    plt.tight_layout()
    return best, axes


### STUDENT TASK ###
X = np.array(pd.read_csv("feature_map.csv"))
y = np.array(pd.read_csv("labels.csv"))
# Change best=None into step size from the list that provides the fastest converge. e.g best=1
res0_1, axes = visualize_error(X / 255, y, best=16, step_sizes=[0.1, 0.5, 1, 5, 10, 16])
# YOUR CODE HERE
plt.show()
