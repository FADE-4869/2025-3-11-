from distutils.command.install import install

import pynput

from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if button == button.left and pressed:
        print(f"鼠标点击的坐标位置：{x}, {y}")


with Listener(on_click=on_click) as listener:
    listener.join()
