import cv2

faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt0.xml")

'''cap = cv2.VideoCapture(0)


while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face_rects:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.imshow("FD", frame)
        v = cv2.waitKey(20)
        c = chr(v & 0xFF)
        if c == 'q':
            break


cap.release()'''

img = cv2.imread("SampleImages/CardsAndSigns/Door1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)
for ( x, y, w, h) in face_rects:
    cv2.rectangle( img, (x,y), (x+w, y+h), (0, 255, 0) , 3)

cv2.imshow("Face", img)
cv2.waitKey()
cv2.destroyAllWindows()