import cv2
import numpy

img = cv2.imread("SampleImages/snowLeo2.jpg")

cv2.circle(img,(130,130), 70, (0,0,255),5)

cv2.rectangle(img,(250,130),(550,250), (0,200,0), -1)

cv2.line(img,(560,230),(600,400),(240,0,0),3)
cv2.line(img,(570,210),(600,338),(240,0,0),3)
cv2.line(img,(580,190),(600,275),(240,0,0),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"snowLeo2.jpg",(10,40),font,1,(0,255,255))

cv2.imshow("snowLeo2", img)

cv2.waitKey()