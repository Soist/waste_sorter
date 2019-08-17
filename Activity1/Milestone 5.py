import cv2
import numpy

vidCap = cv2.VideoCapture(0)

'''img1 = cv2.imread("SampleImages/snowLeo1.jpg")'''
'''cv2.imread("SampleImages/snowLeo2.jpg")'''

ret, img= vidCap.read()

frameP = img[:,::-1,:]
prevPics = [frameP] * 5


flag = False
while flag == False:
    ret, imgN = vidCap.read()
    frameN = imgN

    prevPics.append(frameN)
    prevPics.pop(0)

    (hgt1, wid1, dep1) = prevPics[0].shape
    (hgt2, wid2, dep2) = frameN.shape

    newWid = min(wid1, wid2)
    newHgt = min(hgt1, hgt2)

    img1Crop = prevPics[0][0:newHgt, 0:newWid]
    img2Crop = frameN[0:newHgt, 0:newWid]

    imgFinal = cv2.addWeighted(img1Crop, 0.5,
                               img2Crop, 0.5, 0)

    cv2.imshow("Weight", imgFinal)
    x= cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        flag = True





