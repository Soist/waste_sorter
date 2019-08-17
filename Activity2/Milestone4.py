import cv2
import numpy as np

img = cv2.imread("SampleImages/Coins/coins1.jpg")

cv2.imshow("Original", img)
cv2.waitKey()

imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img, 50, 270)
cv2.imshow("canny", canny)
cv2.waitKey()

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 20, param1 =50, param2= 30, minRadius= 30, maxRadius= 50)

print(circles)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()