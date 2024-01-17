import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("F:\\CV\\Code\\Data\\cats.jpg")
cv.imshow('Cats', img)

blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100,255,-1)

masked=cv.bitwise_and(img, img,mask=mask)

cv.imshow('Mask', masked)

#Gray scale histogram
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

gray_hist=cv.calcHist([gray], [0], mask, [256], [0,256])


plt.figure()
plt.title("Gray scale histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()