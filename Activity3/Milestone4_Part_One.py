'''Identify eyes'''

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt0.xml")
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye1.xml')

if face_cascade.empty():
     raise IOError('Unable to load the face cascade classifier xml file')

if eye_cascade.empty():
     raise IOError('Unable to load the eye cascade classifier xml file')


cap = cv2.VideoCapture(0)


while True:
       ret, frame = cap.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)
       for (x, y, w, h) in faces:
           roi_gray = gray[y:y + h, x:x + w]
           roi_color = frame[y:y + h, x:x + w]
           eyes = eye_cascade.detectMultiScale(roi_gray)
           for (x_eye, y_eye, w_eye, h_eye) in eyes:
               center = (int(x_eye + 0.5 * w_eye), int(y_eye + 0.5 * h_eye))
               radius = int(0.3 * (w_eye + h_eye))
               color = (0, 255, 0)
               thickness = 3
               cv2.circle(roi_color, center, radius, color, thickness)
       cv2.imshow('Eye Detector', frame)

       v = cv2.waitKey(20)
       c = chr(v & 0xFF)
       if c == 'q':
           break
cap.release()
cv2.destroyAllWindows()
