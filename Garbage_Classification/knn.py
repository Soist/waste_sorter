import numpy as np
import cv2



def default_progress_fn(i, total):
    pass

class KNN:
    def __init__ (self, k, progress_fn=default_progress_fn):
        """ Pass k as hyperparameter"""
        self.k = k
        self.progress_fn = progress_fn

    def train(self, X, y):
        """
            X is example training matrix. Every row of X contains one training example. Each training example
            may have `d` features. If there are `m` such examples then X is `m x d` matrix.
            y is the label matrix corrosponding to each training example. Hence y is `m x 1` matrix.
        """

        # During training time stores the references of the input only
        self.tX = X
        self.ty = y

    def predict(self, X):

        """
            Predict y based on test data X.
        """
        # num_training is the row of X, which is the number of training example
        num_training = X.shape[0]

        # For each image, we will predict a label.
        # Therefore, we first create a zero array preparing to store the predicted label.
        YPred = np.zeros(num_training, dtype = self.ty.dtype)

        for i in range(num_training):

            # Euclidean distance is used to find out distance between two datapoint.
                # np.sum( , axis=1) means adding the data horizontally; axis=0 means adding vertically
                # np.reshape means converting a horizontal array into a vertical one (no actual change)
            distances = np.reshape(np.sqrt(np.sum(np.square(self.tX - X[i, :]), axis=1)), (-1, 1))

            # Along with the distance stack the labels so that we can vote easily
                # Stack distances and according labels together
            distance_label = np.hstack((distances, self.ty))

            # Simple majority voting based on the minimum distance
                # argsort() returns a ndArray, which contains indexes of the distances from the smallest distance to the largest one
                # sorted_distance is a ndArray containing the distances listed from the smallest to the largest
            sorted_distance = distance_label[distance_label[:,0].argsort()]

                # k_sorted_distance is a ndArray containing k nearest neighbours (distance + label)
            k_sorted_distance = sorted_distance[:self.k,:]

                # np.unique return the same label only once
                # return_counts = True means counting the number of occurences for each label
            (labels, occurence) = np.unique(k_sorted_distance[:, 1], return_counts=True)

            # label equals to the type of label that occurs most frequently
            label = labels[occurence.argsort()[-1]]
            YPred[i] = label

            self.progress_fn(i, num_training)

        return YPred

if __name__ == "_main_":
    orb = cv2.ORB_create()

