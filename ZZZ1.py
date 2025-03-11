# import ZZZGetpositionfish
# import time  #pythonproject
# import pyautogui
# import keyboard
# from pyautogui import leftClick
# from pynput.keyboard import Controller, Key
# keyboard = Controller()
# import ZZZKO
# import pynput
# import threading
# from PIL import Image
# import pytesseract
# from sympy import print_glsl
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR'
# access_attempts=2
# import ZZZGetposition
# import ZZZGetpositionfishD
# import ZZZGetpositionfishA
# def get_position(word):
#     up_left = None
#     while up_left == None:
#         up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format(word),confidence=0.85)
#     return up_left
# def hold_key(key, duration):
#     controller = Controller()
#     controller.press(key)    # 按下
#     time.sleep(duration)     # 保持
#     controller.release(key)  # 释放
# x=0
# while True:
#         time.sleep(8)
#         hold_key('e',2)
#         time.sleep(2)
#         hold_key('j',3)
#         time.sleep(2)
#         hold_key(Key.space,0.5)
#         time.sleep(2)
#         hold_key('e',2)
#         time.sleep(2)
#         hold_key('e', 2)
#         time.sleep(1)
#         hold_key('c',0.5)
#         time.sleep(2)
#         hold_key('j',3)
#         time.sleep(3)
#         hold_key(Key.space, 0.5)
#         time.sleep(2)
#         hold_key('j', 3)
#         global  x
#         while x<1 :
#             hold_key('j', 0.2)
#
#
#         while True:
#             try:
#                 if get_position('again') is not None:
#                     pyautogui.click(get_position('again'))
#                     x=3
#                     print('找到再来一次')
#
#                     break
#             except pyautogui.ImageNotFoundException:
#
#                     print('无法找到')
#                     time.sleep(0.5)
#         while True:
#
#                if get_position('queding') is not None:
#                     # pyautogui.click(get_position('queding'))
#
#                     break
import ZZZKO
import time
import pyautogui
import threading
from pynput.keyboard import Controller, Key
import ZZZGetposition
# 初始化全局控制变量
running = True
x = 0  # 初始化全局变量
keyboard = Controller()
time.sleep(1.8)
keyboard.press(Key.f2)
time.sleep(1.8)
pyautogui.click(1173,146)
time.sleep(1.8)
pyautogui.click(1474,437)
time.sleep(1.8)
ZZZKO.queding()
time.sleep(3)
keyboard.press(Key.esc)
time.sleep(1.8)
pyautogui.click(1439,510)
time.sleep(1.8)
pyautogui.click(1290,825)
time.sleep(2)
pyautogui.click(1721,1027)
time.sleep(2)
pyautogui.click(1721,1027)
time.sleep(1)
# ================ 图像检测模块 ================
def image_detector():
    """独立线程：持续检测游戏画面中的按钮"""
    global running, x

    def get_position_nonblock(word):
        """非阻塞式获取图片位置"""
        try:
            return pyautogui.locateCenterOnScreen(
                f'C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{word}.png',
                confidence=0.85
            )
        except pyautogui.ImageNotFoundException:
            return None
    a=0
    while a<2:  # 修改为检测两次后停止
        # 检测"again"按钮
        again_pos = get_position_nonblock('again')
        if again_pos:
            pyautogui.click(again_pos)
            a += 1  # 修复递增操作符
            x = 3
            print(f'[系统] 检测到再来一次按钮，当前次数：{a}')

        # 检测"queding"按钮（可根据需要添加更多按钮）
        queding_pos = get_position_nonblock('queding')
        if queding_pos:
            pyautogui.click(queding_pos)
            print('[系统] 检测到确定按钮')

        time.sleep(0.3)  # 降低CPU占用

    # 检测到两次后停止所有线程
    running = False
    print('[系统] 已检测到两次"again"，正在停止所有线程...')

# ================ 按键操作模块 ================
def key_operations():
    """独立线程：执行预设按键序列"""
    global running
    while True:
        try:
            if ZZZGetposition.get_position('ZZ') is not None:
                def hold_key(key, duration):
                    keyboard.press(key)
                    time.sleep(duration)
                    keyboard.release(key)
                print('[系统] 检测到ZZ')
                time.sleep(1)
                hold_key(Key.space, 0.5)
                time.sleep(1)
                hold_key('s', 0.5)
                time.sleep(1)
                hold_key('e', 0.5)
                time.sleep(1)
                hold_key(Key.space, 0.5)
                time.sleep(1)
                hold_key('e', 0.5)
                time.sleep(1.893)

                hold_key('j', 0.5)
                time.sleep(1.893)
                hold_key('j', 0.5)
                time.sleep(1.893)
                hold_key('j', 0.5)
                time.sleep(1.893)
                i=0
                # 第二阶段循环操作（示例）
                while i<20:
                    hold_key('j', 0.1)
                    time.sleep(0.1)
                    i=i+1
        except pyautogui.ImageNotFoundException:
            print('未找到')
            time.sleep(0.5)

# ================ 主控制模块 ================
def main():
    global running

    # 启动检测线程
    detector_thread = threading.Thread(target=image_detector)
    detector_thread.daemon = True  # 设为守护线程

    # 启动操作线程
    operator_thread = threading.Thread(target=key_operations)
    operator_thread.daemon = True

    try:
        detector_thread.start()
        operator_thread.start()
        print('[系统] 所有线程已启动，按CTRL+C停止')

        # 保持主线程运行
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        running = False
        print('[系统] 正在停止所有线程...')
        detector_thread.join(timeout=1)
        operator_thread.join(timeout=1)
        print('[系统] 已安全退出')


if __name__ == "__main__":
    main()

