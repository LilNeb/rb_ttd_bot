import ocr
import screenshot
import crop
import cv2
import time
import sys
import status

windowName = 'Roblox'
repoPath = './screenshots'

# Take a screenshot and save it
raw_screenshot_path = screenshot.takeScreenshotAndSave(windowName, repoPath)
print("Here is the screenshot image path : " , raw_screenshot_path)
#show the screenshot
# img = cv2.imread(raw_screenshot_path)
# if img is None:
#  sys.exit("Could not read the raw screenshot image.")
# cv2.imshow("Display window", img)
# k = cv2.waitKey(0)



#process image and crop it to only show the text (and save it)
cropped_img_start_button = crop.crop_image_with_coordinates(raw_screenshot_path, 'start_button')
cropped_img_lobby_menus = crop.crop_image_with_coordinates(raw_screenshot_path, 'lobby_menus')
# if cropped_img is None:
#  sys.exit("Could not read the cropped screenshot image.")
#display the cropped image
# cv2.imshow("Cropped", cv2.imread(cropped_img))
# k = cv2.waitKey(0)


# ocr the cropped image
# file_path = '/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717072046.png'
#display the cropped image
# cv2.imshow("Cropped", cv2.imread(cropped_img_start_button))
# k = cv2.waitKey(0)
ocr_start_button_coordinates_json = ocr.ocr_file(cropped_img_start_button)
print("here is the detected text on cropped img start button",ocr_start_button_coordinates_json)
# cv2.imshow("Cropped", cv2.imread(cropped_img_lobby_menus))
# k = cv2.waitKey(0)
ocr_lobby_menu_coordinates_json = ocr.ocr_file(cropped_img_lobby_menus)
print("here is the detected text on cropped img lobby menus",ocr_lobby_menu_coordinates_json)

# check for status
status.check_status(ocr_start_button_coordinates_json, "start_button")
status.check_status(ocr_lobby_menu_coordinates_json, "lobby")