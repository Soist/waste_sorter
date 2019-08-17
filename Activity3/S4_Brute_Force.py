import cv2
img1 = cv2.imread("SampleImages/Coins/coins1.jpg")
img2 = cv2.imread("SampleImages/Coins/dollarCoin.jpg")

orb = cv2.ORB_create()
bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)



matches = bfMatcher.match(des1, des2)
matches.sort(key = lambda x: x.distance)  # sort by distance

# draw matches with distance less than threshold
for i in range(len(matches)):
    if matches[i].distance > 50.0:
        break

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:i], None)

cv2.imshow("Matches", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()