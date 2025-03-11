import threading
import pyautogui
import time
# 方法1：通过函数创建
def task():
    while True:
        if pyautogui.locateOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/zhandou.png', confidence=0.9,
                                    region=(54, 9, 90, 29)):
            pyautogui.press('v')
        else:
            time.sleep(1)

t = threading.Thread(target=task)
t.start()

# 方法2：继承 Thread 类
class MyThread(threading.Thread):
    def run(self):
        print("子线程执行")

t = MyThread()
t.start()