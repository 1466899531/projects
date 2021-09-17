from common.base import BaseTest
from work.物泊56.平台端.平台端登录 import ManagerLogin

class PublishAudit(BaseTest):
    """ 参数初始化 """
    def __init__(self):
        self.feeFlag = 1    # 1收服务费 0不收服务费
        self.feeAmount = 0.01 # 服务费金额

    """ 平台端-委托承运货源审核管理数据查询 """
    def query_publishList(self,publishId):
        url = self.get_manager_url("/api/business/priceChange/publishList")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {
            "createdTime":[
                None,
                None
            ],
            "publishId":publishId,
            "page":0,
            "sizePerPage":10
        }
        response_query_publishList = self.post_json(url,data,header)
        if response_query_publishList.json()["content"]:
            if str(response_query_publishList.json()["content"][0]["publishId"]) == publishId:
                print("\033[32m货源审核列表查询成功,货源单id为: "+publishId)
                return publishId
        else:
            raise Exception("\033[31m货源审核列表未查询到该货源")

    """ 平台端货源单审核-差价单据需要审核 """
    def publish_save(self,publishId,feeFlag=0,feeAmount=0.0):
        url = self.get_manager_url("/api/business/priceChange/save")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {
            'type':1,
            'publishId':publishId,
            'sysCompanyPrice':1,
            'taxCarryPrice':1,
            'feeFlag':feeFlag,
            'feeAmount':feeAmount
        }
        response_publish_save = self.post_json(url,data,header)
        if response_publish_save.json()["code"] == 0:
            print("\033[32m货源审核成功,货源单id为: "+publishId)
        else:
            raise print("\033[31m货源审核失败,失败原因为: "+response_publish_save.text)


    """ 串联业务 """
    @staticmethod
    def auditPublish_all(publishId):
        publishAudit = PublishAudit()
        publishAudit.publish_save(publishAudit.query_publishList(publishId),publishAudit.feeFlag,publishAudit.feeAmount)


if __name__ == '__main__':
    print("\033[34m----------------平台委托承运货源审核开始-----------------------")
    managerTk = ManagerLogin().managerLogin("admin", "111111")
    PublishAudit.auditPublish_all("11714048")
    print("\033[34m----------------平台委托承运货源审核结束-----------------------")

