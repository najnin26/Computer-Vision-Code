import cv2
import numpy as np

img=cv2.imread("F:\CV\Code\Data\photo_2024-03-24_05-25-56.jpg")


cv2.circle(img,(148,250), 4,(0,0,255),-1)
cv2.circle(img,(810,255), 4,(0,0,255),-1)
cv2.circle(img,(16,1191), 4,(0,0,255),-1)
cv2.circle(img,(955,1171), 4,(0,0,255),-1)

w,h=(1280, 960)

src1=np.float32([[148,249],[810,255],[16,1191],[955,1171]])
dst1=np.float32([[0,0],[w,0],[0,h],[w,h]])


m=cv2.getPerspectiveTransform(src1, dst1)

new_img=cv2.warpPerspective(img, m,(w,h))
print(img.shape)
img=cv2.resize(img, (500,600))
new_img=cv2.resize(new_img, (500,600))
cv2.imshow('img', img)
cv2.imshow('img1', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

148,249
810,255
16,1191
955,1171


