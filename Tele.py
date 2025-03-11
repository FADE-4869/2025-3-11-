from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# 填入你的 api_id 和 api_hash
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
channel_username = 'sakurahaven'  # 频道用户名（不带 @）

# 创建客户端并连接
with TelegramClient('session_name', api_id, api_hash) as client:
    # 获取频道实体
    channel = client.get_entity(channel_username)

    # 获取历史消息（最多一次性获取 100 条）
    messages = client(GetHistoryRequest(
        peer=channel,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    # 输出消息内容
    for msg in messages.messages:
        print(f"{msg.date}: {msg.message}")