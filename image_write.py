import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\cat.jpg")
img=cv2.resize(img, (300,300))


h=np.hstack((img,img))
v=np.vstack((h,h))

cv2.imwrite("F:\CV\Code\Data\mod.jpg", v)
cv2.imshow("New image",v)
cv2.waitKey(0)
cv2.destroyAllWindows()