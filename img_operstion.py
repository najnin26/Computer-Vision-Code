#Image operations
import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\pikachu.jpg")
print("shape==",img.shape) #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("Imagetype==",type(img))
print("datatype==",img.dtype) #returns Image datatype is obtained

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()