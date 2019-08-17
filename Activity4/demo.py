import cv2
import numpy as np

cam = cv2.VideoCapture(0)



while True:
    ret, currFrame = cam.read()
    currGray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

    ret, currThresh = cv2.threshold(currFrame, 100, 255, cv2.THRESH_BINARY)


    img, contrs,hier = cv2.findContours(currThresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(currThresh,contrs,-1,(0,255,0),3)

    cv2.imshow("Motion", currFrame)

    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == "q":
        break

    prevFrame = currFrame

cam.release()
cv2.destroyAllWindows()
