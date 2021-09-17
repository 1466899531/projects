from selenium import webdriver
import pandas as pd

# 对于一些网站，可能使用反爬虫手段，导致一些页面无法通过beautifulsoup获取，这个时候可以采用的是webdriver
def get_browser(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def get_journal(url):
    browser = get_browser(url)
    journal_list = browser.find_element_by_class_name('gl_list2.gl_list_qk').find_elements_by_tag_name('li')
    journalpd = pd.DataFrame()
    for i,name in enumerate(journal_list):
        journalpd.loc[i,'期刊名称'] = name.find_element_by_tag_name('a').text
        journalpd.loc[i,'url'] = name.find_element_by_tag_name('a').get_attribute('href')
    return journalpd
get_journal('https://www.cas.cn/kxyj/cb/qk/index.shtml')