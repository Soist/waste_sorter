import cv2
import numpy as np

origImage = cv2.imread("SampleImages/snowLeo4.jpg")

print("OrigImage's type: " + str(type(origImage))
      + "       shape: " + str(origImage.shape)
      + "       size: " + str(origImage.size)
      + "       dtype: " + str(origImage.dtype))

gray = cv2.cvtColor(origImage, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", gray)

print("GrayImage's type: " + str(type(gray))
      + "       shape: " + str(gray.shape)
      + "       size: " + str(gray.size)
      + "       dtype: " + str(gray.dtype))

blankImg1 = np.zeros((400, 250), np.uint8)
cv2.imshow("Black background image", blankImg1)

print("BlackImage's type: " + str(type(blankImg1))
      + "       shape: " + str(blankImg1.shape)
      + "       size: " + str(blankImg1.size)
      + "       dtype: " + str(blankImg1.dtype))


blankImg2 = 255 * np.ones((300, 300), np.uint8)
cv2.imshow("White background image", blankImg2)

print("WhiteImage's type: " + str(type(blankImg2))
      + "       shape: " + str(blankImg2.shape)
      + "       size: " + str(blankImg2.size)
      + "       dtype: " + str(blankImg2.dtype))


cv2.waitKey(0)
cv2.destroyAllWindows()


