
import requests
from bs4 import BeautifulSoup
import os

def download_video(url):
    # 发送请求获取页面内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    content = response.text

    # 使用BeautifulSoup解析页面
    soup = BeautifulSoup(content, 'html.parser')
    video_url = 'https://www.bilibili.com/f0fcdc24-da10-4d43-8c80-56c267e36ebe'# 在这里填写视频标签的属性，例如：soup.find('video')['src']<video crossorigin="anonymous" preload="auto" src="blob:https://www.bilibili.com/f0fcdc24-da10-4d43-8c80-56c267e36ebe"></video>

    # 下载视频文件
    if video_url:
        video_response = requests.get(video_url, headers=headers)
        if video_response.status_code == 200:
            # 保存视频文件到当前目录下的 "videos" 文件夹中
            os.makedirs('videos', exist_ok=True)
            filename = os.path.join('videos', f'video_{os.getpid()}.mp4')
            with open(filename, 'wb') as file:
                file.write(video_response.content)
            print(f"视频已下载，保存路径为：{filename}")
        else:
            print("无法下载视频，状态码:", video_response.status_code)
    else:
        print("页面中未找到视频链接")

if __name__ == "__main__":
    # 替换为目标网站的URL
    target_url = 'https://www.bilibili.com/video/av113894110531350/?spm_id_from=333.1387.rich-text.link.click&vd_source=5ea6d663dcf9674e1e8169a76b77d384'  # 请替换为你想要爬取的网页URL
    download_video(target_url)