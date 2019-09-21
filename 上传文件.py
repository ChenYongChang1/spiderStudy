# -*- coding:utf8 -*-

import requests
files={'file':open('证书.py','rb')}
respone=requests.post('http://httpbin.org/post',files=files)

print(respone.json())