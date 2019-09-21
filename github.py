import requests
import re

#第一次请求
r1=requests.get('https://github.com/login')
r1_cookie=r1.cookies.get_dict() #拿到初始cookie(未被授权)
print(r1_cookie)
authenticity_token=re.findall(r'name="authenticity_token".*?value="(.*?)"',r1.text)[0] #从页面中拿到CSRF TOKEN
print(authenticity_token,'token')
#第二次请求：带着初始cookie和TOKEN发送POST请求给登录页面，带上账号密码
data={
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':authenticity_token,
    'login':'ChenYongChang1',
    'password':'ASD123QW@c'
}
r2=requests.post('https://github.com/session',
             data=data,
             cookies=r1_cookie
             )


login_cookie=r2.cookies.get_dict()


#第三次请求：以后的登录，拿着login_cookie就可以,比如访问一些个人配置
r3=requests.get('https://github.com/settings/emails',
                cookies=login_cookie)

# print(r3.text)
print('www.1759633997@qq.com' in r3.text) #True