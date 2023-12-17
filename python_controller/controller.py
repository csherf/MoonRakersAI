import pyautogui
import os

class Controller:
    def __init__(self):
        pass

    def zoom():
        pyautogui.press('z')
        pyautogui.press('.', presses=6)

    def activate_window(name):

        # Name of the window you want to focus on
        app_name = name

        # AppleScript command to activate the application
        script = f'''
        tell application "{app_name}"
            activate
        end tell
        '''

        # Run the AppleScript
        os.system(f"osascript -e '{script}'")
