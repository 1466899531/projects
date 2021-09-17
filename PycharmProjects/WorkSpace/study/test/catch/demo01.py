# _*_coding=utf-8_*_
from selenium import webdriver
import time
import xlwt

class Crawler_Blt(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baletu.com')
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('search-input').send_keys('金葵新城西区')
        self.driver.find_element_by_id('index_search').click()
        self.workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook 其实就是execl，
        self.worksheet = self.workbook.add_sheet('my_worksheet')  # 创建表，如果想创建多个，直接在后面再add_sheet

    def get_cont(self):
        content = self.driver.find_elements_by_class_name('listUnit-date.clearfix.PBA_list_house')
        n = 0
        self.data = []
        for con in content:
            n += 200
            time.sleep(0.5)
            js = f"var q=document.documentElement.scrollTop={n}"
            self.driver.execute_script(js)
            self.data.append(con.find_element_by_class_name('list-pic-ps').text)
            self.data.append(con.find_element_by_class_name('pro-lable').text)
            self.data.append(con.find_element_by_class_name('list-pic-ad').text)
            self.data.append(con.find_element_by_class_name('price').text)
            self.data.append(con.find_element_by_class_name('lazy').get_attribute('src'))

        self.driver.close()
        return self.data

    def write_cont(self, colx=None):
        rowx = 1
        self.colx = colx
        for con in range(len(self.data)):
            if con == self.colx or con % 5 == self.colx:
                self.worksheet.write(rowx, self.colx, self.data[con])
                rowx += 1

    def write_excel(self):
        self.write_cont(colx=0)
        self.write_cont(colx=1)
        self.write_cont(colx=2)
        self.write_cont(colx=3)
        self.write_cont(colx=4)
        self.rawstitle = [' 房屋信息', '房屋位置', '房屋配置', '价格', '照片']
        for i in range(len(self.rawstitle)):
            self.worksheet.write(0, i, self.rawstitle[i])

        self.workbook.save('D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\catchFile\\journal.xls')

    def run(self):
        self.get_cont()
        self.write_excel()
        self.write_cont()

if __name__ == '__main__':
    cc = Crawler_Blt()
    cc.run()

