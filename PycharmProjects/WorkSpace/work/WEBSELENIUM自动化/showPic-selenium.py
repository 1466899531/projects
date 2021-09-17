import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class ShowPic(object):
    """ 获取类的全局变量,初始化赋值 """
    def __init__(self):
        self.target_app_url = "https://jxwy-csoss.oss-cn-hangzhou.aliyuncs.com/"
        chromedriverPath ='D:\\02-Test\\chromedriver_win32\\chromedriver.exe'
        self.webDriver =ShowPic.get_driver(chromedriverPath)
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

    def show_pic(self,picUrl):
        self.webDriver.get(self.target_app_url+picUrl)
if __name__ == '__main__':
    showPic =ShowPic()
    pic_url = "202106/ios_85b5fc52031a45a9bbef8973f3ea683f.jpg"
    showPic.show_pic(pic_url)
