#证书验证(大部分网站都是https)

# 不验证证书

# verify=False
#改进2:去掉报错,并且去掉警报信息
# import urllib3
# urllib3.disable_warnings() #关闭警告

# import requests
# respone=requests.get('https://www.12306.cn') #如果是ssl请求,首先检查证书是否合法,不合法则报错,程序终端
#
#
# #改进1:去掉报错,但是会报警告
# import requests
# respone=requests.get('https://www.12306.cn',verify=False) #不验证证书,报警告,返回200
# print(respone.status_code)


#改进2:去掉报错,并且去掉警报信息
import requests
import urllib3

urllib3.disable_warnings() #关闭警告
respone=requests.get('https://www.12306.cn',verify=False)
print(respone)

#改进3:加上证书
#很多网站都是https,但是不用证书也可以访问,大多数情况都是可以携带也可以不携带证书
#知乎\百度等都是可带可不带
#有硬性要求的,则必须带，比如对于定向的用户,拿到证书后才有权限访问某个特定网站
# import requests
# respone=requests.get('https://www.12306.cn',
#                      cert=('/path/server.crt',
#                            '/path/key'))
# print(respone.status_code)