from bs4 import BeautifulSoup
import requests
from lxml import etree
url = 'https://www.meishij.net/'
r = requests.get(url)

# 创建beautifulsoup对象
soup = BeautifulSoup(r.text,'lxml')
# print(soup)
# print(soup.find_all('a').attrs['href'])

# print(soup.a.attrs['href'])
# print(list(soup.div.children))

# 去除所有文本
# soup.get_text()

# 支持css选择器
print(soup.select(".c"))

