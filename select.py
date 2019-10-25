import cv2
import numpy as np
 

 
# Read image
im = cv2.imread("face.jpeg")
# Select ROI
fromCenter = False
r = cv2.selectROI(im, fromCenter)
         
# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(0)
