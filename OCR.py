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
while True:
    try:
        if ZZZGetpositionfish.get_position('chang_anD') is not None:
            try:
                if ZZZGetpositionfishD.get_position('D1') or ZZZGetpositionfishD.get_position('D2') is not None:
                        print("按下D")
                        pyautogui.moveTo(1604,879)
                        pyautogui.mouseDown(button='left')
            except pyautogui.ImageNotFoundException:
                pyautogui.mouseUp(button='left')


    except pyautogui.ImageNotFoundException:
        pyautogui.mouseUp(button='left')

        print("WEIF")
        time.sleep(2)