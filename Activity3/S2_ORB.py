import cv2

# Some versions of OpenCV need this to fix a bug
# cv2.ocl.setUseOpenCL(False)

img = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")

# create an ORB object, that can run the ORB algorithm.

orb = cv2.ORB_create()    # some versions use cv2.ORB() instead

keypts, des = orb.detectAndCompute(img, None)

img2 = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)

cv2.imshow("Keypoints 1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()