#ROI(Region of Interest)

import cv2
import numpy as np

img=cv2.imread("F:\\CV\\Code\\Data\\roi_opr.jpg")
img=cv2.resize(img, (800,800))
cv2.imshow('Image',img)

#ROI
#(320,49) (435,218)
#[(y1,y2),(x1,x2)]
#diff y=169  x=115
roi=img[49:218,320:435]

img[49:218,90:205]=roi
img[49:218,205:320]=roi

img[49:218,441:556]=roi
img[49:218,557:672]=roi
img[49:218,673:788]=roi

#changing y===
img[350:519,60:175] = roi
cv2.imshow("original image==",img)

#Now try to use one image data into another image
img1 = cv2.imread("F:\\CV\\Code\\Data\\ironman.jpg")
img1 = cv2.resize(img1,(900,600))
img1[1:170,560:675]=roi


cv2.imshow("Modified image==",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()