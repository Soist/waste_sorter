import cv2
import os
import numpy as np

def get_labels(folder_name):
    folder_path = './split-garbage-dataset/' + folder_name + '/'
    sub_folders = os.listdir(folder_path)
    flag = True

    for sub_folder_name in sub_folders:

        sub_folder_path = folder_path + sub_folder_name + '/'
        pictures = os.listdir(sub_folder_path)
        m = len(pictures)

        for num in range(0, m):
            if flag is True:
                labels = np.array([[sub_folder_name]])
            else:
                labels = np.append(labels,[[sub_folder_name]], axis=0)

            flag = False
    return labels

#print(get_labels('test'))




