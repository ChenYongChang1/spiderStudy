# -*- coding:utf8 -*-
import requests
import json

r = requests.get(
    'http://api.oa.tifang.online/homepage/login?loginID=17317628570&password=628570')  # ,auth=('user','password')
responseData = r.json()
TOKEN = responseData.get('data').get('loginToken')  # 存放验证token
# print(responseData.get('data').get('loginToken'))

url = 'http://api.oa.tifang.online/course/class/queryByPage'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    'tokenID': TOKEN,
    'Content-Type': 'application/json'
}
data = {"classCourseQueryDTO": {"name": "", "courseWay": "", "learningStage": "", "grade": "", "courseSubject": "",
                                "term": "", "inYear": '', "orderBys": ["desc,startAt"]}, "currentPage": 0,
        "pageSize": 10}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
