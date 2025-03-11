
import pyautogui
import time
import Getposition

def  SRaward():
    time.sleep(4)
    num1=0
    while num1 <4:
        try:
            if Getposition.get_position('gift') is not None:
                pyautogui.moveTo(Getposition.get_position('gift'))
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(Getposition.get_position('manyou'))
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(Getposition.get_position('Fgift'))
                pyautogui.click()
                break
        except pyautogui.ImageNotFoundException:
            pyautogui.press('esc')
            print('未找到（。。。）')
            time.sleep(1.5)
            num1=num1+1
    # pyautogui.moveTo(1727, 112)#(...)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('esc')
    # pyautogui.moveTo(1680, 279)#（gift）
    # time.sleep(2)
if __name__ == '__main__':
    SRaward()
