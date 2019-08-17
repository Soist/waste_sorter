import cv2
import numpy as np

vidCap = cv2.VideoCapture(0)

flag = False

while True:
    ret, img = vidCap.read()
    img_inv = img[:,::-1,:]
    cv2.imshow("Original", img_inv)

    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        break

    if userChar == 't':
        img2 = cv2.cvtColor(img_inv, cv2.COLOR_BGR2GRAY)
        res, img3 = cv2.threshold(img2, 60, 255, cv2.THRESH_BINARY)
        cv2.imshow("Threshold", img3)
        cv2.waitKey()
        cv2.destroyWindow("Threshold")

    elif userChar == 'm':
        gImg = cv2.cvtColor(img_inv, cv2.COLOR_BGR2GRAY)
        (height, width, depth) = img_inv.shape
        mask = np.zeros((height, width, 1), np.uint8)
        mask[50:int(height / 2), 50:int(width / 2)] = 255
        maskedImg1 = cv2.bitwise_and(gImg, mask)
        cv2.imshow("Mask", maskedImg1)
        cv2.waitKey()
        cv2.destroyWindow("Mask")

    elif userChar == 'h':
        grayIm1 = cv2.cvtColor(img_inv, cv2.COLOR_BGR2GRAY)
        newGray = cv2.equalizeHist(grayIm1)
        cv2.imshow('Equalized', newGray)
        cv2.waitKey()
        cv2.destroyWindow("Equalized")
