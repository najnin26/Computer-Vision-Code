#Image Blending with Trackbars 

import cv2
import numpy as np

#read two different images of same channel
img1 = cv2.imread("F:\\CV\\Code\\Data\\roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("F:\\CV\\Code\\Data\\thor.jpg")
img2 = cv2.resize(img2,(500,700))
cv2.imshow("thor==",img1)
cv2.imshow("bro_thor==",img2)

def blend(x):
    pass

img=np.zeros((400,400,3),dtype='uint8')
cv2.namedWindow('Win')#create track bar windows
cv2.createTrackbar('alpha', 'Win', 1, 100, blend)
switch='0 : OFF \n 1 : ON'#create switch for invoke the trackbars
cv2.createTrackbar(switch, 'Win', 0, 1, blend) #create track bar for switch

while True:
    s=cv2.getTrackbarPos(switch, "Win")
    a=cv2.getTrackbarPos('alpha', "Win")
    n=float(a/100)
    print(n)
    
    if s==0:
        dst=img[:]
        
    else:
        dst=cv2.addWeighted(img1, 1-n, img2, n, 0)
        cv2.putText(dst, str(a), (20,50), cv2.FONT_ITALIC, 2, (0,125,255),2)
    
    cv2.imshow('dst', dst)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()