import cv2
import numpy
image=cv2.imread("F:\CV\Code\Data\dogcat2.jpg")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face=cv2.CascadeClassifier("F:\CV\Code\Data\haarcascade_frontalcatface.xml") #for detecting face

faces=face.detectMultiScale(gray,1.1,1)

for (x,y,w,h) in faces:
  image=cv2.rectangle(image, (x,y),(x+w,y+h), (255,0,0),2)
  

image = cv2.resize(image,(800,700))
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()  
