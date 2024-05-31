import cv2
import numpy as np
import pytesseract
import json
import re

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

# remove special characters
def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

# OCR file and return all found text as JSON
def ocr_files(image_dict):
    found_text = {}
    for name, file_path in image_dict.items():
        image = cv2.imread(file_path)
        gray = get_grayscale(image)
        thresh = thresholding(gray)
        opening_img = opening(gray)
        canny_img = canny(gray)

        images = {'Original Image': image, 'Grayscale Image': gray, 'Thresholded Image': thresh, 'Opening Image': opening_img, 'Canny Image': canny_img}

        text_dict = {}
        for img_name, img in images.items():
            text = pytesseract.image_to_string(img, config=custom_config)
            cleaned_text = remove_special_characters(text)
            text_dict[img_name] = cleaned_text

        found_text[name] = text_dict

    return json.dumps(found_text)


# Test
# image_dict = {
#     'lobby_menus': '/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717109905_lobby_menus_cropped.png',
#     'start_button': '/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717109905_start_button_cropped.png'
# }
# print(ocr_files(image_dict))
