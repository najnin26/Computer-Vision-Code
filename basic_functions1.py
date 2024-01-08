#Drawing function in opencv

import cv2 as cv
import numpy as np

#creating blank image
#img=np.zeros([512,512,3],np.uint8)*255  #black image
img=np.ones([512,512,3],np.uint8)*255    #white image


#img=cv.imread("F:\\CV\\Code\\Data\\thor.jpg")
img=cv.resize(img, (600,700))

#Here line accept 5 parameter (img,starting,ending,color,thickness)
img=cv.line(img,(0,0), (200,200),(154,92,424),8)

#arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness) 
img = cv.arrowedLine(img, (0,125), (255,255), (255, 0, 125), 10)

#Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 8)#-1 for filled

#circle - accept(img,star_co,radius,color,thickness)
img = cv.circle(img, (447, 125), 63, (214, 255, 0), -5)#negative for filled and positive for not filled

font = cv.FONT_ITALIC
#puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)
img = cv.putText(img, 'THOR', (20, 500), font, 4, (0, 125, 255), 10,cv.LINE_AA)

#ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv.ellipse(img,(400,600),(100,50),0,0,360,155,5)
cv.imshow('res', img)

cv.waitKey(0)
cv.destroyAllWindows()
