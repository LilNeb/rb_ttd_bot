import sys
import state
import time
import inputs

window_name = 'Roblox'
screenshot_path = './screenshots'

# [Useless for now] Check if command-line arguments are provided 
if len(sys.argv) > 1:
    # Extract the parameters from command-line arguments
    param = sys.argv[1]

# Infinite loop to keep checking the game state
# while True:
#     current_state = state.get_current_state_of_the_game(window_name, screenshot_path)
#     print(current_state)
#     time.sleep(2)
    
# Uses the param to know what kind of action to take in the game
def action(param):
    if param == 'autoplay':
        inputs.go_to_lobby()
        inputs.go_to_fortress()
        pass
    else:
        # Invalid action
        pass