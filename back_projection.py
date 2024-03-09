#BackProjection using histogram technique

import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\green.jpg")
img=cv2.resize(img, (600,650))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

roi=cv2.imread("F:\CV\Code\Data\g.jpg")
roi_hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

roi_hist=cv2.calcHist([roi_hsv], [0,1], None, [180,256], [0,180,0,256])
mask=cv2.calcBackProject([hsv], [0,1], roi_hist, [0,180,0,256], 1)

kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask=cv2.filter2D(mask,-1,kernel)

_,mask=cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

mask=cv2.merge((mask,mask,mask))
result=cv2.bitwise_or(img, mask)

cv2.imshow("Original image",img)
cv2.imshow("Roi", hsv)
cv2.imshow("Mask", mask)
cv2.imshow("Result", result)


cv2.waitKey(0)
cv2.destroyAllWindows()
