#Image operations
import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\pikachu.jpg")
img=cv2.resize(img, (600,400))
print("shape==",img.shape) #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("Imagetype==",type(img))
print("datatype==",img.dtype) #returns Image datatype is obtained

#Now try to split an image
#print(cv2.split(img))
b,g,r = cv2.split(img)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow('original',img)
#merge all channel
mr1=cv2.merge((r,g,b))
cv2.imshow('rgb', mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)
cv2.waitKey(0)
cv2.destroyAllWindows()