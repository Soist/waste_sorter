import cv2
img = cv2.imread("SampleImages/wildColumbine.jpg")
cv2.imshow("Original", img)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res, img3 = cv2.threshold(img2, 100,255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Thresholded", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
