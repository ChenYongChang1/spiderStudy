#官网链接: http://docs.python-requests.org/en/master/user/advanced/#proxies

#代理设置:先发送请求给代理,然后由代理帮忙发送(封ip是常见的事情)

# 代理
# proxies=proxies

import requests
proxies={
    'http':'http://egon:123@localhost:9743',#带用户名密码的代理,@符号前是用户名与密码
    'http':'http://localhost:9743',
    'https':'https://localhost:9743',
}
respone=requests.get('https://www.12306.cn',
                     proxies=proxies)

print(respone.status_code)



#支持socks代理,安装:pip install requests[socks]
import requests
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
respone=requests.get('https://www.12306.cn',
                     proxies=proxies)

print(respone.status_code)