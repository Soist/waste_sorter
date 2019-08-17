import cv2
import numpy as np

# for some reason this has become the standard way to import numpy...

img = cv2.imread("SampleImages/snowLeo2.jpg")
cv2.imshow("Original", img)

cv2.waitKey()

(rows, cols, depth) = img.shape

transMatrix = np.float32([[1, 0, 30], [0, 1, 50]])
transImag = cv2.warpAffine(img, transMatrix, (cols, rows))
cv2.imshow("Translated", transImag)

cv2.waitKey(0)
cv2.destroyAllWindows()