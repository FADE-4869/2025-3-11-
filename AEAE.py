import time
import pyautogui
import threading
from pynput.keyboard import Controller, Key
keyboard = Controller()

def hold_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)
time.sleep(3)
hold_key('e', 0.5)

time.sleep(1.893)

hold_key('j', 0.5)
time.sleep(1.893)
hold_key('j', 0.5)
time.sleep(1.893)
hold_key('j', 0.5)
time.sleep(1.893)