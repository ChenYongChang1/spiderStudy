import requests
from lxml import etree

# 自己定制headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
}
# url = 'https://www.cnblogs.com/linhaifeng/'
# 目录
url = 'https://recomm.cnblogs.com/api/v2/recomm/blogpost/reco'

data = {"itemId": 7278389, "itemTitle": "Python开发之路"}

r = requests.post(url, headers=headers,data=data)

print(r)
