#Capture Video from youtube
import pafy
import cv2
url="https://www.youtube.com/watch?v=wIAs97ynODo&list=PLaHodugB5x-Ddy_H951h0VHjOjfzZNCBh&index=7&t=6s"

data=pafy.new(url)
data=data.getbest(preftype="mp4")
#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0)   #Here parameter 0 is a path of any video use for webcam

cap.open(data.url)
print("check===",cap.isOpened())
#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("F:\CV\Code\Data\output.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()


#if any os error regarding youtube-dl occur thn
#conda install -c forge youtube-dl
#pip3 install youtube-dl