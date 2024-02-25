#-------------Morphological Transformations-----------------------

#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images. 
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two basic Morphological Transformations are 1) - Erosion and 2) - Dilation

import cv2 as cv
import numpy as np

#Erosion---
#it erodes away the boundaries of foreground object

#kernal slides through all the image and all the pixel 
#from the original image conside 1 only if kernal's pixel is 1

img=cv.imread("F:\CV\Code\Data\col_balls.jpg",0)
_,mask=cv.threshold(img, 230, 255, cv.THRESH_BINARY_INV)
kernel=np.ones((5,5),np.uint8)
e=cv.erode(mask, kernel)

cv.imshow('Image', img)
cv.imshow('Mask', mask)
cv.imshow('Kernel', kernel)
cv.imshow('Erode', e)

#Dilation -- 
#It is just opposite of erosion.
#Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’
#So it inc. the white region in the image or size of foreground object in.
#Normally, in cases like noise removal, erosion is followed by dilation. 
#Because, erosion removes white noises, but it also shrinks our object. 

kernel=np.ones((3,3),np.uint8)
d=cv.dilate(mask, kernel)
cv.imshow('dialated', d)

from matplotlib import pyplot as plt
titles=['img','mask','erosion','dilation']
images=[img,mask,e,d]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

cv.waitKey(0)
cv.destroyAllWindows()
