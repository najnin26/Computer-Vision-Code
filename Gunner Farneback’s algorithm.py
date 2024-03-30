import numpy as np
import cv2 

cap = cv2.VideoCapture("F:\\CV\\Code\\Data\\test2.mp4")


ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv=np.zeros_like(frame1)
hsv[...,1]=255

while(1):
    ret,frame2 = cap.read()
#    resize = cv2.resize(frame, (640, 480))
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
    flow=cv2.calcOpticalFlowFarneback(prvs, next, None,
                                      0.5,
                                      levels=3, 
                                      winsize=15,
                                      iterations=3,
                                      poly_n=5,
                                      poly_sigma=1.2, 
                                      flags=0)
    mag,ang=cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0]=ang*180/np.pi/2
    hsv[...,2]=cv2.normalize(mag, None,0,255,cv2.NORM_MINMAX)
    rgb=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    im1=cv2.add(frame2,rgb)
    img1=cv2.resize(im1, (700,430))
    
    cv2.imshow('frame',im1)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k==ord('s'):
        cv2.imwrite("F:\\CV\\Code\\Data\\1.png", frame2)
        cv2.imwrite("F:\\CV\\Code\\Data\\2.png", rgb)
    prvs = next
        
cap.release()
cv2.destroyAllWindows()

