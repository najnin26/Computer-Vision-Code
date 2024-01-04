import cv2




#Image conversion project colored image into grayscale.
path=input("Enter the image path= ")
img4=cv2.imread(path,0)
img4=cv2.resize(img4, (560,700))
img4 = cv2.flip(img4,-1)
cv2.imshow("Converted image", img4)


k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("F:\\CV\\Code\\Data\\output.png",img4)
else:
    cv2.destroyAllWindows()