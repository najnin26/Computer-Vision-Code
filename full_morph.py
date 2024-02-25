import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\girl.jpg")
img=cv2.resize(img, (300,300))
_,mask=cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
kernel=np.ones((2,2),np.uint8)

e=cv2.erode(mask, kernel)
d=cv2.dilate(mask, kernel)
o = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
c=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
x1=cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
x2=cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
x3=cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Erode', e)
cv2.imshow('dialated', d)
cv2.imshow('Opening', o)
cv2.imshow('Closing', c)
cv2.imshow("x1",x1) 
cv2.imshow("x2",x2) 
cv2.imshow("x3",x3)


from matplotlib import pyplot as plt
titles=['img','mask','erosion','dilation','opening','closing','x1', 'x2',"x3"]
images=[img,mask,e,d,o,c,x1,x2,x3]
for i in range(9):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
cv2.waitKey(0)
cv2.destroyAllWindows()