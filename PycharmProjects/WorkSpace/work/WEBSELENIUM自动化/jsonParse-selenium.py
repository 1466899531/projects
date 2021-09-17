import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class JsonParse(object):
    """ 获取类的全局变量,初始化赋值 """
    def __init__(self):
        self.target_app_url = "https://www.sojson.com/simple_json.html"
        chromedriverPath ='D:\\02-Test\\chromedriver_win32\\chromedriver.exe'
        self.webDriver =JsonParse.get_driver(chromedriverPath)
    """ 获取浏览器驱动 """
    @staticmethod
    def get_driver(chromedriverPath):
        # 1.获取谷歌浏览器配置项
        chrome_options = webdriver.ChromeOptions()
        #   1.1.设置配置参数 ---如果不加这个选项，有时定位会出现问题
        chrome_options.add_argument('--disable-gpu')
        #   1.2.设置配置参数 ---以最高权限运行
        chrome_options.add_argument('--no-sandbox')
        #   1.3.设置配置参数 ---指定浏览器分辨率
        chrome_options.add_argument('window-size=10000*10000')
        #   1.4.设置配置参数 ---浏览器不显示受自动测试软件控制
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--auto-open-devtools-for-tabs")
        #       1.4.1.谷歌浏览器版本在V76以及以上
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #       1.4.2.不自动关闭浏览器
        chrome_options.add_experimental_option("detach", True)
        #   1.5.设置配置参数 ---启动时自动全屏(相当于在浏览器界面按F11按键)
        chrome_options.add_argument('-kiosk')
        #   1.6设置配置参数 ---调用chrome浏览器取消密码保存默认设置
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)

        # 2.获取谷歌浏览器驱动,并设置配置参数
        driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriverPath)
        # 3.窗口最大化显示
        driver.maximize_window()
        # driver.implicitly_wait(20)
        return driver

    def json_writeContent(self,jsonString):
        self.webDriver.get(self.target_app_url)
        self.webDriver.find_element_by_id("eT").send_keys(json.dumps(jsonString))
if __name__ == '__main__':
    jsonParse =JsonParse()
    json_string = {"businessNum":"1234567890","carNum":"蒙C19193","contactPerson":"谢焕星","createDate":"2021-08-09 17:38:19","deliveryId":"18929358","deliveryNum":"DD210809100009","dependId":"20210804006","dependNum":"202108040006","driverName":"许菡达","driverPhone":"16630702259","handCarNo":"蒙C19193","idBackPic":"http://testpic.56yongche.com/201911/ios_3da0087389a6462b8f86daf788c3e6c0.jpg","idFontPic":"http://testpic.56yongche.com/201911/ios_b55b1c703cc14e1e98103c7efb3f28a5.jpg","idNum":"513436200111088955","licenceIdNo":"513436200111088955","licenceIssuingAuthority":"","licencePic":"http://testpic.56yongche.com/201911/ios_f3aae0b70105495ebcce20e7c599c196.jpg","meter":13,"occupNum":"513436200111088955","occupPic":"http://testpic.56yongche.com/202106/WBKJ_ee04d9e9c7944629aded9447eba1bb2c.jpg","quasiDrivingType":"A2","roadTransNo":"1234567890","tonnage":30,"totalTonnage":60.000,"useNature":"货运","vehicleIdentificationCode":"1234567890","vehicleLicenseName":"黄色","vehiclePic":"http://testpic.56yongche.com/202106/WBKJ_5066b174e58849f08967d1005dc0b8ea.jpg","vehicleStyleName":"罐式挂车","zcCardPic":"http://testpic.56yongche.com/201911/ios_73b8866e93544e548656e47f4ccef27b.jpg","zcCertificationDate":"Invalid date","zcIssuingAuthority":"","zcRegistrationDate":"2020-07-16","zcTransPic":"http://testpic.56yongche.com/202106/WBKJ_5066b174e58849f08967d1005dc0b8ea.jpg"}
    jsonParse.json_writeContent(json_string)
