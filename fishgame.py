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
    # time.sleep(duration)     # 保持
    # controller.release(key)  # 释放DDDDDDD
time.sleep(3)
keyboard.press('f')

while True:
    try:
        if ZZZGetposition.get_position('wen') is not None:
            pyautogui.moveTo(ZZZGetposition.get_position('Ffish'))
            time.sleep(0.83)
            pyautogui.click()
            print('已经找到图片')

            break
    except pyautogui.ImageNotFoundException:
        print('未找到图牌')
        time.sleep(0.001)
while True:
    try:
            if ZZZGetpositionfish.get_position('AN') is not None:
                try:
                    if ZZZGetpositionfishD.get_position('D') is not None:
                                while  True:
                                    try:
                                        if ZZZGetpositionfishD.get_position('D') is not None:
                                            print("按下D")
                                            pyautogui.moveTo('D')
                                            pyautogui.mouseDown()
                                    except pyautogui.ImageNotFoundException:
                                            pyautogui.moveTo('D')
                                            pyautogui.mouseUp('D')
                                            break
                except pyautogui.ImageNotFoundException:
                    while True:
                        try:
                            if ZZZGetpositionfishA.get_position('A') is not None:
                                print("按下A")
                                pyautogui.moveTo('A')
                                pyautogui.mouseDown()
                        except pyautogui.ImageNotFoundException:
                            pyautogui.moveTo('A')
                            pyautogui.mouseUp('A')
                            break
    except pyautogui.ImageNotFoundException:
        try:
            if ZZZGetpositionfishD.get_position('D') is not None:
                while True:
                    try:
                        if ZZZGetpositionfishD.get_position('D') is not None:
                            print("点按D")
                            keyboard.press('D')
                            time.sleep(0.0002)

                    except pyautogui.ImageNotFoundException:
                        break

        except pyautogui.ImageNotFoundException:
            while True:
                try:
                    if ZZZGetpositionfishA.get_position('A') is not None:
                        print("点按A")
                        keyboard.press('A')
                        time.sleep(0.02)
                except pyautogui.ImageNotFoundException:
                    break









