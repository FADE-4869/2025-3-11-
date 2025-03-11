import pyautogui
def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format(word),
                                                 confidence=0.8,region=(1437,784,338,220))
    return up_left