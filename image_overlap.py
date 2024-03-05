import cv2
import numpy as np

img1=cv2.imread("F:\CV\Code\Data\hero1.jpg")
img2=cv2.imread("F:\CV\Code\Data\lady.jpg")

img1=cv2.resize(img1, (500,500))
img2=cv2.resize(img2, (500,500))

new=cv2.addWeighted(img1, 1, img2, 1, 1)
cv2.imshow("Img", new)

cv2.waitKey(0)
cv2.destroyAllWindows()