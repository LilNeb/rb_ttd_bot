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
    
def go_to_fortress():
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
    
def play_fortress_game(autoskip=True):
    if autoskip:
        enable_autoskip()
    time.sleep(55) # wait to have enough money (400)
    place_unit("1")
    target_static_unit()
    time.sleep(120) # wait to have enough money (700)
    sell_unit()
    place_unit("2")
    is_spider_targeted = try_targeting_spider()
    if is_spider_targeted:
        time.sleep(120) # wait to have enough money (1800)
        upgrade_unit(target_unit=False)
        time.sleep(130) # wait to have enough money (4000)
        upgrade_unit(target_unit=False)
        time.sleep(90) # wait to have enough money (8000)
        upgrade_unit(target_unit=False)
    

    while True:
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        # print(current_state)
        # 
        if current_state.get('play_again_menus') == True:
            break
        else:
            #throw error
            print("Dont know what state the player is in, exiting...")
        time.sleep(1)   

def play_again():
# if state = play_again_menus --> click on play_again_button
# else --> return "disconnected"
    current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
    current_state = dict(current_state)
    # print(current_state)
    
    if current_state.get('play_again_menus') == True:
        utils.click_on_coordinates(ui_coordinates['play_again_button'])
        time.sleep(15)
        play_fortress_game()
        return True
    else:
        return False
        

def upgrade_unit(target_unit=True):
    if target_unit:
        target_ground()
    
    #check 10 times if upgrade_menus is True, break if True
    for _ in range(10):
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        time.sleep(5)
        # print(current_state)
        if current_state.get('upgrade_menus') == True:
            break
    else:
        print("Failed to find upgrade_menus status after 10 seconds.")
    utils.click_on_coordinates(ui_coordinates['upgrade_button'])

def try_targeting_spider(tries=15):
    for _ in range(tries):
        print("Trying to target spider...")
        pyautogui.moveTo(461, 371)
        pyautogui.click(duration=0.0)
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        time.sleep(5)
        # print(current_state)
        if current_state.get('upgrade_menus') == True:
            print("Successfully targeted spider.")
            return True
        else:
            print("Failed to target spider.")
            return False

def target_static_unit():
    utils.click_on_coordinates(ui_coordinates['target_spider'])
    #get state 5 times
    for _ in range(5):
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        if current_state.get('upgrade_menus') == True:
            break
        time.sleep(1)
    else:
        print("Failed to find upgrade_menus status after 5 seconds.")

def sell_unit():
    target_ground()
    
    #check 10 times if upgrade_menus is True, break if True
    for _ in range(10):
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        time.sleep(5)
        # print(current_state)
        if current_state.get('upgrade_menus') == True:
            break
    else:
        print("Failed to find upgrade_menus status after 10 seconds.")
    utils.click_on_coordinates(ui_coordinates['sell_button'])

def enable_autoskip():
    utils.click_on_coordinates(ui_coordinates['autoskip_button'])
    
def target_ground():
    utils.click_on_coordinates(ui_coordinates['start_button'])
    
def place_unit(slot):
    pyautogui.press(slot)
    target_ground()
    pyautogui.click()

# place_unit("2")
# try_targeting_spider()