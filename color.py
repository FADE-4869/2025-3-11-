from PIL import Image
import pyautogui
import numpy as np

def locate_with_tolerance(image_path, region=None, tolerance=0):
    """
    在指定区域内查找图像，允许 RGB 颜色容差
    :param image_path: 目标图片路径
    :param region: 搜索区域 (x, y, width, height)
    :param tolerance: 允许的 RGB 各通道最大差异（0 表示严格匹配）
    :return: 匹配区域的中心坐标 (x, y) 或 None
    """
    # 加载目标图片
    reference = Image.open(image_path)
    ref_width, ref_height = reference.size
    ref_pixels = np.array(reference)

    # 截取屏幕区域
    if region:
        screen = pyautogui.screenshot(region=region)
        screen_pixels = np.array(screen)
        region_x, region_y = region[0], region[1]
    else:
        screen = pyautogui.screenshot()
        screen_pixels = np.array(screen)
        region_x, region_y = 0, 0

    # 遍历屏幕区域，寻找匹配位置
    for y in range(screen_pixels.shape[0] - ref_height + 1):
        for x in range(screen_pixels.shape[1] - ref_width + 1):
            # 提取当前窗口像素
            current_window = screen_pixels[y:y+ref_height, x:x+ref_width]
            # 计算颜色差异
            diff = np.abs(current_window - ref_pixels)
            # 判断所有像素是否在容差范围内
            if np.all(diff <= tolerance):
                center_x = region_x + x + ref_width // 2
                center_y = region_y + y + ref_height // 2
                return (center_x, center_y)
    return None