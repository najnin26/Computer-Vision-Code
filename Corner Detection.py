import numpy as np
import cv2 as cv

img=cv.imread("F:\CV\Code\Data\shapes.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=np.float32(gray)

res=cv.cornerHarris(gray, 3, 3,0.04)

res=cv.dilate(res, None)
img[res>0.01*res.max()]=[0,0,255]
cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
