import cv2


img1 = cv2.imread('F:\\CV\\Code\\Data\\avengers.jpg',1)  
img1 = cv2.resize(img1,(1280,700))#width ,height
cv2.imshow("Colored Image",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
print("Give image with color==\n",img1)


img2 =cv2.imread("F:\\CV\\Code\\Data\\avengers.jpg",0)
img2 =cv2.resize(img2,(1280,700))
cv2.imshow("Gray scaled image", img2)
print("Gray image==\n",img2)


img3 =cv2.imread("F:\\CV\\Code\\Data\\avengers.jpg",-1)
img3 =cv2.resize(img3,(1280,700))
cv2.imshow("Original image", img3)
print("Original image==\n",img3)



#Image conversion project colored image into grayscale.
path=input("Enter the image path= ")
img4=cv2.imread(path,1)
img4=cv2.resize(img4, (300,300))
img4 = cv2.flip(img4,-1)
cv2.imshow("Converted image", img4)
k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("F:\\CV\\Code\\Data\\output.png",img4)
else:
    cv2.destroyAllWindows()
