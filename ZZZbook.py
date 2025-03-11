import ZZZGetpositionfish
import time  #pythonproject
import pyautogui
import keyboard
from pyautogui import leftClick
from pynput.keyboard import Controller, Key
keyboard = Controller()
import ZZZKO
import pynput
import threading
from PIL import Image
import pytesseract
from sympy import print_glsl
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR'
access_attempts=2
import ZZZGetposition
import ZZZGetpositionfishD
import ZZZGetpositionfishA
def hold_key(key, duration):
    controller = Controller()
    controller.press(key)    # 按下
    time.sleep(duration)     # 保持
    controller.release(key)  # 释放

def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format(word),confidence=0.85)
    return up_left
def ZZZ_book():
    while True:
            pyautogui.click(996,155)
            try:
                if get_position('book') is not None:

                    print('找到手册')

                    break
            except pyautogui.ImageNotFoundException:
                hold_key(Key.f2,0.5)
                print('无法找到')
                time.sleep(1)