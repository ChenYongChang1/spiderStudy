import requests
import pprint
#
# response = requests.get('http://httpbin.org/get')
# print(response.status_code,response.reason)
# # print(response.text)
#
# response = requests.post('http://httpbin.org/post',data={'a':'1'})
# # pprint.pprint(response.json())
#
# # basic-auth认证
# r = requests.get('http://httpbin.org/basic-auth/guye/123456',auth=('guye','123456'))
# # print(r.json())
#
# s = requests.Session()
# # session保存服务器信息  下次请求自动将这个网站的信息自动添加到请求头
# s.get('http://httpbin.org/cookies/set/userid/123456789')
# s.get('http://httpbin.org/cookies/set/token/xxxxxxx')
# r = s.get('http://httpbin.org/cookies')
# print(r.json())

# 在requests中使用代理
# print('不适用代理:',requests.get('http://httpbin.org/ip',timeout = 5).json())

print('适用代理:',requests.get('http://httpbin.org/ip',proxies = {'http':'http://106.14.212.56:41801'}).json())

# print('过期时间:',requests.get('http://httpbin.org/delay/4',timeout = 5).json())