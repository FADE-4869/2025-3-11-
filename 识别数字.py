import pyautogui
import time
import pyautogui
from PIL import Image
import pytesseract
import cv2
import re# 将截图保存为临时文件
screenshot = pyautogui.screenshot(region=(1468,51,100,34))  # x, y, width, height
screenshot_path = 'C:\\Users\\DELL\\PycharmProjects\\AUTO\\resource\\screenshot.png'
screenshot.save(screenshot_path)
image =cv2.imread(screenshot_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_image)
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
cv2.imshow("gray_image",gray_image2)
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
cv2.imshow("gray_image",gray_image3)
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
