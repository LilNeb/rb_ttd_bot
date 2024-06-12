import keyboard
import time
import pyautogui
import os
import glob

# The coordinates corresponds to the relative position of the element in the image, in order to crop and better ocr it.
coordinate_sets = {
    'lobby_menus': {
        'x_rel': 54/1000,    # The relative x start point (0 means the start of the image)
        'y_rel': 392/1000,  # The relative y start point (1/3 means 1/3rd of the image height)
        'w_rel': 6/100,  # The relative width (1/7 means 1/7th of the image width)
        'h_rel': 3/100   # The relative height (1/3 means 1/3rd of the image height)
    },
    'start_button': {
        'x_rel': 44/100,    # The relative x start point (1/4 means 1/4th of the image width)
        'y_rel': 665/1000,    # The relative y start point (2/3 means 2/3rd of the image height)
        'w_rel': 1/9,    # The relative width (1/2 means half of the image width)
        'h_rel': 1/10     # The relative height (1/6 means 1/6th of the image height)
    },
    'in_game': {
        'x_rel': 455/1000,    # The relative x start point (1/4 means 1/4th of the image width)
        'y_rel': 128/1000,    # The relative y start point (2/3 means 2/3rd of the image height)
        'w_rel': 10/100,    # The relative width (1/2 means half of the image width)
        'h_rel': 3/100     # The relative height (1/6 means 1/6th of the image height)
    },
    'disconnected': {
        'x_rel': 250/1000,    # The relative x start point (1/4 means 1/4th of the image width)
        'y_rel': 400/1000,    # The relative y start point (2/3 means 2/3rd of the image height)
        'w_rel': 50/100,    # The relative width (1/2 means half of the image width)
        'h_rel': 30/100     # The relative height (1/6 means 1/6th of the image height)
    },
    'play_again_menus': {
        'x_rel': 250/1000,    # The relative x start point (1/4 means 1/4th of the image width)
        'y_rel': 280/1000,    # The relative y start point (2/3 means 2/3rd of the image height)
        'w_rel': 50/100,    # The relative width (1/2 means half of the image width)
        'h_rel': 50/100     # The relative height (1/6 means 1/6th of the image height)
    },
    'upgrade_menus': {
        'x_rel': 1/1000,    # The relative x start point (1/4 means 1/4th of the image width)
        'y_rel': 500/1000,    # The relative y start point (2/3 means 2/3rd of the image height)
        'w_rel': 25/100,    # The relative width (1/2 means half of the image width)
        'h_rel': 20/100     # The relative height (1/6 means 1/6th of the image height)
    },
    'ad_game_finished': {
        'x_rel': 280/1000,    # The relative x start point (1/4 means 1/4th of the image width)
        'y_rel': 720/1000,    # The relative y start point (2/3 means 2/3rd of the image height)
        'w_rel': 17/100,    # The relative width (1/2 means half of the image width)
        'h_rel': 15/100     # The relative height (1/6 means 1/6th of the image height)
    }
}

# This dictionary maps the status you want to check with the actual word to look for in the OCR results
status_mapping = {
        "lobby_menus": "units",
        
        "start_button": "start",
        
        "in_game": "auto",
        "in_game": "skip",
        
        "disconnected": "reconnect",
        "disconnected": "idle",
        "disconnected": "minutes",
        
        "play_again_menus":"waves",
        "play_again_menus":"lost",
        "play_again_menus":"play",
        "play_again_menus":"again",
        "play_again_menus":"total",
        
        "upgrade_menus":"upgrade",
        "upgrade_menus":"first",
        "upgrade_menus":"sell",
        "upgrade_menus":"target",
        
        "ad_game_finished": "return",
        "ad_game_finished": "to",
        "ad_game_finished": "lobby"
        
    }

# useful coordinates
ui_coordinates = {
    'chat': {
        'x': 122,
        'y': 273
    },
    'start_button': {
        'x': 400,
        'y': 510
    },
    'autoskip_button': {
        'x': 428,
        'y': 112
    },
    'ground': {
        'x': 400,
        'y': 510
    },
    'reconnect_button': {
        'x': 490,
        'y': 450
    },
    'play_again_button': {
        'x': 550,
        'y': 500
    },
    'upgrade_button': {
        'x': 50,
        'y': 410
    },
    'sell_button': {
        'x': 85,
        'y': 480
    },
    'target_spider': {
        'x': 401,
        'y': 371
    },
}

# words to paste
pasta = {
    'lobby_command': "//lobby"
}


# Useful functions

def write(text):
    for char in text:
        keyboard.write(char)
        time.sleep(0.1)
        
def click_on_coordinates(ui_coordinates):
    pyautogui.moveTo(ui_coordinates['x'], ui_coordinates['y'], duration=0.2)
    pyautogui.click()
    time.sleep(0.2)
    return

def delete_all_files_in_screenshots():
    files = glob.glob('./screenshots/*')
    for f in files:
        if os.path.isfile(f):
            os.remove(f)
    print("All files in the 'screenshots' directory have been deleted.")