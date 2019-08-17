import cv2
import numpy

imageNames = ["grandTetons.jpg", "landscape1.jpg",
              "mightyMidway.jpg", "mushrooms.jpg",
              "snowLeo1.jpg", "snowLeo2.jpg",
              "snowLeo3.jpg", "snowLeo4.jpg",
              "chicago.jpg", "canyonlands.jpg"]

for name in imageNames:
    img = cv2.imread("SampleImages/" + name)
    cv2.imshow("win", img)
    cv2.waitKey()
cv2.destroyAllWindows()
