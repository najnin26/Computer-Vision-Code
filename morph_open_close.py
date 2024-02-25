#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images. 
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two more basic Morphological Transformations are 
#1) - Opening and 2) - Closing

import cv2
import numpy as np

#Opening --
#Opening is just another name of erosion followed by dilation. 
#means first erosion take place then dilation

img=cv2.imread("F:\CV\Code\Data\col_balls.jpg",0)
_,mask=cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel=np.ones((3,3),np.uint8)
o = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow('Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Kernel', kernel)
cv2.imshow('Opening', o)

#closing
#It is opposite of opening
#closing is just another name of dilation followed by erosion. 
#means first dilation take place then erosion-
c=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', c)

from matplotlib import pyplot as plt
titles = ["img","mask","opening","closing"]
images = [img,mask,o,c]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()