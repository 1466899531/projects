# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver

caps={}
caps["platformName"] = "Android"
caps["plarformVersion"] = "10"
caps["deviceName"] = "PCT_AL10"
caps["appPackage"] = "com.yaojet.tma.goods"
caps["appActivity"] = ".ui.dirverui.main.activity.SplashActivity"
caps["resetKeyboard"] = True
caps["automationName"] = "UiAutomator2"
caps["unicodeKeyboard"] = True
caps["noReset"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

time.sleep(10)
el3 = driver.find_element_by_id("com.yaojet.tma.goods:id/et_verify_code")
el3.send_keys("111111")
el4 = driver.find_element_by_id("com.yaojet.tma.goods:id/bt_test")
el4.click()

driver.quit()