import ocr
import screenshot
import crop
import cv2
import time
import sys
import interpret_ocr
import utils

# screenshot --> crop it --> ocr it --> interpret the ocr results --> give states of the game --> act accordingly

def get_current_state_of_the_game(window_name, screenshot_path):
    # Take a screenshot and save it
    raw_screenshot_path = screenshot.takeScreenshotAndSave(window_name, screenshot_path)
    # print("Here is the screenshot image path : " , raw_screenshot_path)
    
    # Crop raw screenshot with all coordinates sets
    # raw_screenshot_path="/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717233277.png"
    cropped_images_dict = crop.crop_image_for_all_coordinates_sets(raw_screenshot_path)
    print("Here is the cropped images dictionnary : ",cropped_images_dict)
    
    # OCR the cropped images
    ocr_results = ocr.ocr_files(cropped_images_dict)
    print("Here is the detected text on cropped images : ",ocr_results)
    
    # Interpret the OCR results
    status = interpret_ocr.get_status_from_ocr_results(ocr_results)
    print("Here is the status of the game : ",status)
    
    # Reconnect if disconnected
    if status.get('disconnected') == True:
        print("Reconnecting...")
        utils.click_on_coordinates(utils.ui_coordinates['reconnect_button'])
        time.sleep(10)
        
    return status

# get_current_state_of_the_game('Roblox', './screenshots')