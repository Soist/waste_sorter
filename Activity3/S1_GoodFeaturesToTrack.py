'''In their place, add a ​for​ loop that loops over the rows of the ​goodFeats​ array.
For each row, extract the x and y values, and draw a small circle on the original image at that location.'''
import cv2
import numpy as np
img1 = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
goodFeats = cv2.goodFeaturesToTrack(grayImg, 100, 0.1, 5)
corners = np.float32(goodFeats)

for item in corners:
    x, y = item[0]
    cv2.circle(img1, (x,y), 5, 255, -1)

cv2.imshow("goodFeats", img1)
cv2.waitKey()

print (goodFeats[0], goodFeats[2])
print (goodFeats[0,0])
print (goodFeats[0,0,0], goodFeats[0,0,1])