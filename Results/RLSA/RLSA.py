import cv2
import numpy as np
#image = cv2.imread('struct_image.png') # reading the image
image = cv2.imread('Screenshot.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert2grayscale
(thresh, binary) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # convert2binary
#cv2.imshow('binary', binary)
#cv2.imwrite('binary.png', binary)

# find contours
contours, _ = cv2.findContours(~binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#image is the name of the image
#Mode is Contour retrieval mode
#Method is Contour approximation method

for contour in contours:
    #draw a rectangle around those contours on main image
    [x,y,w,h] = cv2.boundingRect(contour)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 1)
"""    
cv2.imshow('contour', image)
cv2.imwrite('contours.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

mask = np.ones(image.shape[:2], dtype="uint8") * 255 # create blank image of same dimension of the original image
contours, _= cv2.findContours(~binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
heights = [cv2.boundingRect(contour)[3] for contour in contours] # collecting heights of each contour
avgheight = sum(heights)/len(heights) # average height

# finding the larger contours
# Applying Height heuristic
for c in contours:
    [x,y,w,h] = cv2.boundingRect(c)
    if 2*h > avgheight:
        cv2.drawContours(mask, [c], -1, 0, -1)
cv2.imshow('filter', mask)
cv2.imwrite('filter.png', mask)

from pythonRLSA import rlsa
import math
x, y = mask.shape
value = max(math.ceil(x/100),math.ceil(y/100))+20 #heuristic
mask = rlsa.rlsa(mask, True, False, value) #rlsa application
cv2.imshow('rlsah', mask)
cv2.imwrite('rlsah.png', mask)
