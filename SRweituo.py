import time#pythonproject
import pyautogui
import time


import keyboard
import Getposition
# def SR_weituo():
#     while 1:
#         try:
#             if Getposition.get_position('weituo') is not None:
#                 pyautogui.moveTo(Getposition.get_position('weituo'))
#                 pyautogui.click()
#
#                 time.sleep(1)
#                 break
#         except pyautogui.ImageNotFoundException:
#             pyautogui.press('esc')
#             print('未找到委托。。。')
#             time.sleep(2)
#
#
#     time.sleep(1)
#     pyautogui.moveTo(431, 907)#一键领取1
#     pyautogui.click()
#     time.sleep(1)
#     pyautogui.moveTo(1121, 963)#再次委托
#     pyautogui.click()
#     time.sleep(2)
#     pyautogui.click()
#     pyautogui.press('esc')
import time
import pyautogui
import keyboard
from Getposition import get_position  # 假设自定义模块

# 坐标配置（示例值）
CONFIG = {
    "claim_reward": (431, 907),
    "reassign": (1121, 963),
    "max_retries": 5
}


def SR_weituo():
    retries = 0

    while retries < CONFIG['max_retries']:
        try:
            if (pos := get_position('weituo')) is not None:
                pyautogui.click(pos)
                time.sleep(1)
                break

        except pyautogui.ImageNotFoundException:
            print("未找到委托，尝试重试...")
            pyautogui.press('esc')
            retries += 1
            time.sleep(2)

    if retries >= CONFIG['max_retries']:
        print("达到最大重试次数，中止操作")
        return

    try:
        # 一键领取
        pyautogui.click(CONFIG['claim_reward'])
        time.sleep(1)

        # 再次委托
        pyautogui.doubleClick(CONFIG['reassign'], interval=0.5)
        time.sleep(2)

    except Exception as e:
        print(f"操作执行失败: {str(e)}")

    finally:
        keyboard.press('esc')


