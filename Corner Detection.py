import numpy as np
import cv2 as cv

img=cv.imread("F:\CV\Code\Data\shapes.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=np.float32(gray)

res=cv.cornerHarris(gray, 2, 3,0.04)

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
