'''Match two same objects'''

import cv2
import numpy as np

img = cv2.imread("SampleImages/Coins/coins6.jpg")

imgR1 = cv2.resize(img, (0, 0), fx = 0.5,  fy = 0.5)

imgR = imgR1[150:240, 100:200]


orb = cv2.ORB_create()

keypts, des = orb.detectAndCompute(imgR, None)


img1 = cv2.drawKeypoints(imgR, keypts, None, (255, 0, 0), 4)


cv2.imshow("Original",imgR)
vidCap = cv2.VideoCapture(0)

while True:
    ret, img2 = vidCap.read()
    img2_ = img2[:,::-1,:]

    res, img2_inv = cv2.threshold(img2_, 120, 255, cv2.THRESH_BINARY)


    if img2_inv[0,0,0] != 0:
        bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2_inv, None)

        matches = bfMatcher.match(des1, des2)
        matches.sort(key=lambda x: x.distance)

        


        img3 = cv2.drawMatches(img1, kp1, img2_inv, kp2, matches, None)

        cv2.imshow("match", img3)
        x = cv2.waitKey(10)
        userChar = chr(x & 0xFF)
        if userChar == 'q':
            break







