import cv2
import numpy

# Draw a smiley face
draw3 = 255 * numpy.ones((400,500,3), numpy.uint8)

cv2.ellipse(draw3, (250,200), (100,60),0,0,180,(0,0,0),10)

cv2.circle(draw3, (200,150), 5, (0,0,0), -1)
cv2.circle(draw3, (300,150), 5, (0,0,0), -1)

cv2.imshow("Smile", draw3)
'''
draw1 = numpy.zeros((300, 500, 3), numpy.uint8)
draw2 = 255 * numpy.ones((500, 300, 3), numpy.uint8)

cv2.line(draw2, (50, 50), (150, 250), (0, 0, 255))
cv2.rectangle(draw1, (10, 100), (100, 10), (0, 180, 0),-1)

cv2.circle(draw2, (30, 30), 30, (220, 0, 0),-1)

cv2.ellipse(draw1, (250, 150), (100, 60), 30, 0, 220, (250, 180, 110), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(draw1, "Hi, there", (10, 270), font, 1, (255, 255, 255))

cv2.imshow("Black", draw1)
cv2.imshow("White", draw2)

cv2.imwrite("blackPic.jpg", draw1)
cv2.imwrite("whitePic.jpg", draw2)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()




