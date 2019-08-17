import cv2
import numpy as np

image = cv2.imread("SampleImages/canyonlands.jpg")
print("Value at row 20, column 20:", image[20,20], image[20, 20, :])
print("Row 5:")
print(image[:, 5, :])
print("Column 0:")
print(image[0, :, :])
print("Small section:")
print(image[20:60, 100:200, :])
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()