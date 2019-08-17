import numpy as np
import cv2
origIm = cv2.imread('SampleImages/Coins/coins5.jpg')
imgray = cv2.cvtColor(origIm,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

cv2.imshow("Threshold", thresh)
cv2.waitKey()

img, contrs, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(origIm, contrs, -1, (0,255,0), 3)
cv2.imshow('Contours', origIm)

cv2.waitKey(0)
cv2.destroyAllWindows()