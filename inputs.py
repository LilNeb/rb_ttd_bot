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
    
    for _ in range(10):
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
    
def go_to_fortress(autoskip=True):
    current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
    current_state = dict(current_state)
    attempts = 0
    
    while current_state.get('start_button') == False:
            go_to_lobby()
            #press w for 15 seconds
            pyautogui.keyDown('w')
            time.sleep(15)
            pyautogui.keyUp('w')
            pyautogui.keyDown('s')
            time.sleep(0.2)
            pyautogui.keyUp('s')
            #get state 5 times
            for _ in range(5):
                current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
                current_state = dict(current_state)
                if current_state.get('start_button') == True:
                    break
                time.sleep(1)
            attempts += 1
            if attempts > 5:
                raise Exception("Failed to find start_button status after 5 attempts.")
            
    print("arrived at fortress, entering it now...")
    utils.click_on_coordinates(ui_coordinates['start_button'])
    # check 15 times if in_game status is true
    for _ in range(15):
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        if current_state.get('in_game') == True:
            print("in_game status is true")
            break
        time.sleep(1)
    else:
        raise Exception("Failed to find in_game status after 15 seconds.")
    
    time.sleep(6)
    if autoskip:
        enable_autoskip()
    
def play_fortress_game(replay=True):
    go_to_fortress()   
    time.sleep(45) 
    #equip $400 unit by pressing 1
    pyautogui.press('1')
    target_ground()
    pyautogui.click()
    
    
    
    
def enable_autoskip():
    utils.click_on_coordinates(ui_coordinates['autoskip_button'])
    
def target_ground():
    utils.click_on_coordinates(ui_coordinates['start_button'])
    
    
    
# go_to_fortress()
# target_ground()
# enable_autoskip()
play_fortress_game()