import cv2
import numpy as np

img = cv2.imread("SampleImages/snowLeo2.jpg")
cv2.imshow("Original", img)

(rows, cols, depth) = img.shape

origPts = np.float32([[40, 40], [160, 40], [40, 160], [70, 160]])
newPts = np.float32([[10, 80], [180, 5], [35, 193], [60,50]])

mat = cv2.getPerspectiveTransform(origPts, newPts)
warpImg = cv2.warpPerspective(img, mat, (cols, rows))

cv2.imshow("Warped", warpImg)

cv2.waitKey(0)
cv2.destroyAllWindows()



