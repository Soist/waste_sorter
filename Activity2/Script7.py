import cv2
import numpy as np

img = cv2.imread("SampleImages/canyonlands.jpg")
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(height, width, depth) = img.shape

mask = np.zeros((height, width, 1), np.uint8)
mask[50:int(height/2),50:int(width/2)] = 255

maskedImg1 = cv2.bitwise_and(gImg, mask)
cv2.imshow("Original", gImg)
cv2.imshow("Masked", maskedImg1)
cv2.waitKey(0)

colorMask = cv2.merge( (mask, mask, mask) )
maskedImg2 = cv2.bitwise_and(img, colorMask)

cv2.imshow("Original", img)
cv2.imshow("Masked", maskedImg2)

cv2.waitKey(0)
cv2.destroyAllWindows()