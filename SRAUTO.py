import time
import pyautogui
import keyboard
from threading import Thread

# 全局控制变量
is_running = True
PAUSE_KEY = 'u'

def toggle_pause():  # ✅ 正确函数名
    """切换暂停状态"""
    global is_running
    is_running = not is_running
    state = "继续" if is_running else "暂停"
    print(f"程序已 {state}")


# 注册热键回调（修复函数名）
keyboard.add_hotkey(PAUSE_KEY, toggle_pause)  # ✅ 使用 toggle_pause


def main_loop():
    time.sleep(3)
    print(f"程序启动，按 {PAUSE_KEY} 切换暂停/继续")

    while True:
        if is_running:
            pyautogui.press('1')
            pyautogui.press('space')
            time.sleep(0.1)
        else:
            time.sleep(0.05)


if __name__ == "__main__":
    main_loop()