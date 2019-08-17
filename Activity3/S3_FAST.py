import cv2

img = cv2.imread("SampleImages/chicago.jpg")
cv2.imshow("Original 1", img)

# create a FAST object, that can run the FAST algorithm.
fast = cv2.FastFeatureDetector_create()

# detect features
keypts = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)

cv2.imshow("Keypoints 1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()