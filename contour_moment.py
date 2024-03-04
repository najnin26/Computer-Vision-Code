#Contours - 
#Contours can be explained simply as a curve joining all the continuous points 
#(along the boundary), having same color or intensity. 

#The contours are a useful tool for shape analysis and object detection and recognition

#For better accuracy, use binary images and also apply edge detection before 
#findig countours.

#findCountour function manipulate original imge so copy it before proceeding.
#findContour is like finding white object from black background.
#so you must turn image in white and background is black.

import cv2
import numpy as np

img = cv2.imread("F:\\CV\\Code\\Data\\shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)
#findcontour(img,contour_retrival_mode,method)
cnts,hier=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.

print("Number of conour==",cnts,"\ntotal contour ==",len(cnts))
print("Hierarchy==\n",hier)

#img=cv2.drawContours(img, cnts, -1, (10,20,100),4)

for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M=cv2.moments(c)
    print("M==",M)
    cX=int(M["m10"]/M["m00"])
    cY=int(M["m01"]/M["m00"])
    cv2.drawContours(img, [c], -1, (0,255,0),4)
    cv2.circle(img,(cX, cY), 7, (255,255,255),-1)
    cv2.putText(img, "center", (cX-20,cY-20), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,255), 2)

cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

