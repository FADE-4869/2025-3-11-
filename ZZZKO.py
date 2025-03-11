import time  #pythonproject
import pyautogui
import keyboard
from pyautogui import leftClick
from pynput.keyboard import Controller, Key
keyboard = Controller()
import pynput
import ZZZGetposition
from PIL import Image
import pytesseract
from sympy import print_glsl
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR'
access_attempts=2

def queding():
    i=0
    while i<5:
        try:
            if ZZZGetposition.get_position('queding') is not None:
                pyautogui.moveTo(ZZZGetposition.get_position('queding'))
                pyautogui.click()
                print('找到确定')
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            i=i+1
            print('未找到确定')

