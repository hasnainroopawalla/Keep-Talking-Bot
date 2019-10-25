import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
src_path = "3.jpg"

def get_string(img):
    # Read image with opencv
    # Convert to gray
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('d',img)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result
print(get_string(cv2.imread(src_path)))
##
##print('--- Start recognize text from image ---')
##print(src_path + "2face.jpg")
##print(get_string(src_path))