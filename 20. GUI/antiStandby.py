# Simple program that moves your cursor so your computer does not go into standby mode.

import time
import pyautogui

value = 50

while True:
    try:
        time.sleep(10)
        pyautogui.moveRel(value, 0, duration=0.5)
        pyautogui.moveRel(0, value, duration=0.5)
        pyautogui.moveRel(-value, 0, duration=0.5)
        pyautogui.moveRel(0, -value, duration=0.5)
    except KeyboardInterrupt:
        print('Done!')
