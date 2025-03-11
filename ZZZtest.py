import time  #pythonproject
import pyautogui
from pynput.keyboard import Controller, Key
keyboard = Controller()
import ZZZKO
import subprocess
access_attempts=2
import ZZZbook
def hold_key(key, duration):
    controller = Controller()
    controller.press(key)    # 按下
    time.sleep(duration)     # 保持
    controller.release(key)  # 释放

# 正确调用方式（注意要用 Key.esc）


def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format(word),confidence=0.85)
    return up_left
time.sleep(3)
# pyautogui.moveTo(get_position('MHY2'))
# pyautogui.doubleClick()
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


# 应用程序的完整路径
app_path = r"D:\miHoYo Launcher\games\ZenlessZoneZero Game\ZenlessZoneZero.exe"

# 或非阻塞式（不等待程序结束）
subprocess.Popen(app_path)

time.sleep(14)
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
            num=num+1
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

time.sleep(10)

ZZZbook.ZZZ_book()
time.sleep(1.5)
pyautogui.moveTo(966,834)
pyautogui.click()
time.sleep(1.5)
pyautogui.moveTo(1126,634)
pyautogui.click()
time.sleep(2)
x=0
while x<5:
        try:
            if get_position('daindan') is not None:
                pyautogui.moveTo(get_position('daindan'))
                print('找到')
                pyautogui.doubleClick()
                time.sleep(1)
                pyautogui.doubleClick()
                break
        except pyautogui.ImageNotFoundException:
            x=x+1
            print('无法找到')
            time.sleep(1)
# pyautogui.moveTo(get_position('daindan'))
# pyautogui.click()
# time.sleep(1.2)
# # pyautogui.moveTo(get_position('queding'))
# pyautogui.click()

ZZZKO.queding()

while True:
    try:
        if get_position('zhu') is not None:
            print('回到主页面')
            break
    except pyautogui.ImageNotFoundException:
        hold_key(Key.esc, 0.5)

        print('未找到主页面')

        time.sleep(1)
# -----------------------------------------------------------------------

time.sleep(1)
ZZZbook.ZZZ_book()
print("f2")
time.sleep(1.5)
pyautogui.click(pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/qianwang.png',
                                                 confidence=0.85,region=(844,802,246,72)))


time.sleep(1)
ZZZKO.queding()
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(136,945)
pyautogui.click()


pyautogui.moveTo(804,544)
# 向右移动（正弦波实现平滑）
pyautogui.click()
pyautogui.mouseDown(button="left")

pyautogui.moveRel(317, 0, duration=1,tween=pyautogui.easeInOutQuad)
pyautogui.moveRel(-305, 41, duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.moveRel(317, 0,duration=1, tween=pyautogui.easeInOutQuad)
pyautogui.moveRel(-305, 41, duration=1, tween=pyautogui.easeInOutQuad)

pyautogui.mouseUp(button="left")
time.sleep(1)
ZZZKO.queding()
time.sleep(0.5)
pyautogui.doubleClick(1396,521)
time.sleep(1)
while True:
    try:
        if get_position('zhu') is not None:
            print('回到主页面')
            break
    except pyautogui.ImageNotFoundException:
        keyboard.press(Key.esc)
        print('未找到主页面')

        time.sleep(0.2)


# -----------------------------------------------------------------------
time.sleep(5)
ZZZbook.ZZZ_book()
time.sleep(1.5)
pyautogui.moveTo(966,834)

time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/qianwang.png',
                                                 confidence=0.85,region=(844,802,246,72)))
ZZZKO.queding()
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(136,945)
pyautogui.click()
time.sleep(1)

pyautogui.click()
pyautogui.moveTo(903,753)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1683,1028)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1183,753)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1414,1022)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1666,976)
pyautogui.click()
time.sleep(1)
ZZZKO.queding()
pyautogui.click()
time.sleep(2)
while True:
    try:
        if get_position('zhu') is not None:
            print('回到主页面')
            break
    except pyautogui.ImageNotFoundException:
        hold_key(Key.esc, 0.5)

        print('未找到主页面')

        time.sleep(0.5)

time.sleep(3)
while True:
    try:
        if get_position('book') is not None:
            print('回到手册面')
            break
    except pyautogui.ImageNotFoundException:
        hold_key(Key.f2, 0.5)

        print('未找到手册面')

        time.sleep(1)
time.sleep(1.5)
pyautogui.moveTo(979,139)
pyautogui.click()
time.sleep(1.5)
pyautogui.moveTo(846,270)
pyautogui.click()
time.sleep(1)
ZZZKO.queding()
pyautogui.click()
time.sleep(1)
while True:
    try:
        if get_position('zhu') is not None:
            print('回到主页面')
            break
    except pyautogui.ImageNotFoundException:
        hold_key(Key.esc, 0.5)

        print('未找到主页面')

        time.sleep(1)
# ---------------------------------------------------------------------
time.sleep(4)
keyboard.press('i')
time.sleep(2)
pyautogui.moveTo(1495,49)
pyautogui.click()
time.sleep(1.2)
pyautogui.moveTo(1721,1027)
pyautogui.click()
time.sleep(1.3)
pyautogui.moveTo(1260,53)
pyautogui.click()
time.sleep(1.3)
pyautogui.moveTo(1363,1029)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(get_position('return'))
pyautogui.click()
time.sleep(2)
# Kill_SR.kill_process_by_name('ZenlessZoneZero')