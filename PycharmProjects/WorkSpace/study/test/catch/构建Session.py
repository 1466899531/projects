import json

import requests
data = {
    "username":"谢焕星-货主端",
     "password":"111111"
        }
headers = {
    "Content-Type": "application/json;charset=UTF-8"
}
# 登录url
loginUrl = 'http://test-web-consignor.ubor56.com/api/login'
# 构建会话
session = requests.session()
responseLogin = session.post(loginUrl,json=data,headers=headers)
print(responseLogin.text)
data = {}
loginInfoUrl = 'http://test-web-consignor.ubor56.com/api/rgt/rgtOwner/findOwnerLoginInfo'
responseLoginInfo =session.post(loginInfoUrl,json=data,headers=headers)
print(responseLoginInfo.text)
session.close()
