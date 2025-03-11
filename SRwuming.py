import time#pythonproject
import pyautogui
import time


import keyboard
import Getposition
def WUMING ():

    def get_position2(word):
        up_left = None
        while up_left == None:
            up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/{}.png'.format(word),confidence=0.95)
        return up_left


    y=0
    while y<2:
        try:
            if Getposition.get_position('wuming') is not None:
                pyautogui.moveTo(Getposition.get_position('wuming'))
                pyautogui.click()
                time.sleep(3)
                break
        except pyautogui.ImageNotFoundException:
            pyautogui.press('esc')
            print("未找到无名。。。。")
            time.sleep(2)
            y=y+1
    print(y)
    time.sleep(2)
    if y<2:
        try:
           if get_position2('WMgift') is not None:
                pyautogui.moveTo(Getposition.get_position('WMgift'))
                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(1673, 924)  # 领取
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(863, 66)  # 跳转
                time.sleep(1)
                pyautogui.doubleClick()
                time.sleep(1)
                pyautogui.moveTo(1418, 916)  # 领取
                pyautogui.click()
                time.sleep(1)
        except pyautogui.ImageNotFoundException:
                pyautogui.moveTo(1418, 916)  # 一键领取
                pyautogui.click()
                time.sleep(2)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('esc')
    # try:
    #     if get_position('rwding') is not None:
    #         pyautogui.moveTo(get_position('rwding'))
    #         pyautogui.click()
    #         time.sleep(2)
    #         pyautogui.moveTo(1673, 924)  # 领取
    #         pyautogui.click()
    #         time.sleep(2)
    # except pyautogui.ImageNotFoundException:
    #         pyautogui.moveTo(1673, 924)  # 领取
    #         pyautogui.click()
    #         time.sleep(2)
    #
    # time.sleep(3)
    #
    # try:
    #     if get_position('rwzhong') is not None:
    #         pyautogui.moveTo(get_position('rwzhong'))
    #         pyautogui.click()
    #         time.sleep(2)
    #         pyautogui.moveTo(1438, 910)  # 领取
    #         pyautogui.click()
    #         time.sleep(2)
    # except pyautogui.ImageNotFoundException:
    #         pyautogui.moveTo(1438, 910)  # 领取
    #         pyautogui.click()
    #         time.sleep(2)

