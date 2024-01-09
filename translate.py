import numpy as np
import cv2 as cv

img=cv.imread("F:\CV\Code\Data\park.jpg")
cv.imshow('Park', img)

#translate
def translate(ing,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated=translate(img,-100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotation(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    
    rotMat=cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions=(width,height)
    return  cv.warpAffine(img, rotMat, dimensions)

rotated=rotation(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotation(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)