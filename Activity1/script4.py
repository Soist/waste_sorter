import cv2
import numpy

image = cv2.imread("SampleImages/antiqueTractors.jpg")
(bc, gc, rc) = cv2.split(image)
# each channel is shown as grayscale, because it only has value per pixel
cv2.imshow("Blue channel", bc)
cv2.imshow("Green channel", gc)
cv2.imshow("Red channel", rc)
cv2.moveWindow("Blue channel", 30, 30)
cv2.moveWindow("Green channel", 330, 60)
cv2.moveWindow("Red channel", 630, 90)
cv2.waitKey(0)
# Put image back together again
imCopy = cv2.merge((bc, gc, rc))
cv2.imshow("Image Copy", imCopy)
cv2.waitKey(0)