#@project:  ayla_ui_project
#@author: heyeping
#@file: Test_RulePage.py
#@ide: PyCharm
#@time: 2021/2/25 6:31 PM

from BaseDriver.Driver import AutoDriver
from Projects.AndroidConstructionAPP.Pages.RulePage import RulePage
from Projects.AndroidConstructionAPP.Config.Config import *
import unittest
import time,random

class Test_RulePage(unittest.TestCase):
    driver = AutoDriver()
    RulePage = RulePage()
    RulePage.into_rulePage()

    # 截图相关
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_by_base64())
        return True

    # 截图相关
    def cleanup(self):
        pass

    def setUp(self):
        print("场景页面：")
        self.imgs = []  # 截图相关
        self.addCleanup(self.cleanup)  # 截图相关
        time.sleep(2)


    def tearDown(self):
        # self.driver.click_device_btn(4)
        pass

    def test_01_add_oneKeyRule(self):
        """新建一键联动"""
        rule_name = "一键联动" + str(random.randint(0,99))
        self.RulePage.into_oneKey_page()
        self.RulePage.into_cloud_rule()
        self.RulePage.set_rule_name(rule_name)
        self.RulePage.add_one_key_type()
        self.RulePage.add_actionOrCondition(0,0,0,1,1)
        self.RulePage.save_rule()
        actual_name = self.RulePage.get_rule_name()
        assert actual_name == rule_name, "新建一键联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)

    def test_02_add_autoCloudRule(self):
        """新建云端自动化联动"""
        rule_name = "云端联动" + str(random.randint(0,9999))
        self.RulePage.into_autoRule_page()
        self.RulePage.into_cloud_rule()
        self.RulePage.set_rule_name(rule_name)
        self.RulePage.add_actionOrCondition(0,0,0,0,1)
        self.RulePage.add_actionOrCondition(4,0,0,1,1)
        self.RulePage.save_rule()
        actual_name = self.RulePage.get_rule_name()
        assert actual_name == rule_name, "新建云端自动化联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)


