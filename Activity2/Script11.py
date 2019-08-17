import cv2

img = cv2.imread("SampleImages/chicago.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cannyImg = cv2.Canny(gray,100,200)

cv2.imshow("Canny", cannyImg)

cv2.waitKey()