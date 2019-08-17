# This script shows how to crop a part of an image
import cv2
import numpy as np
# Crop first 100 rows and first 200 columns
image = cv2.imread("SampleImages/canyonlands.jpg")
subImg = image[0:100, 0:200]
cv2.imshow("Subimage", subImg)
# Crop two pictures to just the pixel locs they share
im1 = cv2.imread("SampleImages/grandTetons.jpg")
im2 = cv2.imread("SampleImages/mightyMidway.jpg")
(hgt1, wid1, dep1) = im1.shape
(hgt2, wid2, dep2) = im2.shape
newWid = min(wid1, wid2)
newHgt = min(hgt1, hgt2)
im1Crop = im1[0:newHgt, 0:newWid]
im2Crop = im2[0:newHgt, 0:newWid]
cv2.imshow("Im1 Cropped", im1Crop)
cv2.imshow("Im2 Cropped", im2Crop)
cv2.waitKey()
