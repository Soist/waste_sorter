import cv2
import numpy

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

orb = cv2.ORB_create()

img_inv = cv2.imread("SampleImages/PuzzlesAndGames/puzzle3.png")
img = cv2.imread("SampleImages/chicago.jpg")

keypts_ORB, des = orb.detectAndCompute(img_inv, None)
keypts_ORB1, des1 = orb.detectAndCompute(img, None)
print(des)
print(des1)
print(type(des))
print(des.shape)
print(des1.shape)

res = bf.match(des,des1)







