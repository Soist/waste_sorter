import numpy as np
import cv2

vidCap = cv2.VideoCapture(0)

while True:
    ret, image = vidCap.read()
    img_inv = image[:, ::-1, :]
    cv2.imshow("Original", img_inv)

    gray_img = cv2.cvtColor(img_inv, cv2.COLOR_BGR2GRAY)

    res, thresh = cv2.threshold(gray_img, 90, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold", thresh)

    blurImg = cv2.GaussianBlur(thresh, (3, 5), 0)
    cv2.imshow("Guassian", blurImg)

    canny = cv2.Canny(blurImg, 50, 270)
    cv2.imshow("canny", canny)

    #contrs, hier, contrs_img = cv2.findContours(blurImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img_inv, contrs, -1, (0, 255, 0), 3)
    #cv2.imshow('Contours', image)

    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        break
