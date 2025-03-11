import time#pythonproject
import pyautogui
from PIL import Image
import pytesseract
import cv2
import re
import SRday
import SRweituo
import SRwuming
import SRqianzhen
import pyautogui
import Kill_SR
pyautogui.FAILSAFE = False  # 在代码开头添加

from sympy import print_glsl
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Programs\Tesseract-OCR'
access_attempts=2
def get_position(word):
    up_left = None
    while up_left == None:
        up_left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/{}.png'.format(word),confidence=0.85)
    return up_left
# pyautogui.moveTo(get_position('MHY2'))
# pyautogui.doubleClick()
# time.sleep(2)
# p=0
# while True:
#         try:
#             if get_position('srmunu') is not None:
#                 pyautogui.moveTo(get_position('srmunu'))
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
# time.sleep(6)
import subprocess

# 应用程序的完整路径
app_path = r"D:\miHoYo Launcher\games\Star Rail Game\StarRail.exe"

# 或非阻塞式（不等待程序结束）
subprocess.Popen(app_path)
num=0
while num<10:
        try:
            if pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/{}.png'.format('using'),confidence=0.9) is not None:
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
                    pyautogui.moveTo(get_position('SRstart'))
                    pyautogui.click()
                    break
            else:
                    print("Image not found on the screen.")


        except pyautogui.ImageNotFoundException:
            time.sleep(2)
            num=num+2
            print("Imag not found ovn the screen. (Caught ImageNotFoundException)")




while True:
    try:
        if get_position('djjr') is not None:
            print('已经找到图片')
            pyautogui.click()

            break
    except pyautogui.ImageNotFoundException:

        print('未找到点击开始')

        time.sleep(0.1)

t=0
while t<8:
    try:
        if get_position('yueka') is not None:
            pyautogui.moveTo(get_position('yueka'))
            print('已经找到月卡')
            pyautogui.click()
            pyautogui.moveRel(200, 0, duration=1)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()

            break
    except pyautogui.ImageNotFoundException:

        print('未找到月卡')
        t=t+1
        time.sleep(1)


while True:
    try:
        if get_position('rwl') is not None:
            print('已经找到任务栏')


            break
    except pyautogui.ImageNotFoundException:
        pyautogui.press('F4')
        print('未找到任务栏')
        time.sleep(2)




time.sleep(1)
num=0
while True:
   try:
       if get_position('moni') is not None:
        pyautogui.moveTo(get_position('moni'))
        time.sleep(0.5)
        pyautogui.doubleClick()
        time.sleep(2)
        break


   except pyautogui.ImageNotFoundException:

        print('未找到模拟宇宙按键1')

        break



screenshot = pyautogui.screenshot(region=(1468,51,100,34))  # x, y, width, height
screenshot_path = 'C:\\Users\\DELL\\PycharmProjects\\AUTO\\resource\\screenshot.png'
screenshot.save(screenshot_path)
image =cv2.imread(screenshot_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray_image",gray_image)
cv2.waitKey(0)
text = pytesseract.image_to_string(gray_image, config='--oem 3 --psm 6')# 注意：'--oem 3' 表示使用LSTM OCR引擎，'--psm 6' 表示假设图像是一个单一的统一块文本。
numbers = re.findall(r'\b\d+\b', text)
print(numbers)
# 由于text可能包含非数字字符，你可能需要进一步处理它
# 例如，使用正则表达式提取所有数字

screenshot2 = pyautogui.screenshot(region=(1674,51,66,34))  # x, y, width, height
screenshot_path2 = 'C:\\Users\\DELL\\PycharmProjects\\AUTO\\resource\\screenshot2.png'
screenshot2.save(screenshot_path2)
image2 =cv2.imread(screenshot_path2)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray_image",gray_image2)
cv2.waitKey(0)
text2 = pytesseract.image_to_string(gray_image2, config='--oem 3 --psm 6')# 注意：'--oem 3' 表示使用LSTM OCR引擎，'--psm 6' 表示假设图像是一个单一的统一块文本。
numbers2 = re.findall(r'\b\d+\b', text2)
print(numbers2)
## 打印提取的数字
screenshot3 = pyautogui.screenshot(region=(1338,52,77,27))  # x, y, width, height
screenshot_path3 = 'C:\\Users\\DELL\\PycharmProjects\\AUTO\\resource\\screenshot3.png'
screenshot3.save(screenshot_path3)
image3 =cv2.imread(screenshot_path3)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray_image",gray_image3)
cv2.waitKey(0)
text3 = pytesseract.image_to_string(gray_image3, config='--oem 3 --psm 6')# 注意：'--oem 3' 表示使用LSTM OCR引擎，'--psm 6' 表示假设图像是一个单一的统一块文本。
numbers3 = re.findall(r'\b\d+\b', text3)
print(numbers2)
int_num1=int(numbers3[0])
int_num=int(numbers[0])
int_NUM=int(numbers2[0])
target_finds =int( int_num/40)

The_target_finds =  target_finds +int_NUM-1
print(f"共有 {int_num1 }额外开括力")
print(f"共有 {int_num }开括力")
print(f"共有 {int_NUM }沉浸器")

print("有{:d}次".format(target_finds))#转化后的沉浸器
print( The_target_finds) #点击次数

if  target_finds>0:
    time.sleep(1)
    pyautogui.moveTo(407,353) #培养
    time.sleep(1)
    pyautogui.moveTo(1543, 408)#传送流萤副本
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.moveTo(1740,899)#最大
    time.sleep(1)
    pyautogui.click()
    # time.sleep(2.5)
    # pyautogui.moveTo(353, 637)#好友人物
    # pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1617, 989)#开始挑战
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1.5)
    pyautogui.doubleClick()
    time.sleep(3.5)

    while True:
        try:
            if pyautogui.locateOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/zhandou.png', confidence=0.85,region=(54, 9, 90, 29)) is not None:
                pyautogui.press('v')
                break


        except pyautogui.ImageNotFoundException:

            print('未找到模拟宇宙按键1')

            break

    # pyautogui.doubleClick()
    # pyautogui.press('e')
    # time.sleep(1.5)
    # pyautogui.press('2')
    # time.sleep(1.2)
    # pyautogui.press('e')
    # time.sleep(1.2)
    # pyautogui.press('4')
    # time.sleep(1.3)
    # pyautogui.press('e')
    # time.sleep(1.2)
    # pyautogui.keyDown('w')
    # time.sleep(2)
    # pyautogui.keyUp('w')
    # time.sleep(0.5)
    # pyautogui.press('e')
    # time.sleep(3)
    #
    # time.sleep(2)
    # pyautogui.press('v')
    # time.sleep(2)



    # 寻找指定数量的"again"图片
    max_attempts = 1000
    attempts = 0
    center_finds = 0
    while center_finds < The_target_finds:
        try:
            center = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/again.png', confidence=0.9)
            if center:
                pyautogui.click(center)
                time.sleep(2)
                print('图片 "again" 已找到并点击')
                center_finds += 1  # 增加找到center的次数
        except pyautogui.ImageNotFoundException:
            # 如果没有找到图片，增加尝试次数并等待
            time.sleep(1)
            print('未找到图片again，正在重试...')
            attempts += 1

    time.sleep(4)

    attempts = 0  # 重置尝试次数，因为我们现在开始寻找新的图片
    while attempts < max_attempts:
        try:
            left = pyautogui.locateCenterOnScreen('C:/Users/DELL/PycharmProjects/AUTO/resource/SR/tuichu.png', confidence=0.9)
            if left:
                pyautogui.click(left)

                print('图片 "tuichu" 已找到并点击，达到目标次数，退出循环')
                break  # 退出内层循环
        except pyautogui.ImageNotFoundException:
            # 如果没有找到图片，增加尝试次数并等待
            print('未找到图片tuichu，正在重试...')
            time.sleep(1)
            attempts += 1

    # 如果在内层循环中找到了"tuichu"图片，则跳出外层循环（如果需要的话）
      # 这里假设找到"tuichu"图片后就不需要继续执行了

    # 如果因为达到最大尝试次数而退出循环，则打印一条消息
    if attempts == max_attempts and center_finds < target_finds:
        print(f'达到最大尝试次数 {max_attempts}，但未能在找到足够多的 "again" 图片。')

pyautogui.press('esc')
time.sleep(5)

#----------------------------------------------------------好友赠礼--------------------------------------------------------------------#
SRqianzhen.SRaward()
#-------------------------------------------------------------委托------------------------------------------------------------------------------------#

SRweituo.SR_weituo()

#----------------------------------------------------无名勋章----------------------------------------------------------#

SRwuming.WUMING()

# ---------------------------------------------------------------指南--------------------------------------------------------------------
SRday.Daily_Reward()

#--------------------------------------------------------------------关闭程序----------------------------------------------------------------------#
Kill_SR.kill_process_by_name('StarRail')