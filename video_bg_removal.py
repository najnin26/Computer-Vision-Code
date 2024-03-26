import numpy as np
import cv2 as cv
cap = cv.VideoCapture("F:\\CV\\Code\\Data\\qqptest2.mp4")

alg01=
while True:
    ret, frame = cap.read()
    frame = cv.resize(frame,(600,400))
    if frame is None:
        break
    cv.imshow('original', frame)
    keyboard = cv.waitKey(60)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()

