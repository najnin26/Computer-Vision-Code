# Import packages
import cv2
import numpy as np

img = cv2.imread('F:/CV/Code/Data/avengers.jpg')
img=cv2.resize(img, (700,700))
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image
cropped_image = img[80:280, 150:330]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("F:/CV/Code/Data/Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()