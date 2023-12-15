# FILEPATH: /d:/vscodeworkspace/roi-calculator/test001.py

# test0013
import requests
from bs4 import BeautifulSoup
# 发送 HTTP 请求并获取响应
response = requests.get('https://www.baidu.com')

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(response.content, 'html.parser')

# 从 HTML 中提取所需的数据
data = soup.prettify()

# 将数据保存到文件中
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(data)
