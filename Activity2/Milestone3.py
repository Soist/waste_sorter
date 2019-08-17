import cv2
import  numpy

img = cv2.imread("SampleImages/Coins/coins1.jpg")

blurImg = cv2.GaussianBlur(img, (3, 5), 0)

#cv2.imshow("blur", blurImg)
#cv2.waitKey()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,90,255,0)
print(thresh[0,0].dtype)

cv2.imshow("Threshold", thresh)
cv2.waitKey()

img1, contrs, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contrs, -1, (0,255,0), 1)
cv2.imshow('Contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()