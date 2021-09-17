from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome


class OwnerRegister(BaseTest):
    """ 发送注册短信 """
    def send_message(self,phone):
        url = self.get_app_url("/sendMessage/operatorRegister")
        payload = {
            "mobile": phone
        }
        response_send_message = self.post_json(url, payload)
        if response_send_message.text.__contains__("\"code\":0"):
            print("\033[32m注册短信验证码发送成功")
            return True
        else:
            raise print("\033[31m注册短信验证码发送失败,失败原因 : " + response_send_message.text)
    """ 判断是否被注册 """
    def verify(self, code,mobile):
        url = self.get_consignor_url("/api/verify/verify")
        payload = {
            "code": code,
            "mobile": mobile
        }
        response_verify = self.post_json(url, payload)
        if response_verify.text:
            print("\033[32m验证码校验成功")
            return True
        else:
            raise print("\033[31m校验失败,失败原因 : " + response_verify.text)
    """ 提交货主注册请求 """
    def register_owner(self, ownerName,loginName,password,phone):
        url = self.get_consignor_url("/api/rgt/rgtOwner/addRgtOwner")
        payload = {
            "loginName":loginName,
            "password":password,
            "ownerName":ownerName,
            "taxNum":"913301107517434382",
            "contactPerson":"谢焕星",
            "contactPhone":phone,
            "userName":"谢焕星",
            "address":"华滋奔腾大厦",
            "companyNature":"1",
            "registerAmt":"100000000",
            "businessLicensePic":"202108/dd62b158a1f648f7bdc5c0a843cd22ce-e5beaee4bfa1e59bbee789875f323032313033303131383139.jpg",
            "province":"上海市",
            "city":"上海市",
            "country":"浦东新区"
        }
        response_register_owner = self.post_json(url,payload)
        if response_register_owner.text.__contains__("\"code\":0"):
            print("\033[32m货主注册成功-------"+ ownerName+"----登录名: "+loginName)
            return True
        else:
            raise print("\033[31m货主注册失败,失败原因 : " + response_register_owner.text)
    """ 货主注册 """
    @staticmethod
    def registerOwner_all():
        phone = '13838339604'
        ownerName = '550军团'
        loginName = 'hxhz'
        password = 'Aa1466899531'
        if OwnerRegister().send_message(phone):
            SqlTest.run_delete_sql(SqlHome.delRgtOwner_sql(loginName,ownerName))
            SqlTest.run_delete_sql(SqlHome.delOwnerByOwnerName_sql(ownerName))
            SqlTest.run_delete_sql(SqlHome.delLoginUserByLoginName_sql(loginName))
        if OwnerRegister().verify(SqlTest.run_queryMessageCode_sql(SqlHome.queryMessageCode_sql(phone)),phone):
            if OwnerRegister().register_owner(ownerName, loginName, password, phone):
                audited_status = SqlTest.run_query_sql(SqlHome.queryOwnerAuditStatus__sql(ownerName))[0]['audited_status']
                if audited_status == 1:
                    print("\033[34m------------------------货主注冊完成,开始审核-----------------------------------")
                    SqlTest.run_update_sql(SqlHome.update_ownerPassword_sql(loginName))
                    return ownerName
                else:
                    raise print("\033[31m货主不是待审核状态")
if __name__ == '__main__':
    print("\033[34m------------------------货主注冊开始-----------------------------------")
    print(OwnerRegister.registerOwner_all())