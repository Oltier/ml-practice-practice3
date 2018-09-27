import re
from os import listdir
from os.path import isfile, join

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def get_source_image_file_names(base_dir=""):
    return [join(base_dir, f) for f in listdir(base_dir) if isfile(join(base_dir, f)) and re.match('image_[0-9]+\.jpg', f)]


def convert_image_to_average_rgb(path):
    im = Image.open(path)
    width, height = im.size
    pixel_no = width * height
    rgb_im = im.convert('RGB')
    data = np.asarray(rgb_im).reshape((pixel_no, 3))
    rgb_sum = data.sum(axis=0)
    rgb_average = rgb_sum / pixel_no
    reshaped_rgb_average = rgb_average.reshape((1,3))
    return reshaped_rgb_average


def get_feature_matrix(N=55):
    # initialize the feature vector with zeros.

    ### STUDENT TASK ###
    ## Loop through each picture and each pixel and sum the RGB values into the feature vector matrix.
    ## At last, remember to divide each R, G and B sum with the total pixel count to get the average value.
    ## Hint: Most of the commands required for this task are in the 2.Dataset-section.
    # YOUR CODE HERE
    image_sources = np.array(get_source_image_file_names("images"))
    x_vec = np.array(list(map(lambda img: convert_image_to_average_rgb(img), image_sources))).reshape((N, 3))

    return x_vec


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


X = get_feature_matrix()
y = get_labels()

# Full Vector
# Let s label : Grass = 1 , Soil = 0, Tiles = 0
assert X.shape == (55, 3)
axes = Visualize_data(X, y)
