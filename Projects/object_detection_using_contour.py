import cv2
import numpy as np 


#Read Camera
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def nothing(x):
    pass

#window name
cv2.namedWindow("Color Adjustments",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments", (300,300))
cv2.createTrackbar("Thresh","Color Adjustments",0,255,nothing)

#COlor Detection Track

cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)

while True:
    _,frame=cap.read()
    frame=cv2.resize(frame, (400,400))
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #detecting hand
    l_h=cv2.createTrackbar("Lower_H", "Color Adjustments")
    l_s=cv2.createTrackbar("Lower_S", "Color Adjustments")
    l_v=cv2.createTrackbar("Lower_V", "Color Adjustments")

    u_h=cv2.createTrackbar("Upper_H", "Color Adjustments")
    u_s=cv2.createTrackbar("Upper_S", "Color Adjustments")
    u_v=cv2.createTrackbar("Upper_V", "Color Adjustments")
    
    lower_bound=np.array([l_h,l_s,l_v])
    upper_bound=np.array([u_h,u_s,u_v])
    
    #creating mask
    mask=cv2.inRange(hsv, lower_bound, upper_bound)
    #filter mask with image
    filter=cv2.bitwise_and(frame, frame,mask=mask)
    
    
    
    