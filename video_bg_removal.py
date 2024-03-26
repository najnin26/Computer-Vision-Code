import numpy as np
import cv2 as cv
cap = cv.VideoCapture("F:\\CV\\Code\\Data\\test2.mp4")

algo1=cv.createBackgroundSubtractorMOG2(detectShadows=True)
algo2=cv.createBackgroundSubtractorKNN(detectShadows=True)

while True:
    ret, frame = cap.read()
    frame = cv.resize(frame,(600,400))
    if frame is None:
        break
    
    res1=algo1.apply(frame)
    res2=algo2.apply(frame)
    
    cv.imshow('original', frame)
    cv.imshow('res1',res1)
    cv.imshow('res2',res2)
    
    keyboard = cv.waitKey(60)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()

