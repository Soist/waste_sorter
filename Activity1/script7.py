import cv2

catImage = cv2.imread("SampleImages/snowLeo1.jpg")
faceROI = catImage[250:550, 570:860, :]
cv2.imshow("Orig", catImage)
cv2.imshow("Face", faceROI)
cv2.waitKey(0)

# set blue channel of this ROI to zero, notice change shows in original
faceROI[:, :, 1] = 0
cv2.imshow("Orig", catImage)
cv2.imshow("Face", faceROI)
cv2.waitKey(0)

# flip the face upside down by reversing the X direction and keeping the others the same
flipFace = faceROI[::-1, :, :]
cv2.imshow("Flipped", flipFace)
cv2.waitKey(0)