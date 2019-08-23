import image_preprocessor
import image_descriptor
import knn_finder


def waste_sorter(training_data_folder, training_label_folder, test_data_folder, descriptor, k):
    """
    Classify a test_image_set according to a training_data_set
    :param training_data_folder: the folder contains training images
    :param training_label_folder: the folder contains the labels of the training images
    :param test_data_folder: the folder contains test images
    :param descriptor: the descriptor used to describe image
    :param k: the number of labels we find the classify garbage
    :return: a list of predicted labels of the test images according to the training image
    """
    # stage 1: preprocess image
    preprocessed_training_data = image_preprocessor.image_processor(training_data_folder)
    preprocessed_test_data = image_preprocessor.image_processor(test_data_folder)
    training_labels = image_preprocessor.get_labels(training_label_folder)

    # stage 2: turn images into vectors and matrix that computer can manipulate
    vectorized_data = image_descriptor.image_descriptor(descriptor, preprocessed_training_data)

    # stage 3: using knn-algorithm to classify the test images
    knn_obj = knn_finder.KNN(k)
    knn_obj.train(vectorized_data, training_labels)
    predicted_labels = knn_obj.predict(preprocessed_test_data)

    return predicted_labels



