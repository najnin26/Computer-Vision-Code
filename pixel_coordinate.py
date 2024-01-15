#Working on pixel color values------

import cv2
import numpy as np
img=cv2.imread("F:\CV\Code\Data\lion.jpg")
img = cv2.resize(img,(1024,700))
cv2.imshow('lion', img)
print("shape==",img.shape) #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("Imagetype==",type(img))
print("datatype==",img.dtype)
#access a pixel value by its row and column coordinates.
px=img[520,580]
print("the pixel of that co-ordinates==",px) #we get the pixel value
#Now try to find selected channel value from cordinate
#We know we have three channel -   0,1,2
# accessing only blue pixel
blue = img[520,580,0]
print("the pixel having blue color==",blue)
grn = img[520,580,1]
print("the pixel having green color==",grn)
red = img[520,580,2]
print("the pixel having red color==",red)


cv2.waitKey(0)
cv2.destroyAllWindows()