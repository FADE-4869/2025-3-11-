import os

def kill_process_by_name(StarRail):
    """使用系统命令强制终止进程"""
    os.system(f'taskkill /f /im {'StarRail'}.exe')  # 示例：kill_process_by_name('notepad')
    
# 在程序退出前调用（如main函数末尾）
kill_process_by_name('StarRail')  # 替换为实际需要关闭的exe名称
