import cv2
vid=cv2.VideoCapture("F:\CV\Code\Data\dog.mp4")
sub=cv2.createBackgroundSubtractorMOG2()
while True:
    r,frame=vid.read()
    if r==True:
        frame=cv2.resize(frame,(700,500))
        sub_v=sub.apply(frame)
        cv2.imshow("Img",frame)
        cv2.imshow("Sub",sub_v)
        if cv2.waitKey(25) & 0xff==ord('q'):
            break
    else:
        break
vid.release()
cv2.waitKey(0)
cv2.destroyAllWindows()