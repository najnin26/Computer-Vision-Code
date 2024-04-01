import cv2
import numpy as np

img=cv2.imread("F:\\CV\\Code\\Data\\a.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face=cv2.CascadeClassifier("F:\\CV\\Code\\Data\\haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier(("F:\\CV\\Code\\Data\\haarcascade_eye.xml"))

faces=face.detectMultiScale(gray,4,4)

for (x,y,w,h) in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h), (127,0,205),3)
    
img=cv2.resize(img, (800,600))
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()