from common.base import BaseTest
from work.物泊56.平台端.平台端登录 import ManagerLogin
from work.物泊56.承运人端.物流公司.物流公司注册 import LogisRegister


class LogisAudit(BaseTest):

    """ 平台端-物流公司注册审核管理数据查询 """
    def query_LogisAudit(self,logisName):
        url = self.get_manager_url("/api/user/rgtLogis/query")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data ={
            "logisName":logisName,
            "page":0,
            "sizePerPage":10,
            "sort":[
                "loginId"
            ],
            "order":[
                "DESC"
            ]
        }
        response_query_LogisAudit = self.post_json(url,data,header)
        if response_query_LogisAudit.json()["content"]:
            if str(response_query_LogisAudit.json()["content"][0]["logisName"]) == logisName:
                loginName = str(response_query_LogisAudit.json()["content"][0]["loginName"])
                print("\033[32m物流公司注册审核列表查询成功,物流公司登录名为: "+str(loginName))
                return str(response_query_LogisAudit.json()["content"][0]["loginId"])
        else:
            raise Exception("\033[31m司机注册审核列表未查询到该司机")

    """ 平台端-物流公司审核 """
    def auditPass(self,loginId,robTaxFlag=1):
        url = self.get_manager_url("/api/user/logis/auditPass")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data = {"loginId":loginId,"auditedRemark":"robTaxFlag: 1可抢含税,0不可抢含税","robTaxFlag":robTaxFlag}
        response_auditPass = self.post_json(url,data,header)
        if response_auditPass.json()["code"] == 0:
            print("\033[32m物流公司审核通过")
            return True
        else:
            raise print("\033[31m物流公司审核通过失败,失败原因为: "+response_auditPass.text)

    """ 串联业务 """
    @staticmethod
    def auditLogis_all(logisName):
        logisAudit = LogisAudit()
        login_id = logisAudit.query_LogisAudit(logisName)
        if login_id:
            if logisAudit.auditPass(login_id):
                print("物流公司审核通过了, 去做业务吧!")

""" 测试 """
if __name__ == '__main__':
    print("\033[34m----------------平台物流公司注册审核开始-----------------------")
    managerTk = ManagerLogin().managerLogin("admin", "111111")
    LogisAudit.auditLogis_all(LogisRegister.registerLogis_all())
    print("\033[34m----------------平台物流公司注册审核结束-----------------------")

