import cv2
vidCap = cv2.VideoCapture(0)
'''
for i in range(100):
    ret, img = vidCap.read()
    cv2.imshow("Webcam", img)
    x = cv2.waitKey(10)
 #   print(i, chr(x & 0xFF))
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        break
'''
flag = False
while flag == False:
    ret, img = vidCap.read()
    cv2.imshow("Webcam",img)
    x= cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        flag = True


cv2.destroyAllWindows()
vidCap.release()