#add shapes and text on Video 

import cv2
import datetime

cap=cv2.VideoCapture("F:\CV\Code\Data\dog.mp4")
print("For width=",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("For height=",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Width=",cap.get(3))#here 3 for width
print("Height=",cap.get(4))#here 4 for height

while cap.isOpened():
    ret,frame=cap.read()
    frame=cv2.resize(frame, (800,600))
    if ret == True:
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        text=' Height : ' + str(cap.get(4)) + " Width : " + str(cap.get(3))
        frame = cv2.putText(frame, text, (10,20), font,1,(0,0,0),1,cv2.LINE_AA)
        date_date="Date "+str(datetime.datetime.now())
        frame = cv2.putText(frame, date_date, (20,50), font,1,(0,0,0),1,cv2.LINE_AA)
        frame = cv2.rectangle(frame, (384, 10), (510, 128), (128, 0, 255), 8)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(30) & 0xFF==ord('q'):
            break
    else:
        break
    
    
cap.release()
cv2.destroyAllWindows()

