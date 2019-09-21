#认证设置:登陆网站是,弹出一个框,要求你输入用户名密码（与alter很类似），此时是无法获取html的
# 但本质原理是拼接成请求头发送
#         r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
# 一般的网站都不用默认的加密方式，都是自己写
# 那么我们就需要按照网站的加密方式，自己写一个类似于_basic_auth_str的方法
# 得到加密字符串后添加到请求头
#         r.headers['Authorization'] =func('.....')

#看一看默认的加密方式吧，通常网站都不会用默认的加密设置
import requests
# from requests.auth import HTTPBasicAuth
# r=requests.get('http://api.oa.tifang.online/homepage/login',auth=HTTPBasicAuth('17317628570','628570'))
# print(r.text)

#HTTPBasicAuth可以简写为如下格式
# import requests
r=requests.get('http://api.oa.tifang.online/homepage/login?loginID=17317628570&password=628570') #,auth=('user','password')
print(r.text)