import cv2
import numpy as np

frame=cv2.imread("F:\\CV\\Code\\Data\\color_balls.jpg")
frame=cv2.resize(frame, (600,400))

#used to pass the parameter value and handle null value
def nothing(x):
    pass

cv2.namedWindow('Color Adjustment')
cv2.createTrackbar('Lower_H','Color Adjustment', 0, 255, nothing)
cv2.createTrackbar('Lower_S','Color Adjustment', 0, 255, nothing)
cv2.createTrackbar('Lower_V','Color Adjustment', 0, 255, nothing)

cv2.createTrackbar('Upper_H','Color Adjustment', 255, 255, nothing)
cv2.createTrackbar('Upper_S','Color Adjustment', 255, 255, nothing)
cv2.createTrackbar('Upper_V','Color Adjustment', 255, 255, nothing)

while True:
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos('Lower_H','Color Adjustment')
    l_s=cv2.getTrackbarPos('Lower_S','Color Adjustment')
    l_v=cv2.getTrackbarPos('Lower_V','Color Adjustment')
    
    u_h=cv2.getTrackbarPos('Upper_H','Color Adjustment')
    u_s=cv2.getTrackbarPos('Upper_S','Color Adjustment')
    u_v=cv2.getTrackbarPos('Upper_V','Color Adjustment')


    lower_bound=np.array([l_h,l_s,l_v])
    upper_bound=np.array([u_h,u_s,u_v])
    
    #Creating Mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
