import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
upperbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')


img = cv2.imread('static/jack2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255), -1)
    roi_gray = gray[y:y+h, x:x+w]

# upperbody = upperbody_cascade.detectMultiScale(
#     gray,
#     scaleFactor=1.05,
#     minNeighbors=5,
#     minSize=(30, 30)
#     #flags = cv2.CV_HAAR_SCALE_IMAGE
# )
# for (x,y,w,h) in upperbody:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()