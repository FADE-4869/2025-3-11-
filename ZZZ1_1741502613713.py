import threading
from pathlib import Path
import keyboard
import time
import pyautogui
import threading
from pynput.keyboard import Controller, Key
import ZZZGetposition
# 使用事件对象替代全局变量
detector_stop_event = threading.Event()
program_stop_event = threading.Event()

def image_detector():
    """独立线程：持续检测游戏画面中的按钮"""
    # 使用 pathlib 处理路径
    resource_path = Path('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ')
    
    # 常量定义（添加类型注解）
    CONFIDENCE: float = 0.85
    CHECK_INTERVAL: float = 0.3
    MAX_RETRIES: int = 2  # 符合两次需求

    def get_position_nonblock(word: str) -> tuple:
        """非阻塞式获取图片位置（添加参数校验）"""
        if not (resource_path / f"{word}.png").exists():
            print(f'[错误] 缺失资源文件: {word}.png')
            return None
            
        try:
            return pyautogui.locateCenterOnScreen(
                str(resource_path / f"{word}.png"),
                confidence=CONFIDENCE
            )
        except pyautogui.ImageNotFoundException:
            return None
        except Exception as e:
            print(f'[警告] 图像识别异常: {str(e)}')
            return None

    retry_count = 0
    while not detector_stop_event.is_set() and retry_count < MAX_RETRIES:
        # 添加坐标有效性校验
        if (again_pos := get_position_nonblock('again')) and all(again_pos):
            pyautogui.click(again_pos)
            retry_count += 1
            print(f'[系统] 检测到再来一次按钮（{retry_count}/{MAX_RETRIES}）')
            # 使用原子操作更新状态
            threading.current_thread().x = 3

        if (queding_pos := get_position_nonblock('queding')) and all(queding_pos):
            pyautogui.click(queding_pos)
            print('[系统] 检测到确定按钮')

        time.sleep(CHECK_INTERVAL)

    print('[系统] 已达到最大重试次数，终止检测线程')
    detector_stop_event.set()

def hold_key(key, duration: float):
    """提取重复操作逻辑"""
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def key_operations():
    """独立线程：执行预设按键序列"""
    while not program_stop_event.is_set():
        try:
            if ZZZGetposition.get_position('ZZ') is not None:
                print('[系统] 检测到ZZ')
                time.sleep(1)
                
                # 使用元组存储操作序列
                key_sequence = (
                    (Key.space, 0.5), ('e', 0.5), (Key.space, 0.5),
                    (Key.space, 0.8), ('e', 0.5), (1.893, None),
                    *((('j', 0.5), 1.893) for _ in range(3)),
                    *((('j', 0.1), 0.1) for _ in range(20))
                )

                for item in key_sequence:
                    if program_stop_event.is_set():
                        return
                    if isinstance(item[0], (str, Key)):  # 按键操作
                        hold_key(item[0], item[1])
                    else:  # 休眠操作
                        time.sleep(item[0])
        except pyautogui.ImageNotFoundException:
            print('未找到')
            time.sleep(0.5)

def main():
    # 初始化事件状态
    detector_stop_event.clear()
    program_stop_event.clear()

    detector_thread = threading.Thread(target=image_detector)
    operator_thread = threading.Thread(target=key_operations)

    try:
        detector_thread.start()
        operator_thread.start()
        print('[系统] 所有线程已启动，按CTRL+C停止')

        while detector_thread.is_alive():
            time.sleep(0.5)

    except KeyboardInterrupt:
        print('[系统] 正在停止所有线程...')
        program_stop_event.set()
        detector_stop_event.set()
        
        # 添加安全终止检查
        detector_thread.join(timeout=2)
        operator_thread.join(timeout=2)
        if detector_thread.is_alive() or operator_thread.is_alive():
            print('[警告] 部分线程未正常终止')
        print('[系统] 已安全退出')
