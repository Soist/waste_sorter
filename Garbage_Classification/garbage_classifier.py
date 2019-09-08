import cv2
import numpy as np
import os
import preprocessor
import descriptor
import knn


def garbage_classifier(training_data_folder,  test_data_folder, k):
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
    training_labels = preprocessor.get_labels(training_data_folder)

    # stage 2: turn images into vectors and matrix that computer can manipulate
    #vectorized_training_data = descriptor.Hu_descriptor(training_data_folder)
    #vectorized_test_data = descriptor.Hu_descriptor(test_data_folder)

    #vectorized_training_data = descriptor.ORB_descriptor(training_data_folder)
    #vectorized_test_data = descriptor.ORB_descriptor(test_data_folder)

    vectorized_training_data = descriptor.Hu_descriptor(training_data_folder)
    vectorized_test_data = descriptor.Hu_descriptor(test_data_folder)

    # stage 3: using knn-algorithm to classify the test images
    knn_obj = knn.KNN(k)

    knn_obj.train(vectorized_training_data, training_labels)

    #predicted_labels = knn_obj.predict_by_Euclidean(vectorized_test_data)
    #predicted_labels = knn_obj.predict_by_Hamming(vectorized_test_data)
    #predicted_labels = knn_obj.predict_by_Manhattan(vectorized_test_data)
    predicted_labels = knn_obj.predict_by_Cosine(vectorized_test_data)

    print("   predict | actual")
    print('------------------------')
    display = np.hstack((predicted_labels, preprocessor.get_labels(test_data_folder)))
    print(display)
    print(display.shape)
    count = 0

    for num in range(0,431):
        if display[num,0] == display[num,1]:
            count = count + 1
    print("Accuracy of prediction:")
    print(count/431)
    print("Random:")
    print(1/6)

    return predicted_labels

garbage_classifier('train', 'test',10)

#number of test

'''pic_card = os.listdir('./split-garbage-dataset/test/cardboard/')
pic_glass = os.listdir('./split-garbage-dataset/test/glass/')
pic_metal = os.listdir('./split-garbage-dataset/test/metal/')
pic_paper = os.listdir('./split-garbage-dataset/test/paper/')
pic_plastic = os.listdir('./split-garbage-dataset/test/plastic/')
pic_trash = os.listdir('./split-garbage-dataset/test/trash/')

total = len(pic_card) + len(pic_glass) + len(pic_metal) + len(pic_paper) + len(pic_plastic) + len(pic_trash)
print('test')
print(total)


pic_card = os.listdir('./split-garbage-dataset/train/cardboard/')
pic_glass = os.listdir('./split-garbage-dataset/train/glass/')
pic_metal = os.listdir('./split-garbage-dataset/train/metal/')
pic_paper = os.listdir('./split-garbage-dataset/train/paper/')
pic_plastic = os.listdir('./split-garbage-dataset/train/plastic/')
pic_trash = os.listdir('./split-garbage-dataset/train/trash/')

total = len(pic_card) + len(pic_glass) + len(pic_metal) + len(pic_paper) + len(pic_plastic) + len(pic_trash)
print('train')
print(total)'''

'''print('predict:')
    print(predicted_labels.shape)
    print('actual')
    print(preprocessor.get_labels(test_data_folder).shape)'''

