import cv2 as cv


def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

#For the image

img=cv.imread('F:\\CV\\Code\\Data\\avengers.jpg')
resized_img=rescaleFrame(img,scale=0.4)
cv.imshow("Resized image ", resized_img)


#For the video
cap=cv.VideoCapture('F:\CV\Code\Data\dog.mp4')

while True:
    ret,frame=cap.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    cv.imshow("Video", frame)
    cv.imshow("Resized vodeo ", frame_resized)
    if cv.waitKey(25) & 0xFF==ord("q"):
        break
    
cap.release()
cv.destroyAllWindows()    