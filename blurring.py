import cv2 as cv
img = cv.imread("F:\CV\Code\Data\cats.jpg")
cv.imshow('Cats', img)

# Averaging
average=cv.blur(img, (3,3))
cv.imshow('Blur', img)

# Gaussian Blur
gauss=cv.GaussianBlur(img, (3,3), 0)
cv.imshow('GaussianBlur', gauss)

# Median Blur
med=cv.medianBlur(img, 3)
cv.imshow('MedianBlur', med)

# Bilateral
bil=cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bil)

cv.waitKey(0)
cv.destroyAllWindows()