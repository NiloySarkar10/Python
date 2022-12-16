import pyautogui
import time
from random import randint 

time.sleep(5)
for i in range(0, 500):
    col = randint(50, 1500)
    row = randint(100, 999)
    time_duration = randint(2, 12)
    sleep_duration = randint(3, 10)
    pyautogui.moveTo(col, row, duration = time_duration)
    time.sleep(sleep_duration)