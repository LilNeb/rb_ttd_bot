import pyautogui
import time
import utils
import pyperclip
import keyboard

ui_coordinates = utils.ui_coordinates
pasta = utils.pasta

def go_to_lobby():
    time.sleep(5)
    utils.click_on_coordinates(ui_coordinates['chat'])
    utils.write(pasta['lobby_command'])
    pyautogui.press('enter')


go_to_lobby()