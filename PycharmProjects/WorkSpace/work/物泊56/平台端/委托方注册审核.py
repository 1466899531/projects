from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.物泊56.平台端.平台端登录 import ManagerLogin
from work.物泊56.承运人端.物流公司.物流公司注册 import LogisRegister
from work.物泊56.货主端.货主注册 import OwnerRegister


class OwnerAudit(BaseTest):

    """ 平台端-委托方注册审核管理数据查询 """
    def query_OwnerAudit(self,ownerName):
        url = self.get_manager_url("/api/user/rgtOwner/query")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data ={
            "ownerName":ownerName,
            "page":0,
            "sizePerPage":10,
            "sort":[
                "loginId"
            ],
            "order":[
                "DESC"
            ]
        }
        response_query_OwnerAudit = self.post_json(url,data,header)
        if response_query_OwnerAudit.json()["content"]:
            if str(response_query_OwnerAudit.json()["content"][0]["ownerName"]) == ownerName:
                loginName = str(response_query_OwnerAudit.json()["content"][0]["loginName"])
                print("\033[32m货主注册审核列表查询成功,货主登录名为: "+str(loginName))
                return str(response_query_OwnerAudit.json()["content"][0]["loginId"])
        else:
            raise Exception("\033[31m货主注册审核列表未查询到该货主")

    """ 平台端-货主审核(税率) """
    def auditPass(self,loginId):
        url = self.get_manager_url("/api/user/owner/auditPass")
        header = {
            'Content-Type':'application/json',
            'Cookie':'MANAGER-SESSION='+managerTk
        }
        data ={
            "ownerName":"550军团",
            "companyNature":1,
            "registerAmt":100000000,
            "taxNum":"913301107517434382",
            "address":"华滋奔腾大厦",
            "contactPerson":"谢焕星",
            "contactPhone":"13838339604",
            "ownerWeightUnit":"吨",
            "customerCode":"2215",
            "businessLicensePic":"202108/dd62b158a1f648f7bdc5c0a843cd22ce-e5beaee4bfa1e59bbee789875f323032313033303131383139.jpg",
            "province":"上海市",
            "city":"上海市",
            "country":"浦东新区",
            "loginId":loginId,
            "sysCompanyId":124130,
            "taxRate":0.01,
            "taxRateCarrier":0.01,
            "amtCalModel":1,
            "prechargeGenorderAmount":"10000000",
            "fundDeductModel":1,
            "yfjsAuditFlag":1,
            "signAuditFlag":0,
            "calcAuditFlag":0,
            "invoiceFormFlag":1,
            "prePublishFlag":0,
            "deliveryAudit":0,
            "contractDate":1914336000000,
            "ownerOrgan":0,
            "referrer":"Python脚本",
            "prechargeGenorderFlag":1,
            "kefuFlag":1,
            "cancelDeliveryFlag":1,
            "sysCompanyCal":1,
            "sysOrganId":10000043,
            "sysUserId":10000105,
            "sysOrganName":"测试部门5",
            "customerPayFlag":0,
            "taxFlag":1,
            "companyClassification":1,
            "pointUseType":0,
            "ownerItType":"0",
            "ifAssociatedCompany":1,
            "yfjsValidateFlag":1,
            "publishLvesFlag":0,
            "picAuditedBusiSwitch":0,
            "picAutoAuditedFlag":1,
            "businessMode":0,
            "businessType":1
        }
        response_auditPass = self.post_json(url,data,header)
        if response_auditPass.json()["code"] == 0:
            print("\033[32m货主审核通过")
            return True
        else:
            raise print("\033[31m货主审核通过失败,失败原因为: "+response_auditPass.text)

    """ 串联业务 """
    @staticmethod
    def auditLogis_all(ownerName):
        ownerAudit = OwnerAudit()
        login_id = ownerAudit.query_OwnerAudit(ownerName)
        if login_id:
            if ownerAudit.auditPass(login_id):
                print("税率货主审核通过了, 去做业务吧!")

""" 测试 """
if __name__ == '__main__':
    print("\033[34m----------------平台货主注册审核开始-----------------------")
    managerTk = ManagerLogin().managerLogin("admin", "111111")
    OwnerAudit.auditLogis_all(OwnerRegister.registerOwner_all())
    print("\033[34m----------------平台货主注册审核结束-----------------------")

