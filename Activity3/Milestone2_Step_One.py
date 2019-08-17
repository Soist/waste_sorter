'''Identify corners with directions'''

import cv2

imgO = cv2.imread("SampleImages/PuzzlesAndGames/puzzle1.jpg")
img1O = cv2.imread("SampleImages/PuzzlesAndGames/puzzle2.jpg")


img = cv2.resize(imgO, (0,0), fx = 0.5, fy = 0.5)
img1 = cv2.resize(img1O, (0,0), fx = 0.5, fy = 0.5)



blurImg = cv2.GaussianBlur(img, (3, 5), 0)
blurImg1 = cv2.GaussianBlur(img1, (3, 5), 0)
#-------------------------------------------------------------------------------------------------------------------------------------
orb = cv2.ORB_create()

keypts, des = orb.detectAndCompute(blurImg, None)

img_copy = blurImg.copy()
img2 = cv2.drawKeypoints(img_copy, keypts, None, (255, 0, 0), 4)

cv2.imshow("ORB 1", img2)

#-------------------------------------------------------------------------------------------------------------------------------------

img_copy = blurImg1.copy()
img3 = cv2.drawKeypoints(img_copy, keypts, None, (255, 0, 0), 4)

cv2.imshow("ORB 2", img3)

#-------------------------------------------------------------------------------------------------------------------------------------

fast = cv2.FastFeatureDetector_create()

img_copy = blurImg.copy()

keypts = fast.detect(img_copy, None)
img4 = cv2.drawKeypoints(img_copy, keypts, None, (255, 0, 0), 4)

cv2.imshow("FAST 1", img4)

#-------------------------------------------------------------------------------------------------------------------------------------

img_copy = blurImg1.copy()

keypts = fast.detect(img_copy, None)
img5 = cv2.drawKeypoints(img_copy, keypts, None, (255, 0, 0), 4)

cv2.imshow("FAST 2", img5)


cv2.waitKey()
cv2.destroyAllWindows()


