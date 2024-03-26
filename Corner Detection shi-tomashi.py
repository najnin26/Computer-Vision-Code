import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread("F:\CV\Code\Data\shapes.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cornres=cv.goodFeaturesToTrack(gray,40, 0.01, 20)
cornres=np.int64(cornres)

for i in cornres:
    x,y=i.ravel()
    cv.circle(img,(x,y),3,255,-1)


cv.imshow('res== ', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()

