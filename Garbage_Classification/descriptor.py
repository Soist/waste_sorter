import cv2
import numpy as np
import os


def Hu_descriptor(folder_name):


# Use the specified descriptor to generate n-dimensional vectors for m images
#:param descriptor: the descriptor used to describe images
#:param image_set: the preprocessed the image_set to be described
#:return: a m x n matrix representing m images by n-dimensional vectors

    folder_path = './split-garbage-dataset/' + folder_name + '/'
    sub_folders = os.listdir(folder_path)
    count = 0

    for sub_folder_name in sub_folders:


        sub_folder_path = folder_path + sub_folder_name + '/'
        pictures = os.listdir(sub_folder_path)
        m = len(pictures)

        if(count != 0):
            training_data = np.vstack( (training_data, np.zeros( (m, 7) ) ) )
        else:
            training_data = np.zeros((m,7))

        count_copy = count
        for picture_name in pictures:

            picture_path = sub_folder_path + picture_name
            img = cv2.imread(picture_path)

            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            img_canny = cv2.Canny(img_gray,50,270)

            hu = cv2.HuMoments(cv2.moments(img_canny)).flatten()
            training_data[count_copy, :] = hu
            count_copy = count_copy + 1

        count = count + m

        # TODO: using a descriptor to turn the image_set into a m x n matrix
    return training_data

def ORB_descriptor(folder_name):


# Use the specified descriptor to generate n-dimensional vectors for m images
#:param descriptor: the descriptor used to describe images
#:param image_set: the preprocessed the image_set to be described
#:return: a m x n matrix representing m images by n-dimensional vectors
    count = 0

    folder_path = './split-garbage-dataset/' + folder_name + '/'
    sub_folders = os.listdir(folder_path)
    orb = cv2.ORB_create(nfeatures=10)

    all_training_data =  np.empty((0,320),dtype=int)
    for sub_folder_name in sub_folders:

        sub_folder_path = folder_path + sub_folder_name + '/'
        pictures = os.listdir(sub_folder_path)

        for picture_name in pictures:


            picture_path = sub_folder_path + picture_name
            img = cv2.imread(picture_path)

            keypts, des = orb.detectAndCompute(img, None)

            if des is not None:
                if des.shape == (10,32):
                    training_data = des.reshape(1,320)
                    #print(des)
                    all_training_data = np.append(all_training_data, training_data, axis=0)
                else:
                    print(picture_name)
                    count = count + 1
                    #training_data = np.zeros((1,320),dtype=int)
                    #all_training_data = np.append(all_training_data,training_data,axis=0)
            else:
                training_data = np.zeros((1, 320), dtype=int)
                all_training_data = np.append(all_training_data, training_data, axis=0)

    #print(count)
        # TODO: using a descriptor to turn the image_set into a m x n matrix
    return all_training_data

ORB_descriptor("ORBtest")
'''img = cv2.imread("split-garbage-dataset/ORBtest/cardboard/cardboard8.jpg")
print(img)
cv2.imshow("hi",img)
cv2.waitKey()
'''