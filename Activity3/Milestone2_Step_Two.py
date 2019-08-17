'''Identify corners in the camera'''

import cv2

vidCap = cv2.VideoCapture(0)

orb = cv2.ORB_create()

fast = cv2.FastFeatureDetector_create()

while True:
    ret,img = vidCap.read()
    img_inv= img[:,::-1,:]


    keypts_ORB, des = orb.detectAndCompute(img_inv, None)

    img2 = cv2.drawKeypoints(img_inv, keypts_ORB, None, (255, 0, 0), 4)

    cv2.imshow("ORB", img2)

    keypts_FAST = fast.detect(img_inv, None)
    img3 = cv2.drawKeypoints(img_inv, keypts_FAST, None, (255, 0, 0), 4)

    cv2.imshow("FAST", img3)

    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        break