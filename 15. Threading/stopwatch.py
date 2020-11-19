# StopWatch.py

import time
import pyperclip

print('''Press Enter to begin, each Enter pressed means a new lap.
CTRL+C ends the program.''')


def just(num):
    return str(num).rjust(6)


input()

print('START')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap #{lapNum}: {just(totalTime) + ' (' + just(lapTime) + ')'}", end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("Done!")
