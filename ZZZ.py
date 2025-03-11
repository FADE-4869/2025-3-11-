import time#pythonproject
import pyautogui
from PIL import Image
import pytesseract
from sympy import print_glsl
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR'
access_attempts=2
def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format(word),confidence=0.85)
    return up_left
# pyautogui.moveTo(get_position('MHY2'))
# pyautogui.doubleClick()
# time.sleep(2)
# p=0
# while True:
#         try:
#             if get_position('ZZZ') is not None:
#                 pyautogui.moveTo(get_position('ZZZ'))
#                 print('找到')
#                 pyautogui.doubleClick()
#                 time.sleep(1.5)
#                 break
#         except pyautogui.ImageNotFoundException:
#             print('无法找到')
#             time.sleep(1)
#
# pyautogui.moveTo(get_position('start'))
# pyautogui.doubleClick()
time.sleep(6)
num=0
while num<10:
        try:
            if pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format('using'),confidence=0.9) is not None:
                    pyautogui.moveTo(get_position('using'))
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.moveTo(get_position('password'))
                    pyautogui. click()
                    pyautogui.write('qinruili4869')
                    time.sleep(0.5)
                    pyautogui.moveTo(get_position('phone'))
                    time.sleep(0.5)
                    pyautogui.doubleClick()
                    pyautogui.write('15023134279')
                    time.sleep(0.2)
                    pyautogui.moveTo(get_position('00'))
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.moveTo(get_position('ZZZstart'))
                    pyautogui.click()
                    break
            else:
                    print("Image not found on the screen.")


        except pyautogui.ImageNotFoundException:
            time.sleep(2)
            num=num+2
            print("Imag not found ovn the screen. (Caught ImageNotFoundException)")




while True:
    try:
        if get_position('ZZZdjjr') is not None:
            print('已经找到图片')
            pyautogui.click()

            break
    except pyautogui.ImageNotFoundException:

        print('未找到点击开始')

        time.sleep(0.1)

