import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\chess.jpg")
img=cv2.resize(img, (400,400))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray, 20, 250)

cv2.imshow('edge', edges)
cv2.imshow("lines", img)

cv2.waitKey(0)
cv2.destroyAllWindows()