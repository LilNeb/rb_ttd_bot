import ocr
import screenshot
import crop
import cv2
import time
import sys
import interpret_ocr

# screenshot --> crop it --> ocr it --> interpret the ocr results

def get_current_state_of_the_game(window_name, screenshot_path):
    # Take a screenshot and save it
    raw_screenshot_path = screenshot.takeScreenshotAndSave(window_name, screenshot_path)
    print("Here is the screenshot image path : " , raw_screenshot_path)
    
    # Crop raw screenshot with all coordinates sets
    cropped_images_dict = crop.crop_image_for_all_coordinates_sets(raw_screenshot_path)
    print("Here is the cropped images dictionnary : ",cropped_images_dict)
    
    # OCR the cropped images
    ocr_results = ocr.ocr_files(cropped_images_dict)
    print("Here is the detected text on cropped images : ",ocr_results)
    
    # Interpret the OCR results
    status = interpret_ocr.get_status_from_ocr_results(ocr_results)
    print("Here is the status of the game : ",status)
    
    # # Crop raw screenshot with given coordinates
    # cropped_img_start_button_path = crop.crop_image_with_coordinates(raw_screenshot_path, 'start_button')
    # cropped_img_lobby_menus_path = crop.crop_image_with_coordinates(raw_screenshot_path, 'lobby_menus')
    # # OCR the cropped images
    # ocr_start_button_coordinates_json = ocr.ocr_files(cropped_img_start_button_path)
    # print("here is the detected text on cropped img start button",ocr_start_button_coordinates_json)
    # ocr_lobby_menu_coordinates_json = ocr.ocr_files(cropped_img_lobby_menus_path)
    # print("here is the detected text on cropped img lobby menus",ocr_lobby_menu_coordinates_json)
    # # check for status in the OCR results
    # print('Start button status : ',interpret_ocr.get_status_from_ocr_results(ocr_start_button_coordinates_json))
    # print('Lobby status :        ',interpret_ocr.get_status_from_ocr_results(ocr_lobby_menu_coordinates_json))
    return