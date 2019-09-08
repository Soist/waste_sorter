import cv2
import numpy as np
import os
import preprocessor
import descriptor
import knn


def garbage_classifier(training_data_folder,  test_data_folder, k):

    training_labels = preprocessor.get_labels(training_data_folder)

    # HU DESCRIPTOR
    #vectorized_training_data = descriptor.Hu_descriptor(training_data_folder)
    #vectorized_test_data = descriptor.Hu_descriptor(test_data_folder)

    # ORB DESCRIPTOR
    vectorized_training_data = descriptor.ORB_descriptor(training_data_folder)
    vectorized_test_data = descriptor.ORB_descriptor(test_data_folder)

    '''print("training data: ")
    print(vectorized_training_data)
    print("test data: ")
    print(vectorized_test_data)'''

    knn_obj = knn.KNN(k)

    knn_obj.train(vectorized_training_data, training_labels)

    # EUCLIDEAN
    #predicted_labels = knn_obj.predict_by_Euclidean(vectorized_test_data)

    # HAMMING
    #predicted_labels = knn_obj.predict_by_Hamming(vectorized_test_data)

    # MANHATTAN
    predicted_labels = knn_obj.predict_by_Manhattan(vectorized_test_data)

    # COSINE
    #predicted_labels = knn_obj.predict_by_Cosine(vectorized_test_data)

    '''print("   predict | actual")
    print('------------------------')
    display = np.hstack((predicted_labels, preprocessor.get_labels(test_data_folder)))
    print(display)
    print(display.shape)
    count = 0

    for num in range(0,2):
        if display[num,0] == display[num,1]:
            count = count + 1
    print(count)
    print("Accuracy of prediction:")
    print(count/431)
    print("Random:")
    print(1/6)'''

    return predicted_labels




garbage_classifier('pre-train', 'pre-test',10)

