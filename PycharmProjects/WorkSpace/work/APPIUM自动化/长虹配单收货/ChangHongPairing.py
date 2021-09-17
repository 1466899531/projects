import random

from common.base import BaseTest
from common.sql import SqlTest
from common.sqlHome import SqlHome
from work.APPIUM自动化.appium_exception.AppiumException import AppiumException
from work.APPIUM自动化.appium_log.AppiumLogger import logger
from work.APPIUM自动化.安卓.PageElementUtil import PageElementUtil
from work.外部接口.JK_U33长虹民生.上传货源 import UploadPublish
from work.物泊56.接口测试.修改调度单创建时间 import UpdateCreatedDate


class ChangHongPairing(BaseTest):
    @staticmethod
    def do_publish(dependId, goodTypeDesc):
        """ 上传货源单  """
        if UploadPublish().uploadPublish(dependId, goodTypeDesc) == dependId:
            data = SqlTest.run_query_sql(SqlHome.query_publishIdByDependId(dependId))
            publishId = data[0]["publish_id"]
            logger.info("发单成功，货源单Id为："+str(publishId))
            return publishId
        else:
            raise AppiumException("发单失败")

    @staticmethod
    def get_publish(dependId):
        """ 根据业务单据id 获取货源单ID """
        sql = "SELECT * FROM business.bu_publish p WHERE p.depend_id = '" + dependId + "'"
        data = SqlTest.run_query_sql(sql)
        logger.info(data)
        if data is not None:
            return data[0]['publish_id']
        else:
            raise AppiumException("根据此dependId未查询到对应的货源单")

    @staticmethod
    def if_route_delivery(loginName):
        """ 判断司机是否存在在途调度单 """
        sql = "SELECT * FROM business.bu_delivery d WHERE d.driver_id = (SELECT d.driver_id FROM usercenter.uc_driver d WHERE d.driver_id = (SELECT l.user_id FROM usercenter.u_user_login l WHERE l.login_name = '" + str(
            loginName) + "'))AND d.val_status IN (10,20,30)"
        data = SqlTest.run_query_sql(sql)
        logger.info(data)
        if data is not None:
            logger.info("SQL判断该司机有在途调度单")
            return True
        else:
            logger.info("该司机没有在途调度单")
            return False

    """ 根据司机登录名更新该司机下调度单状态为00 """
    @staticmethod
    def update_deliveryStatus(loginName):
        SqlTest.run_update_sql(SqlHome.update_delivery_valStatus_byLoginName(loginName))
        logger.info("修改此在途调度单状态为00")

    @staticmethod
    def get_deliveryId(pubId):
        """ 根据货源单ID 获取调度单id """
        data = SqlTest.run_query_sql(SqlHome.query_deliveryIdByPublishId(pubId))
        deliveryId =data[0]["delivery_id"]
        return deliveryId

    @staticmethod
    def get_deliveryValStatus(deliveryId):
        """ 根据调度单ID 获取调度单状态 """
        data = SqlTest.run_query_sql(SqlHome.query_delivery_valStatus_sql(deliveryId))
        deliveryValStatus = data[0]["val_status"]
        return deliveryValStatus

    @staticmethod
    def get_delivery_carry_mode(deliveryId):
        """ 根据调度单ID 获取调度单承运人承运模式 """
        data = SqlTest.run_query_sql(SqlHome.query_delivery_valStatus_sql(deliveryId))
        delivery_Carrier_carry_mode = data[0]["carrier_carry_mode"]
        return delivery_Carrier_carry_mode


if __name__ == '__main__':
    login_name = "16630702259"
    password = "111111"
    env = "test"
    depend_id = "YW" + str(random.randint(100000, 1000000))
    good_type_desc = "煤炭及制品"
    jiHua_car_num = 3
    publish_id = ChangHongPairing.do_publish(depend_id, good_type_desc)
    """ 走UI层面 """
    pageElementUtil = PageElementUtil()
    pageElementUtil.login_page()
    pageElementUtil.login_info(login_name, password, env)
    pageElementUtil.login()
    if ChangHongPairing.if_route_delivery(login_name):
        pageElementUtil.exist_delivery()
        ChangHongPairing.update_deliveryStatus(login_name)
    else:
        pageElementUtil.no_exist_delivery()
    pageElementUtil.search_publishByPublishId(publish_id)
    pageElementUtil.grabBill()
    delivery_id = ChangHongPairing.get_deliveryId(publish_id)
    logger.info("抢单成功，调度单ID为："+str(delivery_id)+",调度单状态为：" + str(ChangHongPairing.get_deliveryValStatus(delivery_id))+"待取单")
    pageElementUtil.quDan()
    logger.info("取单成功，调度单状态为：" + str(ChangHongPairing.get_deliveryValStatus(delivery_id))+"待装货")
    pageElementUtil.zhuangHuo()
    logger.info("装货成功，调度单状态为：" + str(ChangHongPairing.get_deliveryValStatus(delivery_id))+"待收货")
    logger.info("装货成功之后，避开收货20分钟限制，修改调度单的创建时间")
    UpdateCreatedDate().update_created_date(delivery_id)
    pageElementUtil.shouHuo()
    if ChangHongPairing.get_delivery_carry_mode(delivery_id) ==1:  # 1代表计划模式，NULL代表单车模式'
        pageElementUtil.jiHua_CarryMode(jiHua_car_num)
    else:
        logger.info("单车模式，无需车数直接上传回单即可")
    pageElementUtil.upload_pic_and_shouHuo()
    logger.info("收货成功，调度单状态为：" + str(ChangHongPairing.get_deliveryValStatus(delivery_id))+"已完成")

