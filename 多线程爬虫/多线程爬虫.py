import requests,threading
from lxml import etree
import parsel

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    response = requests.get(url,headers = headers)

    print(response.text)

url = 'https://www.doutula.com/article/list?page=1'
get_html(url)