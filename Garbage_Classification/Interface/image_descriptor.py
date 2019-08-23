import numpy as np


def image_descriptor(descriptor, image_set):
    """
     Use the specified descriptor to generate n-dimensional vectors for m images
    :param descriptor: the descriptor used to describe images
    :param image_set: the preprocessed the image_set to be described
    :return: a m x n matrix representing m images by n-dimensional vectors
    """
    m = len(image_set)
    training_data = np.zeros((m, n))
    # TODO: using a descriptor to turn the image_set into a m x n matrix
    return training_data
