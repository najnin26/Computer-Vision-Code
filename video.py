import cv2

cap=cv2.VideoCapture("F:\CV\Code\Data\dog.mp4")
print("cap",cap)

while True:
    res,frame=cap.read()
    frame=cv2.resize(frame, (700,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame",frame)
    cv2.imshow("Gray", gray)
    k=cv2.waitKey(25)
    if k== ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()

