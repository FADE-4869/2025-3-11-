import cv2
import pyautogui
from PIL import Image
import pytesseract
screenshot = pyautogui.screenshot(region=(1461,51, 280,26))  # x, y, width, height
import cv2
# 将截图保存为临时文件
screenshot_path = 'C:\\Users\\DELL\\PycharmProjects\\AUTO\\resource\\screenshot.png'
screenshot.save(screenshot_path)
# 读取图像
image = cv2.imread(screenshot_path)

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_image)
cv2.waitKey(0)
# 应用高斯模糊进行去噪
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# 二值化处理
_, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 保存处理后的图像
cv2.imwrite('processed_document.jpg', binary_image)
