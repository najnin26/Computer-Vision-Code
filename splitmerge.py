import cv2 as cv
import numpy as np

img=cv.imread("F:\CV\Code\Data\park.jpg")
b,g,r=cv.split(img)

blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])


cv.imshow('image', img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

mer=cv.merge([b,g,r])
cv.imshow('merged', mer)

cv.waitKey(0)
cv.destroyAllWindows()