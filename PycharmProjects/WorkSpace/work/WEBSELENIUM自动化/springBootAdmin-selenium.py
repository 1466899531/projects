import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class SpringBootAdmin(object):

    """ 获取类的全局变量,初始化赋值 """
    def __init__(self):
        self.target_app_url = "http://10.0.161.60:8850/login"
        chromedriverPath ='D:\\0-software\\Selenium\\chromedriver.exe'
        self.webDriver =SpringBootAdmin.get_driver(chromedriverPath)
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

    """ 登录springBootAdmin """
    def springBootAdmin_login(self,name,pwd):
        self.webDriver.get(self.target_app_url)
        # 隐性等待，最长等30秒 在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
        # webDriver.implicitly_wait(30)
        ele_usernameInput = self.webDriver.find_element_by_name('username')
        time.sleep(1)
        ele_usernameInput.send_keys(name)  # 输入用户名
        self.webDriver.find_element_by_name("password").send_keys(pwd) # 输入密码
        self.webDriver.find_element_by_xpath('/html/body/section/div/div/div/div/form/div[4]/div/input').click() # 点击登录
        time.sleep(1)

    """ 进入首页模块 """
    def springBootAdmin_homePage(self):
        self.webDriver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/div/a[1]').click()

    """ 进入项目列表 """
    def springBootAdmin_projectList(self):
        self.webDriver.find_element_by_xpath('//*[@id="navigation"]/div/div[2]/div/a[2]').click()

    """ 选择对应的项目 """
    def springBootAdmin_selectApp(self,projectName):
        self.webDriver.find_element_by_id(str.upper(projectName)).click()
        time.sleep(3)

    """ 进入项目详情 """
    def springBootAdmin_toAppDetail(self,projectName):
        self.webDriver.find_element_by_xpath('//*[@id="'+str.upper(projectName)+'"]/div').click()
        time.sleep(1)

    """ 选择缓存处理项 """
    def springBootAdmin_caches(self):
        self.webDriver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/aside/div/ul/li[6]/a').click()
        time.sleep(2)

    """ 清除缓存"""
    def springBootAdmin_clear(self):
        self.webDriver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/section/div/table/thead/tr/th[3]/button/span').click()


if __name__ == '__main__':
    springBootAdmin =SpringBootAdmin()
    username = "admin"
    password = "admin"
    project_name = "finance"
    springBootAdmin.springBootAdmin_login(username,password)
    # springBootAdmin.springBootAdmin_homePage()
    springBootAdmin.springBootAdmin_projectList()
    springBootAdmin.springBootAdmin_selectApp(project_name)
    springBootAdmin.springBootAdmin_toAppDetail(project_name)
    springBootAdmin.springBootAdmin_caches()
    springBootAdmin.springBootAdmin_clear()
