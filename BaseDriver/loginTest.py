import unittest
from appium import webdriver
import os
import time

class Login(unittest.TestCase):

    def setUp(self):
        print("初始化")
        desired_cups = {}
        #设备平台
        desired_cups['platformName'] = 'Android'
        #设备系统版本
        desired_cups['platformVersion'] = '10'
        #设备名称
        desired_cups['deviceName'] = 'OPPO A5'
        desired_cups['udid'] = '58e8a185'
        desired_cups['appPackage'] = 'com.ayla.hotelsaas'
        desired_cups['appActivity'] = 'com.ayla.hotelsaas.ui.SPlashActivity'
        #desired_cups['appWaitActivity'] = 'com.ayla.hotelsaas.ui.ProjectListActivity'
        desired_cups['noReset'] = True
        #如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

        #启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_cups)

        #启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
        time.sleep(10)

    def test_login(self):
        print("进行登录")
        activity = self.driver.current_activity
        print(activity)
        time.sleep(2)
        username = self.driver.find_element_by_id('editCount')
        time.sleep(3)
        #username.clear()
        print("输入账号")
        username.send_keys('19988881234')
        password = self.driver.find_element_by_id('editPass')
        #password.clear()
        password.send_keys('123456')
        self.driver.find_element_by_id('submitBtn').click()
        self.driver.wait_activity(".ui.ProjectListActivity", 10)
        time.sleep(5)
        # title = self.driver.find_element_by_id('com.grandsoft.intercom:id/toolTitle')
        # if title is not None:
        #     print('login is success')
        # else:
        #     print('login is false')

    def tearDown(self):
        print("结束")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()