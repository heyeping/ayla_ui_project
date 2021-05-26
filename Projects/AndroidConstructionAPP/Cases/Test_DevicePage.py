#@project:  ayla_ui_project
#@author: heyeping
#@file: Test_DevicePage.py.py
#@ide: PyCharm
#@time: 2021/5/26 10:52 AM

from BaseDriver.Driver import AutoDriver
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Pages.DevicesPage import DevicesPage
from Projects.AndroidConstructionAPP.Config.Config import *
import pytest,allure
import time, random

class Test_DevicePage():
    driver = AutoDriver()
    ProjectPage = ProjectPage()
    DevicesPage = DevicesPage()

    @allure.feature("设备管理模块")
    @allure.story("修改设备名称--正向用例")
    @allure.title("修改设备测试")
    def test_01_editDeviceName(self):
        """
        用例描述
        测试点：修改设备名称
        用例步骤：1、选择某个设备，2、进入设备更多页，3、操作修改设备名称
        校验：1、获取修改后的设备名称与device_name做比较
        :return:
        """
