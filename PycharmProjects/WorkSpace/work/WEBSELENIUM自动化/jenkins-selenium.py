import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class Jenkins(object):

    """ 获取类的全局变量,初始化赋值 """
    def __init__(self):
        self.target_app_url = "http://developer.wbtech.com:9802/login"
        self.webDriver =Jenkins.get_driver()
        self.actions = ActionChains(self.webDriver) # 打开新的标签页

    """ 获取浏览器驱动 """
    @staticmethod
    def get_driver():
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
        #   1.6设置配置参数 ---调用chrom浏览器取消密码保存默认设置
        prefs = {"":""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        chrome_options.add_experimental_option("prefs", prefs)

        # 2.获取谷歌浏览器驱动,并设置配置参数
        driver = webdriver.Chrome(options=chrome_options,executable_path='D:\\0-software\\Selenium\\chromedriver.exe')
        # 3.窗口最大化显示
        driver.maximize_window()
        # driver.implicitly_wait(20)
        return driver

    """ 登录jenkins """
    def jenkins_login(self,name,pwd):
        self.webDriver.get(self.target_app_url)
        # 隐性等待，最长等30秒 在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
        # webDriver.implicitly_wait(30)
        ele_usernameInput = self.webDriver.find_element_by_id("j_username")
        time.sleep(1)
        ele_usernameInput.send_keys(name)  # 输入用户名
        self.webDriver.find_element_by_name("j_password").send_keys(pwd) # 输入密码
        self.webDriver.find_element_by_name('Submit').click() # 点击登录

    """ 选择项目环境 """
    def jenkins_select_test(self,test):
        if test == 1:
            self.webDriver.find_element_by_xpath('//*[@id="projectstatus-tabBar"]/div/div[1]/div[5]/a').click()
        elif test == 2:
            self.webDriver.find_element_by_xpath('//*[@id="projectstatus-tabBar"]/div/div[1]/div[6]/a').click()
        elif test == 3:
            self.webDriver.find_element_by_xpath('//*[@id="projectstatus-tabBar"]/div/div[1]/div[7]/a').click()

    """ 发布项目 """
    def jenkins_do_project(self,test,projectName):
        self.webDriver.find_element_by_xpath('//*[@id="job_56yc3.0-'+test+'-'+projectName+'"]/td[7]/a/img').click()
        time.sleep(1)
    """ 发布成功之后点击进入 """
    def jenkins_do_content(self,test,projectName):
        self.webDriver.find_element_by_xpath('//*[@id="job_56yc3.0-'+test+'-'+projectName+'"]/td[3]/a').click()
    """ """
    def jenkins_do_move(self):
        move = self.webDriver.find_element_by_xpath('//*[@id="pipeline-box"]/div/div/table/tbody[2]/tr[1]/td[1]/div/div/div[2]/div[2]')
        self.actions.move_to_element(move).perform()

if __name__ == '__main__':
    jenkins =Jenkins()
    username = "xiehuanxing"
    password = "Txhx202004"
    test_num = 1
    project_name = "web-manager"
    jenkins.jenkins_login(username, password)
    jenkins.jenkins_select_test(test_num)
    if test_num == 1:
        jenkins.jenkins_do_project("test",project_name)
        jenkins.jenkins_do_content("test",project_name)
    elif test_num == 2:
        jenkins.jenkins_do_project("test2",project_name)
        jenkins.jenkins_do_content("test2",project_name)
    elif test_num == 3:
        jenkins.jenkins_do_project("test3",project_name)
        jenkins.jenkins_do_content("test3",project_name)

