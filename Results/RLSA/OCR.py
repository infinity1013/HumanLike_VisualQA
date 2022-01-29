# importing modules
import cv2
import pytesseract

# reading image using opencv
image = cv2.imread('struct_image.png')

#converting image into gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# converting it to binary image by Thresholding
# this step is require if you have colored image because if you skip this part
# then tesseract won't able to detect text correctly and this will give incorrect result
threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

"""
# display image
cv2.imshow('threshold image', threshold_img)

# Maintain output window until user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()"""

#configuring parameters for tesseract
custom_config = r'--oem 3 --psm 6'

# now feeding image to tesseract
details = pytesseract.image_to_data(threshold_img, output_type=Output.DICT, config=custom_config, lang='eng')
print(details.keys())
