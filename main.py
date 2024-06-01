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
    print("HERE IS PARAM",param)
    
# Uses the param to know what kind of action to take in the game
def action(param):
    if param == 'autoplay':
        current_state = state.get_current_state_of_the_game('Roblox', './screenshots')
        current_state = dict(current_state)
        print(current_state)
        
        if current_state.get('play_again_menus') == False:
            print("Starting autoplay...")
            inputs.go_to_lobby()
            print("Arrived at lobby")
            inputs.go_to_fortress()
            print("Arrived at fortress")
            inputs.play_fortress_game(autoskip=True)
            print("Playing fortress game")
            action('autoplay')
        
        elif current_state.get('play_again_menus') == True:
            print("Play again menus status is true")
            inputs.play_again()
            print("Playing again")
            action('autoplay')
        elif current_state.get('disconnected') == True:
            inputs.reconnect()
            action('autoplay')
            print("Reconnecting...")
        
        

action(param)