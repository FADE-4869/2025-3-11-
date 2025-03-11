import os
import subprocess
import platform

def kill_process_by_name(process_name):
    """使用系统命令强制终止进程（仅支持Windows系统）
    
    Args:
        process_name: 目标进程名称（不含.exe后缀）
    """
    if platform.system() != 'Windows':
        raise OSError("This function only supports Windows operating system")
    
    if not isinstance(process_name, str) or not process_name.isidentifier():
        raise ValueError("Invalid process name format")
    
    try:
        completed = subprocess.run(
            ['taskkill', '/f', '/im', f'{process_name}.exe'],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Successfully terminated {process_name}.exe")
    except subprocess.CalledProcessError as e:
        if "not found" in e.stderr:
            print(f"Process {process_name}.exe not running")
        else:
            print(f"Failed to terminate process: {e.stderr}")

if __name__ == '__main__':
    # 在程序退出前调用（如main函数末尾）
    kill_process_by_name('StarRail')  # 替换为实际需要关闭的exe名称
