# autoForm.py url = 'https://autbor.com/form'

"""Upgraded version of the project from the book."""

import keyboard
import pyautogui
import json
import time


"""
>>> Uncomment to get coordinates of the buttons <<<

print('Press CTRL + C, to stop the program.')

field = {}
try:
    while True:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))

        if keyboard.is_pressed('space'):  # Press space to save the coordinates of your cursor.
            field[(x, y)] = pixelColor
            print(f'x: {x}, y: {y}, RGB: ({pixelColor})')
except KeyboardInterrupt:
    print(field)
"""

pyautogui.PAUSE = 0.5

with open('form.json') as f:
    formData = json.load(f)

# Pass the coordinates to these variables.
nameField = (777, 320)
submitButton = (754, 868)
submitAnotherLink = (779, 219)

for person in formData['info']:
    print('>>> 2-SEC break to let you press CTRL+C <<<')
    time.sleep(2)

    print(f"Inserting information about {person['name']}")

    pyautogui.click(nameField[0], nameField[1])
    pyautogui.typewrite(person['name'] + '\t')
    pyautogui.typewrite(person['fear'] + '\t')

    sourceData = {'wand': ['down'],
                  'amulet': ['down', 'down'],
                  'crystal ball': ['down', 'down', 'down'],
                  'money': ['down', 'down', 'down', 'down']}

    robocopData = {1: ['space'],
                   2: ['right'],
                   3: ['right', 'right'],
                   4: ['right', 'right', 'right'],
                   5: ['right', 'right', 'right', 'right']}

    for keyS, valueS in sourceData.items():
        if person['source'] == keyS:
            pyautogui.typewrite(valueS)
            pyautogui.press('enter')
            pyautogui.press('tab')

    for keyR, valueR in robocopData.items():
        if person['robocop'] == keyR:
            pyautogui.typewrite(valueR)
            pyautogui.press('tab')
            pyautogui.press('tab')

    pyautogui.typewrite(person['comments'] + '\t')
    pyautogui.press('enter')

    print(f"Form for {person['name']} sent!")
    time.sleep(1)

    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
