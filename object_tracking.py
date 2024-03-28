#Object Tracking using Meanshift Algo.
#The idea behind this algo is to move small window to get the high 
#density pixels same as histogram backprojection.

#Steps to use this algo-----
#First setup target and find its histogram for backproject the traget.
#ALso set one initial location
#setup the termination criteria

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("F:\\CV\\Code\\Data\\test2.mp4")

ret, frame = cap.read()

while  True:
    ret, frame = cap.read()
    
    if ret == True:
        cv.imshow('Original== ', frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()