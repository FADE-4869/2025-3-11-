import requests
from bs4 import BeautifulSoup
import csv

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

data = []
for page in range(0, 250, 25):
    response = requests.get(f'{url}?start={page}', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    for item in soup.select('.item'):
        title = item.select_one('.title').get_text(strip=True)
        rating = item.select_one('.rating_num').get_text()
        link = item.a['href']
        year = item.select_one('.bd p').text.split('/')[-1].strip()

        data.append([title, rating, year, link])

# 保存到CSV
with open('douban_top250.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Rating', 'Year', 'Link'])
    writer.writerows(data)