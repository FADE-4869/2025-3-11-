import pyautogui
def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/ZZZ/{}.png'.format(word),
                                                 confidence=0.6,region=(1081,218,447,258))
    return up_left