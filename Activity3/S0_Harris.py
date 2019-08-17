'''Try out this code. ​
Look at what happens when you don’t dilate the Harris result before thresholding it.
What happens if you change the three parameters of the call to the Harris detector?
Make a version of this program that draws a circle on the original image at every location where a corner has been found.
'''

import cv2
import numpy as np

img = cv2.imread("SampleImages/PuzzlesAndGames/puzzle4.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Compute Harris
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print(dst[0])

# Isolate Harris corners from image
dilDst = cv2.dilate(dst, None)
thresh = 0.01 * dst.max()
ret, threshDst =  cv2.threshold(dilDst, thresh, 255, cv2.THRESH_BINARY)

'''corners = np.float32(dst)


for item in corners:
    x, y = item[0]
    cv2.circle(img, (x,y), 5, 255, -1)'''

# Display corners points
disp = np.uint8(threshDst)
cv2.imshow("Harris", disp)
cv2.waitKey(0)
cv2.destroyAllWindows()
