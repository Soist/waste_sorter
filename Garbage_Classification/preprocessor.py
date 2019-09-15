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

        for picture_name in pictures:
            if flag is True:
                labels = np.array([[picture_name]])
            else:
                labels = np.append(labels,[[picture_name]], axis=0)

            flag = False




    return labels


print(get_labels("train"))



