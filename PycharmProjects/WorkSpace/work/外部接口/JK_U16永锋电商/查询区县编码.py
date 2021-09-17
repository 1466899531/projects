import requests
''' 
    查询区县编码
'''
def query():
    url = 'http://116.228.222.130:28082/areaCode/query'
    header = {'Content-Type': "application/json"}
    data = {
        "keyValue":"市辖区",
        "fatherKeyValue":"天津"
    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
query()