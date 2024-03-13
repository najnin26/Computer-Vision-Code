import cv2
import numpy as np
img=np.ones((500,500,3),np.uint8)*255
img1=np.zeros((500,500,3),np.uint8)*255
cv2.imshow("Img",img)
cv2.imshow("Img1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()