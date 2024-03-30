#Optical Flow-- Lucas-Kanade method
#Optical flow is the pattern of apparent motion of image objects
#between two consecutive frames caused by the movemement 
#of object or camera.

#Optical flow works on several assumptions:

#The pixel intensities of an object do not change b/w consecutive frames.
#Neighbouring pixels have similar motion.

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("F:\\CV\\Code\\Data\\test2.mp4")

# params for ShiTomasi corner detection
feature_params=dict(maxCorners=100,
                    qualitylevel=0.3,
                    minDistance=7,
                    blocksize=7
                    )
while  True:
    ret, frame = cap.read()
    
    if ret == True:
        frame=cv.resize(frame, (700,600))
        cv.imshow('Frame', frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
