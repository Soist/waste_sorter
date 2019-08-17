'''
Answer in comment
For an individual image like "puzzle3.png",
I think goodFeaturesToTrack is better.
I can preset a reasonable value for maxCorners.
Then the image will have all the marking points neatly lying at the corners.
For an individuak image, Harris is not as neat as goodFeaturesToTrack,
but Harris provides more details than goodFeaturesToTrack. (shows the cross section while goodFeaturesToTrack just shows a point)

For a set of images, Harris is much better than goodFeaturesToTrack.
If we do not preset a reasonable value of maxCorner for goodFeaturesToTrack,
it cannot detect all the corners in an image.
However, Harris can always detect all the corners in an image.
'''

'''Identify corners in the image'''
import cv2
import numpy as np

img = cv2.imread("SampleImages/PuzzlesAndGames/puzzle3.png")
img1 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 4, 3, 0.04)

dilDst = cv2.dilate(dst, None)
thresh = 0.01 * dst.max()
ret, threshDst =  cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

disp = np.uint8(threshDst)
cv2.imshow("Harris", disp)

goodFeats = cv2.goodFeaturesToTrack(gray, 200, 0.1, 15)

corners = np.float32(goodFeats)

for item in corners:
    x, y = item[0]
    cv2.circle(img1, (x,y), 5, 255, -1)
cv2.imshow("goodFeats", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------------------------------------------

img = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")
img1 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 4, 3, 0.04)

dilDst = cv2.dilate(dst, None)
thresh = 0.01 * dst.max()
ret, threshDst =  cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

disp = np.uint8(threshDst)
cv2.imshow("Harris", disp)

goodFeats = cv2.goodFeaturesToTrack(gray, 200, 0.1, 15)

corners = np.float32(goodFeats)

for item in corners:
    x, y = item[0]
    cv2.circle(img1, (x,y), 5, 255, -1)
cv2.imshow("goodFeats", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------------------------------------------

img = cv2.imread("SampleImages/PuzzlesAndGames/puzzle1.jpg")
img1 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 4, 3, 0.04)

dilDst = cv2.dilate(dst, None)
thresh = 0.01 * dst.max()
ret, threshDst =  cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

disp = np.uint8(threshDst)
cv2.imshow("Harris", disp)

goodFeats = cv2.goodFeaturesToTrack(gray, 200, 0.1, 15)

corners = np.float32(goodFeats)

for item in corners:
    x, y = item[0]
    cv2.circle(img1, (x,y), 5, 255, -1)
cv2.imshow("goodFeats", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------------------------------------------

img = cv2.imread("SampleImages/PuzzlesAndGames/puzzle2.jpg")
img1 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 4, 3, 0.04)

dilDst = cv2.dilate(dst, None)
thresh = 0.01 * dst.max()
ret, threshDst =  cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

disp = np.uint8(threshDst)
cv2.imshow("Harris", disp)

goodFeats = cv2.goodFeaturesToTrack(gray, 200, 0.1, 15)

corners = np.float32(goodFeats)

for item in corners:
    x, y = item[0]
    cv2.circle(img1, (x,y), 5, 255, -1)
cv2.imshow("goodFeats", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()