import cv2

cap=cv2.VideoCapture(0)
print("cap",cap)

#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("F:\CV\Code\Data\output.avi",fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.flip(frame, 0)
        cv2.imshow("Frame",frame)
        cv2.imshow("Gray", gray)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    
    
cap.release()
output.release()
cv2.destroyAllWindows()
