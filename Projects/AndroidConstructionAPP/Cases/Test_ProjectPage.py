#@project:  ayla_ui_project
#@author: heyeping
#@file: Test_ProjectPage.py.py
#@ide: PyCharm
#@time: 2021/5/25 11:26 AM

from BaseDriver.Driver import AutoDriver
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Config.Config import *
import pytest,allure
import time, random

class Test_ProjectPage():
    driver = AutoDriver()
    ProjectPage = ProjectPage()

    @allure.feature("项目管理模块")
    @allure.story("新建项目--正向用例")
    @allure.title("新建项目场景测试")
    def test_01_addProject(self):
        """
        用例描述：
        测试点：新建项目
        用例步骤：1、创建新项目
        检验：1、获取当前最新项目的title，与project_name做比较
        :return:
        """
        project_name = "项目" + str(random.randint(0,99))
        # with allure.step("step1: 统计当前项目个数"):
        #     old_project = self.ProjectPage.get_project_num()
        # except_num = old_project + 1

        with allure.step("step1: 新建项目"):
            self.ProjectPage.add_project(project_name)

        with allure.step("step2: 获取当前最新的项目名称"):
            actual_name = self.ProjectPage.get_project_name()

        with allure.step("step3: 断言"):
            assert actual_name == project_name
