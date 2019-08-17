import cv2
vidCap = cv2.VideoCapture(0)

count = 0
flag = False
while flag == False:
    ret, img = vidCap.read()
    img2 = img[:,::-1,:]
    cv2.imshow("Webcam",img2)
    x= cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        flag = True
    elif userChar == 's':
        cv2.imwrite("snap.jpg",img2)



cv2.destroyAllWindows()
vidCap.release()