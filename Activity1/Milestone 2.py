import cv2
import numpy
import random

image = cv2.imread("SampleImages/canyonlands.jpg")
(b, g, r) = cv2.split(image)
a = [b, g, r]
random.shuffle([b, g, r])

cv2.imshow("First channel", a[0])
cv2.imshow("Second channel", a[1])
cv2.imshow("Third channel", a[2])

cv2.moveWindow("First channel", 30, 30)
cv2.moveWindow("Second channel", 330, 60)
cv2.moveWindow("Third channel", 630, 90)
cv2.waitKey()


imcopy = cv2.merge((a[0], a[1], a[2]))
cv2.imshow("Image copy", imcopy)
cv2.waitKey()

