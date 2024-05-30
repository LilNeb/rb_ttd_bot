import cv2
import numpy as np
import pytesseract
import json

custom_config = r'--oem 3 --psm 6'

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)
 
# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

# OCR file and return all found text as JSON
def ocr_file(file_path):
    image = cv2.imread(file_path)
    gray = get_grayscale(image)
    thresh = thresholding(gray)
    opening_img = opening(gray)
    canny_img = canny(gray)

    images = {'Original Image': image, 'Grayscale Image': gray, 'Thresholded Image': thresh, 'Opening Image': opening_img, 'Canny Image': canny_img}

    found_text = {}
    for name, img in images.items():
        text = pytesseract.image_to_string(img, config=custom_config)
        found_text[name] = text

    return json.dumps(found_text)

