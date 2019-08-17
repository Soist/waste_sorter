import cv2
import numpy

img1 = cv2.imread("SampleImages/antiqueTractors.jpg")
cv2.imshow("Win", img1)
cv2.waitKey()

img2 = cv2.imread("SampleImages/beachBahamas.jpg")
cv2.imshow("Win", img2)
cv2.waitKey()

img3 = cv2.imread("SampleImages/canyonlands.jpg")
cv2.imshow("Win", img3)
cv2.waitKey()

img4 = cv2.imread("SampleImages/chicago.jpg")
cv2.imshow("Win", img4)
cv2.waitKey()

cv2.destroyAllWindows()