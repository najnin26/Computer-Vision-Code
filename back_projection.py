#BackProjection using histogram technique

import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\green.jpg")
img=cv2.resize(img, (600,650))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow("Original image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
