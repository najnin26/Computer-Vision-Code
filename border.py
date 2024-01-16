#How to create a border for an image using opencv
import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\lion.jpg")
img = cv2.resize(img,(1000,600))
#creating image border 
#with the help of cv2.copyMakeBorder() function.
#it take parameters like(img,border_width*4,bordertype,val_brder)
#border woidth = top,bottom,right,left
bdr=cv2.copyMakeBorder(img, 10, 10, 5, 5, cv2.BORDER_CONSTANT,value=[255,0,125])


cv2.imshow('res', img)
cv2.imshow('bordered', bdr)

cv2.waitKey(0)
cv2.destroyAllWindows()