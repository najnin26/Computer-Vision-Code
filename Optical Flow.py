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
                    qualityLevel=0.3,
                    minDistance=7,
                    blockSize=7
                    )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
color=np.random.randint(0,255,(100,3))

ret,old_frame=cap.read()
old_gray=cv.cvtColor(old_frame,cv.COLOR_BGR2GRAY)
p0=cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask=np.zeros_like(old_frame)

while  True:
    ret, frame = cap.read()
    
    if ret == True:
        frame=cv.resize(frame, (700,600))
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        # calculate optical flow
        p1, st, err = cv.calcOpticalFlowPyrLK(old_gray,
                                          frame_gray, p0, 
                                          None, **lk_params)
        cv.imshow('Frame', frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
