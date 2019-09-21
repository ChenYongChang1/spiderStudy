#超时设置
#两种超时:float or tuple
#timeout=0.1 #代表接收数据的超时时间
#timeout=(0.1,0.2)#0.1代表链接超时  0.2代表接收数据的超时时间

import requests

import urllib3
urllib3.disable_warnings() #关闭警告

respone=requests.get('https://www.baidu.com',
                     timeout=1,
                     verify=False)

print(respone.text)