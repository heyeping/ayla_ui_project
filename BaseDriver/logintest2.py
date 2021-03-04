import time

from appium import webdriver
from selenium.webdriver.common.by import By


desired_capabilities = {
        'platformName': 'Android',
        'platformVersion': '8.1.0',
        'deviceName': '58e8a185',
        'appPackage': 'com.ayla.hotelsaas',
        'appActivity': '.ui.SPlashActivity',
        'noReset': True
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(10)

name = '18002549655'
pwd = 'Hyp123456'
in_name = driver.find_element(By.ID, 'com.ayla.hotelsaas:id/editCount')
# in_name.clear()
in_name.send_keys(name)
in_pwd = driver.find_element(By.ID, 'com.ayla.hotelsaas:id/editPass')
# in_pwd.clear()
in_pwd.send_keys(pwd)
# driver.save_screenshot('login.png')

driver.find_element(By.ID, 'com.ayla.hotelsaas:id/submitBtn').click()

time.sleep(5)
driver.quit()

