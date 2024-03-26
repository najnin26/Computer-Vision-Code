import numpy as np
import cv2 as cv

img=cv.imread("F:\CV\Code\Data\shapes.png")


cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
