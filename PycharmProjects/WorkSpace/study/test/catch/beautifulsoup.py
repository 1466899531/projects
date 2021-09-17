import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
# ================================== beautifulsoup 来解析html页面内容，然后对页面内容进行提取。
def return_soup(url):     # 静态获取网页的源码，返回lxml解析格式
    response = requests.get(url)    # 构造一个向服务器请求资源的url对象
    response.encoding = response.apparent_encoding    # 解决中文乱码问题
    soup = BeautifulSoup(response.text, "lxml")    # 构造bs对象 解析html页面 lxml也是解析器，其作为解释器比html更稳定，更快
    return soup
# 获得每期的url
def get_app_url(url):
    soup = return_soup(url)
    journal_list = soup.find('ul',class_='gl_list2 gl_list_qk').find_all('li')
    journalpd = pd.DataFrame()
    i = 0
    for m,iss in enumerate(journal_list):
        journalpd.loc[i,'序号'] = str(i)
        # journalpd.loc[i,'期刊名称'] = journal_list[m].find('a').attrs['title']    # 获取title的内容
        journalpd.loc[i,'期刊名称'] = iss.find('a').attrs['title']    # 获取title的内容
        journalpd.loc[i,'url'] = journal_list[m].find('a').attrs['href']   # 获取href的内容
        i = i+1
    return journalpd

journalpd = get_app_url(url='https://www.cas.cn/kxyj/cb/qk/index.shtml')
journalpd.to_excel("D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\catchFile\\journal.xlsx")