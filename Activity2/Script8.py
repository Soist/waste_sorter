import cv2
im1 = cv2.imread('SampleImages/canyonlands.jpg')
grayIm1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
newGray = cv2.equalizeHist(grayIm1)
cv2.imshow('Original', grayIm1)
cv2.imshow('Equalized', newGray)
cv2.waitKey(0)
cv2.destroyAllWindows()