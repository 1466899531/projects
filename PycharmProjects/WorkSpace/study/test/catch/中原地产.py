import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

class CaptureZYDC(object):
    """
        获取类的全局变量,初始化赋值
    """
    def __init__(self):
        self.target_path = "D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\catchFile\\result.xlsx"
        self.target_app_url = "https://sh.centanet.com/ershoufang/"
        self.request_headers = self.get_request_param()
        self.driver = self.get_driver()

    """
        获取浏览器驱动
    """
    def get_driver(self):
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
        #       1.4.1.谷歌浏览器版本在V76以及以上
        chrome_options.add_experimental_option('useAutomationExtension', True)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #   1.5.设置配置参数 ---启动时自动全屏(相当于在浏览器界面按F11按键)
        chrome_options.add_argument('-kiosk')
        #   1.6设置配置参数 ---调用chrom浏览器取消密码保存默认设置
        prefs = {"":""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        chrome_options.add_experimental_option("prefs", prefs)
        # 2.获取谷歌浏览器驱动,并设置配置参数
        driver = webdriver.Chrome(options=chrome_options)
        # 3.窗口最大化显示
        driver.maximize_window()
        driver.implicitly_wait(20)
        return driver

    """
        获取入参
    """
    def get_request_param(self):
        request_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
        }
        return request_headers

    """
        获取静态获取网页的源码，返回lxml解析格式
    """
    def get_soup(self,target_app_url):
        # 构造一个向服务器请求资源的url对象
        response = requests.get(url=target_app_url, headers=self.request_headers)
        # 解决中文乱码问题
        response.encoding = response.apparent_encoding
        # 构造bs对象 解析html页面 lxml也是解析器
        resultSoup = BeautifulSoup(response.text, "html.parser")
        # 返回解析后的HTML页面
        return resultSoup

    """
        获取页数地址
    """
    def get_pageUrl(self,target_app_url,num):
        home_pageUrl = []
        for i in range(1,num):
            page = str('g'+str(i))
            target_nextUrl = str(target_app_url+page)
            home_pageUrl.append(target_nextUrl)
        return home_pageUrl

    """ 
        获取房源标题
    """
    def get_title(self,target_app_url):
        resultSoup = self.get_soup(target_app_url)
        # prettify美化，会格式化输出，还会自动补齐闭合
        # resultSoup.prettify()
        div_ResultSet = resultSoup.findAll(name='div',attrs={'class':'box-c-tt'})
        home_title = []
        for div in div_ResultSet:
            a_list = div.select('a')
            for a in a_list:
                home_title.append(a.text)
        return home_title

    """ 
        获取房源详情页URL
    """
    def get_detail(self,target_app_url):
        resultSoup = self.get_soup(target_app_url)
        div_ResultSet = resultSoup.findAll(name='div',attrs={'class':'box-c-tt'})
        home_detail = []
        for div in div_ResultSet:
            a_list = div.select('a')
            for a in a_list:
                string = str(a['href']).replace('/ershoufang/','')
                target_detailUrl = str(target_app_url+string)
                home_detail.append(target_detailUrl)
        return home_detail
    """ 
        获取经纪人姓名
    """
    def get_name(self,target_app_url):
        home_detail = self.get_detail(target_app_url)
        home_name =[]
        for home_target_detailUrl in home_detail:
            resultSoup = self.get_soup(home_target_detailUrl)
            div_ResultSet = resultSoup.findAll(name='div',attrs={'class':'box_info_more'})
            for divTag in div_ResultSet:
                a_list = divTag.select('a')
                for name in a_list:
                    home_name.append(str(name.text))
        return home_name

    """ 
        获取经纪人电话
    """
    def get_phone(self,target_app_url):
        home_detail = self.get_detail(target_app_url)
        home_phone =[]
        for home_target_detailUrl in home_detail:
            self.driver.get(home_target_detailUrl)
            phone_list = self.driver.find_elements_by_xpath('//*[@id="detail"]/div[1]/div/div[3]/div[2]/div/div/div[4]/div/div[1]/div[2]/div/h3')
            time.sleep(2)
            for phone in phone_list:
                home_phone.append(str(phone.text))
        self.driver.close()
        return home_phone

    """ 
        获取房源介绍信息
    """
    def get_explain(self,target_app_url):
        resultSoup = self.get_soup(target_app_url)
        div_ResultSet = resultSoup.findAll(name='div',attrs={'class':'box-c-tp'})
        home_explain = []
        for div in div_ResultSet:
            home_explain.append(div.text.replace('\n', '').replace(' ','').replace('\r', ''))
        return home_explain

    """ 
        获取房源地址
    """
    def get_address(self,target_app_url):
        resultSoup = self.get_soup(target_app_url)
        div_ResultSet = resultSoup.findAll(name='div',attrs={'class':'box-c-lc'})
        home_address = []
        for divTag in div_ResultSet:
            p_ResultSet = divTag.select('p')
            for pTag in p_ResultSet:
                home_address.append(pTag.text.replace('\n', '').replace(' ','-').replace('\r', ''))
        return home_address

    """ 
       获取房源价格
    """
    def get_price(self,target_app_url):
        resultSoup = self.get_soup(target_app_url)
        div_ResultSet = resultSoup.findAll(name='div',attrs={'class':'ct-box-r'})
        home_price = []
        for divTag in div_ResultSet:
            span_ResultSet = divTag.select('span')
            p_ResultSet = divTag.select('p')
            em_ResultSet = divTag.select('em')
            for spanTag,emTag,pTag in zip(span_ResultSet,em_ResultSet,p_ResultSet):
                p_text = str(pTag.text)
                if p_text.__contains__('降'):
                    continue
                else:
                    home_price.append('总价'+spanTag.text+emTag.text+'||单价'+pTag.text)
        return home_price

    """
        写数据到excel表格
    """
    def write_dataToExcel(self):
        data_df = pd.DataFrame()
        # 设置索引列名
        data_df.index.name = 'id'
        data_df["房屋标题"] = self.get_title(self.target_app_url)
        data_df["房屋详情页"] = self.get_detail(self.target_app_url)
        data_df["房屋介绍"] = self.get_explain(self.target_app_url)
        data_df["房屋地址"] = self.get_address(self.target_app_url)
        data_df["房屋联系人姓名"] = self.get_name(self.target_app_url)
        data_df["房屋联系人电话"] = self.get_phone(self.target_app_url)
        data_df["房屋价格"] = self.get_price(self.target_app_url)
        # 创建一个writer
        writer = pd.ExcelWriter('Excel_test_homeMessage.xlsx')
        data_df.to_excel(writer, sheet_name='房屋信息统计', float_format='%.5f',encoding='utf-8',index=True)  # float_format 控制精度
        # 保存
        writer.save()

    """
        设置excel表格样式
    """
    def set_excel_style(self,writer):
        workbook = writer.book
        worksheet = writer.sheets['房屋信息统计']
        header_format = workbook.add_format({
            'bold': True, # 字体加粗
            'text_wrap': True, # 是否自动换行
            'valign': 'top',  #垂直对齐方式
            'align': 'right', # 水平对齐方式
            'fg_color': '#FFEE99', # 单元格背景颜色
            'border': 5}) # 单元格边框宽度
        worksheet.set_row(0, cell_format=header_format)

    """
        测试
    """
    def run_get_detailAndTitle(self):
        self.write_dataToExcel()

    """
        总方法执行入口
    """
if __name__ == '__main__':
    captureZYDC = CaptureZYDC()
    captureZYDC.run_get_detailAndTitle()