import requests
''' 
    查询区县编码
'''
def wuliuDeliveryServlet():
    url = 'http://222.133.28.202:18094/servlet/wuliuDeliveryServlet'
    header = {'Content-Type': "application/json"}
    data = {
        "dataInfo":{
        "brokerPeople":"山东物泊经纪人1","deliveryTime":"2020-02-25 11:37:17","carNum":"鲁E12345","deliveryId":10000737,"dependId":"464459","dependNum":"464459","driverName":"陈小凤","idCard":"44088219900725374X","mobile":"13917280001"}
    }
    res = requests.post(url, json=data, headers=header)
    print(res.status_code)
    print(res.text)
wuliuDeliveryServlet()