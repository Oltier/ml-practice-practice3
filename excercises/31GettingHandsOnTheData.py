import matplotlib.pyplot as plt
import numpy as np


def get_feature_matrix(N=55):
    # initialize the feature vector with zeros.
    x_vec = np.zeros((N, 3))

    x = []
    ### STUDENT TASK ###
    ## Loop through each picture and each pixel and sum the RGB values into the feature vector matrix.
    ## At last, remember to divide each R, G and B sum with the total pixel count to get the average value.
    ## Hint: Most of the commands required for this task are in the 2.Dataset-section.
    # YOUR CODE HERE
    raise NotImplementedError()
    return x_vec;


def get_labels(N=55):
    y = np.zeros((N, 1));
    ### STUDENT TASK ###
    ## Generate the label vector, where 1 is a Grass image and 0 is Non-Grass.
    ## Hint: See the 2.Dataset-section where the picture order is defined.
    # YOUR CODE HERE
    raise NotImplementedError()
    return y


# """ VISUALIZE THE DATA """
def Visualize_data(X, y):
    indx_1 = np.where(y == 1)  # for grass.
    indx_2 = np.where(y == 0)  # for non-grass.

    # Set figure size (width, height)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    # PLOT GREENNESS AGAINST REDNESS
    # Make a scatterplot of the average greenness vs redness.
    # Indicate Grass images by a cross, and others by a dot.
    ### STUDENT TASK ###
    # axes[0].scatter(...,..., c='g', marker ='x', label='Grass')
    # axes[0].scatter(...,..., c='r', marker ='o', label='Soil+Tiles')
    # YOUR CODE HERE
    raise NotImplementedError()
    axes[0].set_xlabel('Greenness of Images')
    axes[0].set_ylabel('Redness of Images')
    axes[0].legend()
    axes[0].set_title(r'$\bf{Figure\ 1.}$Green vs Red')

    # PLOT GREENNESS AGAINST BLUENESS
    # The same as above but now greenness vs blueness.
    ### STUDENT TASK ###
    # axes[1].scatter(..., ..., c='g', marker ='x', label='Grass')
    # axes[1].scatter(..., ..., c='b', marker ='o', label='Soil+Tiles')
    # YOUR CODE HERE
    raise NotImplementedError()
    axes[1].set_xlabel('Greenness of Images')
    axes[1].set_ylabel('Blueness of Images')
    axes[1].legend()
    axes[1].set_title(r'$\bf{Figure\ 2.}$Green vs Blue')

    # PLOT REDNESS AGAINST BLUENESS
    # The same as above but now redness vs blueness.
    ### STUDENT TASK ###
    # axes[2].scatter(..., ..., c='r', marker ='x', label='Grass')
    # axes[2].scatter(..., ..., c='b', marker ='o', label='Soil+Tiles')
    # YOUR CODE HERE
    raise NotImplementedError()
    axes[2].set_xlabel('Redness of Images')
    axes[2].set_ylabel('Blueness of Images')
    axes[2].legend()
    axes[2].set_title(r'$\bf{Figure\ 3.}$Red vs Blue')
    plt.tight_layout()
    return axes


y = get_labels()
X = get_feature_matrix()

# Full Vector
# Let s label : Grass = 1 , Soil = 0, Tiles = 0
assert X.shape == (55, 3)
axes = Visualize_data(X, y)
