import cv2
img=cv2.imread("F:\CV\Code\Data\lady.jpg")

print(img.shape)
crop=img[220:270,220:400]

cv2.imshow("Img",img)
cv2.imshow("Crop",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
