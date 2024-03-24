import cv2
import numpy as np

img=cv2.imread("F:\\CV\\Code\\Data\\avengers.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template=cv2.imread("F:\\CV\\Code\\Data\\temp.jpg",0)
w,h=template.shape[::-1]

res=cv2.matchTemplate(gray, template, cv2.TM_CCORR_NORMED)


print("RES",res)
threshold=0.999
count=0
loc=np.where(res>=threshold)

for i in zip(*loc[::-1]):
    print('i==',i)
    cv2.rectangle(img, i, (i[0]+w,i[1]+h),(0,0,255),2)
    count+=1
    
print("count==",count)
img=cv2.resize(img, (800,600))
cv2.imshow('img', img)
res=cv2.resize(res, (800,600))
cv2.imshow('temp ', res)

cv2.waitKey(0)
cv2.destroyAllWindows()