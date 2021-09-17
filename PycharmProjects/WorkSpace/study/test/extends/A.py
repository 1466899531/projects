from selenium.webdriver.chrome.webdriver import WebDriver

class A(WebDriver):
    print(111)

if __name__ == '__main__':
    A().find_element_by_class_name()
