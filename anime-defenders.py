import sys
import state
import time
import inputs
import pyautogui

window_name = 'Roblox'
screenshot_path = './screenshots'

# [Useless for now] Check if command-line arguments are provided 
# if len(sys.argv) > 1:
#     # Extract the parameters from command-line arguments
#     param = sys.argv[1]
#     print("HERE IS PARAM", param)

# Uses the param to know what kind of action to take in the game
def action():
    while True:  # Constantly check
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        # print(current_state)
        
        if current_state.get('ad_game_finished') == True:
            print("Ad game finished, pressing COMMAND + K and restarting...")
            # press down ctrl
            pyautogui.keyDown('ctrl')
            time.sleep(0.1)
            pyautogui.keyDown('k')
            time.sleep(0.5)
            # release ctrl
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('k')
            time.sleep(2)  # Wait for a moment before continuing the loop

action()
