import cv2
import numpy as np

cam = cv2.VideoCapture(0)

ret, prevFrame = cam.read()
prevGray = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)


while True:
    ret, currFrame = cam.read()
    currGray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)

    ret, prevThresh = cv2.threshold(prevFrame, 100, 255, cv2.THRESH_BINARY)
    ret, currThresh = cv2.threshold(currFrame, 100, 255, cv2.THRESH_BINARY)

    diff = cv2.absdiff(prevFrame,currFrame)


    img1, contrs, hier = cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(currThresh,contrs,-1,(0,255,0),3)

    cv2.imshow("Motion", currFrame)

    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == "q":
        break

    prevFrame = currFrame

cam.release()
cv2.destroyAllWindows()
