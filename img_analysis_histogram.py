#Imgage Histogram - Find, Plot and Analyze
#It which gives you an overall idea about the intensity distribution of an image. 
#It distribute data along x and y axis.
# x - axis contain range of color vlaues.
# y - axis contain numbers of pixels in an image.
#With histogram to extrct information about contast, brigthness and intensity etc.

import numpy as np
import cv2 
from matplotlib import pyplot as plt

#plotting with calhist method
"""
img=np.zeros((200,200),np.uint8)

cv2.rectangle(img, (0,100), (200,200),(255),-1)
cv2.rectangle(img, (0,50), (50,100),(127),-1)

hist=cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()

cv2.imshow("res", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
img=cv2.imread("F:\\CV\\Code\\Data\\thor.jpg")
img=cv2.resize(img, (500,650))
b,g,r=cv2.split(img)
cv2.imshow("img", img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

plt.hist(b.ravel(), 256,[0,256])
plt.hist(g.ravel(), 256,[0,256])
plt.hist(r.ravel(), 256,[0,256])
plt.title("Colorful image")
plt.show()

#cal
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.title("ColorFull Image")
plt.plot(hist)
plt.show()

#gray scale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist=cv2.calcHist(gray, [0], None, [256], [0,256])
plt.plot(hist)
plt.title("Gray Image")
plt.show()


#Histogram equalization is good when  of the image is confined to a particular region.
#It accept gray scale image

equ=cv2.equalizeHist(gray)
res=np.hstack((gray,equ))
cv2.imshow('equ', res)
hist1=cv2.calcHist([equ], [0], None, [256], [0,256])
plt.plot(hist1)
plt.title("Equalization")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()