import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Jira(object):

    """ 获取类的全局变量,初始化赋值 """
    def __init__(self):
        self.target_app_url = "http://developer.wbtech.com:9803/"
        chromedriverPath ='D:\\0-software\\Selenium\\chromedriver.exe'
        self.webDriver =Jira.get_driver(chromedriverPath)
        self.actions = ActionChains(self.webDriver)

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

    """ 登录jira """
    def jira_login(self,name,pwd):
        self.webDriver.get(self.target_app_url)
        # 隐性等待，最长等30秒 在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
        # webDriver.implicitly_wait(30)
        ele_usernameInput = self.webDriver.find_element_by_id("login-form-username")
        time.sleep(1)
        ele_usernameInput.send_keys(name)  # 输入用户名
        self.webDriver.find_element_by_id("login-form-password").send_keys(pwd) # 输入密码
        self.webDriver.find_element_by_id('login').click() # 点击登录
        time.sleep(1)

    """ 进入我的问题页面 """
    def jira_myProblem(self):
        time.sleep(2)
        self.webDriver.find_element_by_id('find_link').click() # 点击问题
        time.sleep(2)
        self.webDriver.find_element_by_id('filter_lnk_my_lnk').click() # 我的问题
        time.sleep(3)

    """ 进入我的报告页面 """
    def jira_myReport(self):
        time.sleep(1)
        self.webDriver.find_element_by_id('find_link').click() # 点击问题
        time.sleep(1)
        self.actions.key_down(Keys.CONTROL).click(self.webDriver.find_element_by_id('filter_lnk_reported_lnk')).key_up(Keys.CONTROL).perform() # 点击我的报告
        self.webDriver.switch_to.window(self.webDriver.window_handles[1]) # 切换到新标签页
        time.sleep(3)

    """ 搜索jira """
    def jira_search(self,jiraNum,jiraCount):
        js = "window.open('"+self.target_app_url+"')"
        self.webDriver.execute_script(js)
        self.webDriver.switch_to.window(self.webDriver.window_handles[jiraCount])
        ele_searchInput = self.webDriver.find_element_by_id('quickSearchInput') # 获取搜索jira输入框
        ele_searchInput.send_keys(jiraNum)
        ele_searchInput.send_keys(Keys.ENTER) # 回车键(Enter)
        time.sleep(1)

    """ 获取jira状态 """
    def jira_status(self):
        time.sleep(2)
        return self.webDriver.find_element_by_id('status-val').text

    """ 获取jira经办人 """
    def jira_operator(self):
        return self.webDriver.find_element_by_id('assignee-val').text

    """ 分配给我 """
    def jira_giveMe(self,jiraNum,name):
        self.webDriver.find_element_by_id('assign-to-me').click()
        print(jiraNum+"成功分配给"+name+"!")
        time.sleep(2)

    """ 维护jiraNum """
    @staticmethod
    def jira_num():
        jira_num_list = ['TMS-22017']
        return jira_num_list

if __name__ == '__main__':
    jira =Jira()
    username = "xiehuanxing"
    password = "xhx1466899531!"
    jira.jira_login(username,password)
    jira.jira_myProblem() # 标签页0
    jira.jira_myReport() # 标签页1
    jira_count = 1  # 所以从1开始
    for jira_num in Jira.jira_num():
        jira_count += 1
        jira.jira_search(jira_num,jira_count)
        if jira.jira_status() == "测试部署" and jira.jira_operator() != "谢焕星":
            jira.jira_giveMe(jira_num,username)

