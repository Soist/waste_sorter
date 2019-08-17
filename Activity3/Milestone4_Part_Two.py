'''Identify eyes and attach figures to it'''

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt0.xml")
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye1.xml')

face_mask = cv2.imread('GoogleyEye.png')
h_mask, w_mask = face_mask.shape[:2]



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
            frame_roi = frame[y_eye:y_eye + h_eye, x_eye:x_eye + w_eye]
            face_mask_small = cv2.resize(face_mask, (w_eye, h_eye))

            face_mask_gray = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
            cv2.imshow("gray", face_mask_gray)

            face_mask_gray_INV = cv2.bitwise_not((face_mask_gray))
            cv2.imshow("gray inv", face_mask_gray_INV)
            cv2.moveWindow("gray inv", 1000, 300)

            cv2.moveWindow("gray", 1000,0)
            frame[y_eye:y_eye + h_eye, x_eye:x_eye + w_eye] = cv2.bitwise_and(frame_roi,face_mask_small)

            cv2.imshow("GoogleEye", frame)
            v = cv2.waitKey(10)
            c = chr(v & 0xFF)
            if c == 'q':
                break




'''while True:
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
               #cv2.circle(roi_color, center, radius, color, thickness)

               frame_roi = frame[y_eye:y_eye+h_eye, x_eye:x_eye+w_eye]
               face_mask_small = cv2.resize(face_mask, (w_eye, h_eye))


               gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
               ret, mask =cv2.threshold(gray_mask,180,255,cv2.THRESH_BINARY_INV)

               mask_inv = cv2.bitwise_not(mask)

               masked_face = cv2.bitwise_and(face_mask_small,face_mask_small,mask = mask)

               masked_frame = cv2.bitwise_and(frame_roi,frame_roi,mask = mask_inv)

               cv2.imshow("masked_frame", masked_frame)

               frame[y_eye:y_eye+h_eye, x_eye:x_eye+w_eye] = cv2.add(masked_face,masked_frame)
               cv2.imshow("GoogleEye",frame)
               v = cv2.waitKey(10)
               c = chr(v & 0xFF)
               if c == 'q':
                   break
cap.release()
cv2.destroyAllWindows()'''






