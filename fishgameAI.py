import time
import pyautogui
from pynput.keyboard import Controller, Key
from ZZZGetpositionfish import get_position as get_fish_position
from ZZZGetposition import get_position

# 初始化键盘控制器
keyboard_controller = Controller()


def hold_key(key, duration):
    """按住指定键一段时间"""
    keyboard_controller.press(key)
    time.sleep(duration)
    keyboard_controller.release(key)


def press_key_based_on_image(image_name, key):
    """检测到指定图片时持续按住对应按键"""
    try:
        # 如果找到图片，持续按下按键
        if get_fish_position(image_name) is not None:
            print(f"按下 {key}")
            keyboard_controller.press(key)
            return True
    except pyautogui.ImageNotFoundException:
        # 图片未找到时释放按键
        keyboard_controller.release(key)
    return False


# 初始操作：等待3秒后按F键开始
time.sleep(3)
hold_key('f', 0.1)

# 寻找钓鱼触发点
while True:
    try:
        if get_position('wen') is not None:
            target_pos = get_position('Ffish')
            time.sleep(0.83)
            if target_pos:
                pyautogui.moveTo(target_pos)
                pyautogui.click()
                print("已启动钓鱼")
                break
    except pyautogui.ImageNotFoundException:
        time.sleep(0.1)

# 处理钓鱼小游戏中的操作
while True:
    try:
        # 检测是否需要操作方向键
        if get_fish_position('--') is not None:
            # 交替检测D和A键
            d_pressed = press_key_based_on_image('D', 'D')
            a_pressed = press_key_based_on_image('A', 'A')

            # 如果都没有按下，稍作等待
            if not d_pressed and not a_pressed:
                time.sleep(0.1)
        else:
            # 没有检测到提示时短暂等待
            time.sleep(0.5)
    except KeyboardInterrupt:
        # 允许用户通过Ctrl+C退出
        break
    except Exception as e:
        print(f"发生错误: {e}")
        time.sleep(1)

# 确保所有按键释放
keyboard_controller.release('D')
keyboard_controller.release('A')
print("程序结束")






