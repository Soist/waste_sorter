import cv2
import numpy

img = cv2.imread("SampleImages/mightyMidway.jpg")

img1 = cv2.resize(img, (100, 100))

cv2.imshow("100 X 100", img1)
cv2.waitKey()

img2 = cv2.resize(img, (0,0), fx=2, fy=2)

cv2.imshow("Stretch", img2)
cv2.waitKey()

img3 = cv2.resize(img, (0,0), fx=0.5, fy= 1.0)

cv2.imshow("Squash", img3)
cv2.waitKey()

