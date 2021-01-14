import os
import pyautogui

def click():
    try:
        BASE_DIR = os.path.dirname(__file__)
        img = pyautogui.locateOnScreen(os.path.join(BASE_DIR, 'button.png'))
        img = pyautogui.center(img)
        pyautogui.click(img)
    except:
        pass