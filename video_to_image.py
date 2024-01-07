#Break video to multiple images ans save in a folder
import cv2

vidcap=cv2.VideoCapture("F:\CV\Code\Data\dog.mp4")
ret,img=vidcap.read()
count=0
while True:
    if ret==True:
        cv2.imwrite("F:\\CV\\Code\\Data\\img\\imgN%d.jpg"%count,img)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count**1000)) #used to hold speed of frame generation
        ret,img=vidcap.read()
        cv2.imshow('res', img)
        print ('Read a new frame:',count ,ret)
        count+=1
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
            cv2.destroyAllWindows()
    else:
        break
vidcap.release()
cv2.destroyAllWindows()