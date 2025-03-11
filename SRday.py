import time#pythonproject
import pyautogui
import time


import keyboard
import Getposition
import ctypes
# 通过内存写入直接修改游戏键位状态（需逆向分析）
import ctypes

def Daily_Reward():
    time.sleep(5)
    z=0
    while z<3:
        try:
            if Getposition.get_position('zhinan') is not None:
                pyautogui.moveTo(Getposition.get_position('zhinan'))
                pyautogui.click()
                time.sleep(1.8)
                pyautogui.moveTo(362, 213)
                pyautogui.click()
                break
        except pyautogui.ImageNotFoundException:
            pyautogui.press('esc')
            print("未找到指南。。。。")
            time.sleep(2)
            z=z+1

    time.sleep(3)
    try:
        i=0
        while i<6:
               try:
                    pyautogui.moveTo(Getposition.get_position('lingqu'))#点击领奖
                    pyautogui.click()
                    time.sleep(1)
               except pyautogui.ImageNotFoundException:
                    print('未发现领取按钮1')
                    time.sleep(1)
                    i=i+2
        pyautogui.moveTo(638, 303)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    except pyautogui.ImageNotFoundException:#未发现每日图像
        z = 0
        while z < 5:
            try:
                pyautogui.moveTo(Getposition.get_position('lingqu'))  # 点击领奖
                pyautogui.click()
                time.sleep(1.5)
            except pyautogui.ImageNotFoundException:
                print('未发现领取按钮2')
                time.sleep(1)
                z = z + 2
        pyautogui.moveTo(1123, 314)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    pyautogui.press('esc')
