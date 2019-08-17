import cv2
import numpy as np

img1 = cv2.imread("SampleImages/chicago.jpg")

img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print(img2)

(height, width, depth) = img1.shape

maskG = np.zeros((height,width), np.uint8)

maskG[50:int(height/2), 50:int(width/2)] = 255

cv2.imshow("Original", img2)
cv2.moveWindow("Original", 500, 20)

imgAnd = cv2.bitwise_and(img2, maskG)

cv2.imshow("And", imgAnd)

cv2.waitKey()