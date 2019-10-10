import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://www.meishij.net/'
r = requests.get(url)

HTML = etree.HTML(r.text)

links = HTML.xpath('//a[last()]/@href')
# links = HTML.xpath('//a[last()-1]/@href')
# links = HTML.xpath('//a[position()<3]/@href')
# links = HTML.xpath('//a[@class='aa']/@href')
# links = HTML.xpath('//a[contains(@class,'ff')]/@href')
for link in links:
    print(link)