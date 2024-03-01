#Image Gradient--
#It is a directional change in the color or intensity in an image.
#It is most important part to find inormation from image
#Like finding edges within the images.
#There are various methods to find image gradient.
#These are - Laplacian Derivatives,SobelX and SobelY.
#All these functions have diff. mathematical approach to get result.
#All load image in the gray scale

import cv2
import numpy as np

#load image into gray scale
img = cv2.imread("F:\\CV\\Code\\Data\\avengers.jpg")
img = cv2.resize(img,(400,300))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian Derivative---It calculate laplace derivate
#parameter(img,data_type for -ve val,ksize)
#kernal size must be odd
lap=cv2.Laplacian(img_gray,cv2.CV_64F,ksize=3)
lap=np.int8(np.absolute(lap))

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("Laplacian==",lap)
#cv2.imshow("SobelX===",sobelX)
#cv2.imshow("SobelY==",sobelY)
#cv2.imshow("COmbined image==",sobelcombine)

cv2.waitKey(0)
cv2.destroyAllWindows()