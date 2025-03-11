import requests
import pandas as pd
import time
from datetime import datetime


# 定义获取K线数据的函数
def fetch_binance_klines(symbol, interval, start_time=None, end_time=None, limit=1000):
    base_url = ""
    params = {
        "symbol": symbol,  # 交易对，如BTCUSDT
        "interval": interval,  # 时间间隔（1m, 5m, 1h, 1d等）
        "limit": limit  # 单次请求最多获取的数据条数
    }

    # 添加时间范围参数（可选）
    if start_time:
        params["startTime"] = int(start_time.timestamp() * 1000)
    if end_time:
        params["endTime"] = int(end_time.timestamp() * 1000)

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # 检查HTTP错误
        data = response.json()

        # 转换为DataFrame并处理列名
        columns = [
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_volume", "trades", "taker_buy_volume",
            "taker_buy_quote_volume", "ignore"
        ]
        df = pd.DataFrame(data, columns=columns, dtype=float)
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")  # 转换为时间戳

        return df[["timestamp", "open", "high", "low", "close", "volume"]]  # 选择关键列

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None


# 示例用法
if __name__ == "__main__":
    # 参数设置
    symbol = "BTCUSDT"  # 比特币对USDT
    interval = "1h"  # 1小时K线
    start_time = datetime(2023, 1, 1)  # 开始时间
    end_time = datetime(2023, 1, 2)  # 结束时间

    # 获取数据
    df = fetch_binance_klines(symbol, interval, start_time, end_time)

    if df is not None:
        # 保存为CSV
        df.to_csv(f"binance_{symbol}_{interval}_data.csv", index=False)
        print(f"数据已保存，共获取{len(df)}条记录")
        print(df.head())
    else:
        print("数据获取失败")