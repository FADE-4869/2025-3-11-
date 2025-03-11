from pynput import keyboard
from time import perf_counter

# 全局状态记录
key_stats = {
    "first_press_time": None,    # 首次按键按下时间
    "last_press_time": None,     # 上次按键按下时间
    "key_down_times": {},        # 当前按下按键的时间记录
    "last_release_time": None,   # 上次按键释放时间
    "event_counter": 0           # 新增事件计数器
}

def get_key_name(key):
    """统一处理按键名称"""
    try:
        return key.char
    except AttributeError:
        return str(key).split(".")[-1].lower()

def print_event(event_type, key_name, message):
    """统一格式化输出事件"""
    key_stats["event_counter"] += 1
    print(f"{key_stats['event_counter']:>3}. [{event_type}] 按键: {key_name:<8} {message}")

def on_press(key):
    """处理按键按下事件"""
    current_time = perf_counter()
    key_name = get_key_name(key)

    # 记录首次按下时间
    if key_stats["first_press_time"] is None:
        key_stats["first_press_time"] = current_time

    # 记录当前按键按下时间
    key_stats["key_down_times"][key] = current_time

    # 计算按下间隔
    interval = current_time - key_stats["last_press_time"] if key_stats["last_press_time"] else 0.0

    # 更新最后按下时间
    key_stats["last_press_time"] = current_time

    # 格式化输出
    print_event("按下", key_name, f"| 距上次按下间隔: {interval:.3f}s")

def on_release(key):
    """处理按键释放事件"""
    current_time = perf_counter()
    key_name = get_key_name(key)

    # 计算持续时间
    duration = 0.0
    if key in key_stats["key_down_times"]:
        duration = current_time - key_stats["key_down_times"][key]
        del key_stats["key_down_times"][key]

    # 更新最后释放时间
    key_stats["last_release_time"] = current_time

    # 格式化输出
    print_event("释放", key_name, f"| 持续时长: {duration:.3f}s")

    # ESC键退出处理
    if key == keyboard.Key.esc:
        if key_stats["first_press_time"] and key_stats["last_release_time"]:
            total_duration = key_stats["last_release_time"] - key_stats["first_press_time"]
            print(f"\n总输入时长: {total_duration:.3f}秒 (从首次按下到末次释放)")
        print("程序已安全退出")
        return False

def main():
    print("带序号键盘监听器已启动（按ESC退出）")
    print("=" * 50)
    print("事件编号规则：")
    print("- 每个独立事件（按下/释放）都有唯一递增编号")
    print("- 编号从1开始连续计数\n")

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:

        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n用户中断操作")

if __name__ == "__main__":
    main()