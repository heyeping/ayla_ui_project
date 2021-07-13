#@project:  ayla_ui_project
#@author: heyeping
#@file: Test_RulePage.py
#@ide: PyCharm
#@time: 2021/2/25 6:31 PM

from BaseDriver.Driver import AutoDriver
from Projects.AndroidConstructionAPP.Pages.RulePage import RulePage
from Projects.AndroidConstructionAPP.Pages.DevicePage import DevicePage
from Projects.AndroidConstructionAPP.Config.Config import *
import unittest
import time,random

class Test_RulePage():
    driver = AutoDriver()
    RulePage = RulePage()
    DevicePage = DevicePage()
    DevicePage.into_devicePage()

    @allure.feature("联动管理模块")
    @allure.story("新建联动--正向用例")
    @allure.title("新建一键联动测试")
    def test_09_add_oneKeyRule(self):
        """
        用例描述：
        测试点：新建一键联动
        用例步骤：1、新建一键联动
        校验：1、拿到最新一键联动的名称与创建的名称做比较
        :return:
        """
        self.RulePage.into_rulePage()
        rule_name = "一键联动" + str(random.randint(0, 99))
        self.RulePage.into_oneKey_page()
        self.RulePage.into_cloud_rule()
        self.RulePage.set_rule_name(rule_name)
        self.RulePage.add_one_key_type()
        self.RulePage.add_actionOrCondition("cloud", 0, 0, 0, 1, 1)
        self.RulePage.save_rule()
        actual_name = self.RulePage.get_rule_name()
        assert actual_name == rule_name, "新建一键联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)

    # def test_01_add_oneKeyRule(self):
    #     """新建一键联动"""
    #     rule_name = "一键联动" + str(random.randint(0,99))
    #     self.RulePage.into_oneKey_page()
    #     self.RulePage.into_cloud_rule()
    #     self.RulePage.set_rule_name(rule_name)
    #     self.RulePage.add_one_key_type()
    #     self.RulePage.add_actionOrCondition(0,0,0,1,1)
    #     self.RulePage.save_rule()
    #     actual_name = self.RulePage.get_rule_name()
    #     assert actual_name == rule_name, "新建一键联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)
    #
    # def test_02_add_autoCloudRule(self):
    #     """新建云端自动化联动"""
    #     rule_name = "云端联动" + str(random.randint(0,9999))
    #     self.RulePage.into_autoRule_page()
    #     self.RulePage.into_cloud_rule()
    #     self.RulePage.set_rule_name(rule_name)
    #     self.RulePage.add_actionOrCondition(0,0,0,0,1)
    #     self.RulePage.add_actionOrCondition(4,0,0,1,1)
    #     self.RulePage.save_rule()
    #     actual_name = self.RulePage.get_rule_name()
    #     assert actual_name == rule_name, "新建云端自动化联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)


