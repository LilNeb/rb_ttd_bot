import pyautogui
import time
import utils
import pyperclip
import keyboard
import state

ui_coordinates = utils.ui_coordinates
pasta = utils.pasta

def go_to_lobby():
    time.sleep(5)
    utils.write(pasta['lobby_command'])
    pyautogui.press('enter')
    time.sleep(2)
    
    for _ in range(13):
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        # load current_state as a dictionary
        current_state = dict(current_state)
        print(current_state)
        
        # Check if any status is True for lobby_menus
        if (current_state.get('lobby_menus') == True):
            break
        
        time.sleep(1)
    else:
        raise Exception("Failed to find lobby_menus status after 13 seconds.")
    


go_to_lobby()