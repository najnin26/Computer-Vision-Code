import cv2 as cv
img = cv.imread('F:/CV/Code/Data/park.jpg')
cv.imshow('Image', img)

# Converting to grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Park', gray)

# Blur 
blur=cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny=cv.Canny(img, 125, 175)
cv.imshow('Canny edge', canny)

# Dilating the image
dilated=cv.dilate(canny,(7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded=cv.erode(dilated, (7,7),iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized=cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)