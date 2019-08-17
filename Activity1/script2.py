import cv2
img1 = cv2.imread("SampleImages/snowLeo1.jpg")
cv2.imshow("Leopard 1", img1)
cv2.waitKey(1000)
img2 = cv2.imread("SampleImages/snowLeo2.jpg")
cv2.imshow("Leopard 1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()