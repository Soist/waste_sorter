import cv2
import numpy

vidCap = cv2.VideoCapture(0)
#i,j = 0,0
#while i < 256:
#    while j < 256:

while True:
 ret, img = vidCap.read()
 img1 = img[:,::-1,:]

 gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

 cannyImg = cv2.Canny(gray, 140, 140)
#print("i = " + str(i) + "            j = " + str(j))

 cv2.imshow("Canny", cannyImg)

#j += 10

 x = cv2.waitKey(10)
 userChar = chr(x & 0xFF)
 if userChar == 'q':
    break
#    j = 0

#    i += 10

    '''x = cv2.waitKey(1000)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        break'''

