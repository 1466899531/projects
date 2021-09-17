import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

from common.sql import SqlTest
from work.APPIUM自动化.appium_config.AppiumConfig import global_config
from work.APPIUM自动化.appium_log.AppiumLogger import logger

class PageElementUtil(object):
    def __init__(self, sleep_interval=2):
        desired_caps = {
            'platformName': global_config.get('android', 'platformName'),
            'platformVersion': global_config.get('android', 'platformVersion'),
            'deviceName': global_config.get('android', 'deviceName'),
            'appPackage': global_config.get('android', 'appPackage'),
            'appActivity': global_config.get('android', 'appActivity'),
            'unicodeKeyboard': global_config.get('android', 'unicodeKeyboard'),
            'resetKeyboard': global_config.get('android', 'resetKeyboard'),
            'noReset': global_config.get('android', 'noReset'),
            'newCommandTimeout': global_config.get('android', 'newCommandTimeout'),
            'automationName': global_config.get('android', 'automationName')
        }
        self.driver = webdriver.Remote(global_config.get('android', 'appiumServer_remoteUrl'), desired_caps)
        self.sleep_interval = sleep_interval

    def login_page(self):
        """ 新安装的app-进入登录页面 """
        time.sleep(5)
        try:
            el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/btn_agree")
        except StaleElementReferenceException as msg:
            print(u"查找同意并继续元素异常%s" % msg)
            print(u"重新获取元素")
            el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/btn_agree")
        logger.info("点击同意并继续")
        el1.click()
        time.sleep(3)
        try:
            el2 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button")
        except NoSuchElementException as msg:
            logger.error("未找到元素。继续查找", msg)
            time.sleep(self.sleep_interval)
            el2 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button")
        el2.click()
        logger.info("始终允许位置权限")
        time.sleep(self.sleep_interval)
        el3 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        el3.click()
        logger.info("始终允许照片权限")
        time.sleep(self.sleep_interval)
        el4 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        el4.click()
        logger.info("始终允许设备权限")

    def login_info(self, username, pwd, env):
        time.sleep(3)
        """ 完善登录页信息 """
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/et_phone_number")
        el1.send_keys(username)
        logger.info("输入用户名")
        el2 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/et_verify_code")
        el2.send_keys(pwd)
        logger.info("输入密码")
        el3 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/ck_remember_passowrd")
        el3.click()
        logger.info("点击记住密码")
        el4 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/cb_rule")
        el4.click()
        logger.info("点击同意规则")
        # dev:37 test:60
        el5 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/bt_" + env + "")
        el5.click()
        logger.info("选择" + env + "环境。注:【dev:37,test:60】")

    def login(self):
        """ 点击登录按钮 """
        el3 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_login")
        el3.click()
        logger.info("点击登录")

    def exist_delivery(self):
        """ 判断是否存在在途调度单 """
        time.sleep(5)
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/iv_back")
        el1.click()
        logger.info("存在在途调度单，点击返回")
        """ 登录进去之后关闭一些弹框 """
        time.sleep(self.sleep_interval)
        el7 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_cancel")
        el7.click()
        logger.info("关闭保存二维码弹窗")
        el8 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/positiveButton")
        el8.click()
        logger.info("点击稍后验证")
        el9 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/rb_resource_list")
        el9.click()
        logger.info("点击进入货源单列表")

    def no_exist_delivery(self):
        logger.info("不存在在途单,直接进入货源单列表")
        """ 登录进去之后关闭一些弹框 """
        time.sleep(self.sleep_interval)
        el7 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_cancel")
        el7.click()
        logger.info("关闭保存二维码弹窗")
        time.sleep(self.sleep_interval)
        el8 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/positiveButton")
        el8.click()
        logger.info("点击稍后验证")

    def search_publishByPublishId(self, publish_id):
        """ 货源单列表进行搜索货源单 """
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_select")
        el1.click()
        logger.info("点击筛选")
        el2 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/et_huoyuan_id")
        el2.send_keys(publish_id)
        logger.info("输入货源单Id: "+str(publish_id))
        el3 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_screen_detail_sure")
        el3.click()
        logger.info("点击确定按钮,进行搜索")

    def grabBill(self):
        """ 抢单 """
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/confirm_robbing")
        el1.click()
        logger.info("点击抢单")
        time.sleep(4)
        el2 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/btn_submission")
        el2.click()
        logger.info("提交抢单确认")
        time.sleep(5)

    def quDan(self):
        """ 取单 """
        time.sleep(3)
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/ll_querenqudan")
        el1.click()
        logger.info("点击取单")
        time.sleep(3)
        el2 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_agree")
        el2.click()
        logger.info("确认取单")
        time.sleep(self.sleep_interval)

    def zhuangHuo(self):
        """ 装货 """
        el3 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_zhuanghuo")
        el3.click()
        logger.info("点击装货")
        el4 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/negativeButton")
        el4.click()
        logger.info("确认装货")
        time.sleep(self.sleep_interval)

    def shouHuo(self):
        """ 收货 """
        time.sleep(self.sleep_interval)
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/ll_querenshouhuo")
        el1.click()
        logger.info("点击收货")

    def jiHua_CarryMode(self, num_car):
        """ 计划模式需要输入收货车数 """
        el1 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/et_input_zhuangchecheshu")
        el1.send_keys(num_car)
        logger.info("计划模式需要输入收货车数: "+str(num_car)+"车")

    def upload_pic_and_shouHuo(self):
        """ 根据配置是否上传回单，上传的话 则需调用此处 """
        time.sleep(3)
        el5 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/ll_shangchuan")
        el5.click()
        logger.info("点击上传回单")
        time.sleep(3)
        el2 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        el2.click()
        logger.info("允许访问相册")
        time.sleep(3)
        logger.info("再次点击上传回单")
        el10 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/ll_shangchuan")
        el10.click()
        time.sleep(3)
        el11 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/iv_arrow")
        el11.click()
        time.sleep(3)
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.RelativeLayout[2]/android.widget.ImageButton")
        el3.click()
        logger.info("选择图片")
        time.sleep(4)
        el4 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/common_actionbar_right_btn")
        el4.click()
        logger.info("确定选择的图片")
        time.sleep(3)
        el6 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/btn_commit")
        el6.click()
        logger.info("确认上传")
        time.sleep(3)
        el8 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_queren")
        el8.click()
        logger.info("确认收货")
        time.sleep(3)
        el7 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/negativeButton")
        el7.click()
        time.sleep(self.sleep_interval)
        logger.info("收货成功，点击确定按钮去除弹框")
        el9 = self.driver.find_element_by_id("com.yaojet.tma.goods:id/tv_queding")
        el9.click()







if __name__ == '__main__':
    pageElementUtil = PageElementUtil()
    pageElementUtil.login_page()
    pageElementUtil.login_info("16630702259", "111111", "test")
    pageElementUtil.login()
    pageElementUtil.no_exist_delivery()
    dependId = 'YD202108270048386'
    sql = "SELECT * FROM business.bu_publish p WHERE p.depend_id = '" + dependId + "'"
    data = SqlTest.run_query_sql(sql)
    pageElementUtil.search_publishByPublishId(data[0]['publish_id'])
