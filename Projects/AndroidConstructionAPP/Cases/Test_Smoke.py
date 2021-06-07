#@project:  ayla_ui_project
#@author: heyeping
#@file: Test_Smoke.py
#@ide: PyCharm
#@time: 2021/6/1 10:38 AM

from BaseDriver.Driver import AutoDriver
from Projects.AndroidConstructionAPP.Pages.LoginPage import LoginPage
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Pages.RoomPage import RoomPage
from Projects.AndroidConstructionAPP.Pages.DevicePage import DevicePage
from Projects.AndroidConstructionAPP.Pages.RulePage import RulePage
from Projects.AndroidConstructionAPP.Pages.MyInfoPage import MyInfoPage
from Projects.AndroidConstructionAPP.Config.Config import *
import pytest,allure, time
import time, random

class TestSmoke():
    """
    冒烟测试：正向流程
    """
    driver = AutoDriver()
    LoginPage = LoginPage()
    ProjectPage = ProjectPage()
    RoomPage = RoomPage()
    DevicePage = DevicePage()
    RulePage = RulePage()
    MyInfoPage = MyInfoPage()

    @pytest.mark.skip(reason='skip testing this')
    @allure.feature("登录模块")
    @allure.story("登录--正向用例")
    @allure.title("登录场景测试")
    def test_01_login(self):
        """
        用例描述：
        测试点：登录
        用例步骤：1、调起app，判断app是否处于登录页，否则则操作logout
        检验：1、操作登录后判断是否进入项目列表页面
        :return:
        """
        #判断是否在登录页
        flag = self.LoginPage.is_in_login_page()
        if flag:
            self.LoginPage.app_login("18002549655", "Hyp123456")
        else:
            self.MyInfoPage.into_myInfo()
            self.MyInfoPage.logout()
            self.LoginPage.app_login("18002549655", "Hyp123456")
        flag_assert = self.ProjectPage.is_project_page()
        assert flag_assert, '登录失败'


    @allure.feature("项目管理模块")
    @allure.story("新建项目--正向用例")
    @allure.title("新建项目场景测试")
    def test_02_addProject(self):
        """
        用例描述：
        测试点：新建项目
        用例步骤：1、创建新项目
        检验：1、获取当前最新项目的title，与project_name做比较
        :return:
        """
        project_name = "项目" + str(random.randint(0, 99))
        # with allure.step("step1: 统计当前项目个数"):
        #     old_project = self.ProjectPage.get_project_num()
        # except_num = old_project + 1

        with allure.step("step1: 新建项目"):
            self.ProjectPage.add_project(project_name)

        with allure.step("step2: 获取当前最新的项目名称"):
            actual_name = self.ProjectPage.get_project_name()

        with allure.step("step3: 断言"):
            assert actual_name == project_name

    @allure.feature("项目管理模块")
    @allure.story("删除项目--正向用例")
    @allure.title("删除项目场景测试")
    def test_03_removeProject(self):
        """
        用例描述：
        测试点：删除项目
        用例步骤：1、选择上个用例新建的项目，进入对应房间，操作删除项目
        检验：1、
        :return:
        """
        self.DevicePage.into_devicePage()
        self.DevicePage.into_room_more()
        self.DevicePage.del_room()
        actual_toast = self.DevicePage.remove_toast()
        assert actual_toast == '移除成功'

    @allure.feature("房间管理模块")
    @allure.story("修改房间名称--正向用例")
    @allure.title("修改房间名称场景测试")
    def test_03_changeRoomName(self):
        """
        用例描述：
        测试点：修改房间名称
        用例步骤：1、从项目列表进入房间，进入房间更多页，操作修改名称
        校验：1、获取修改后的房间title，与修改的name作校验
        :return:
        """
        pass

    @allure.feature("设备管理模块")
    @allure.story("修改设备名称--正向用例")
    @allure.title("修改设备名称场景测试")
    def test_03_changeDeviceName(self):
        """
        用例描述：
        测试点：修改设备名称
        用例步骤：1、选择某个设备进去更多页
        校验：1、获取修改后的设备name，与修改的name作校验
        :return:
        """
        pass



    @pytest.mark.skip(reason='skip testing this')
    @allure.feature("联动管理模块")
    @allure.story("新建联动--正向用例")
    @allure.title("新建一键联动测试")
    def test_04_add_oneKeyRule(self):
        """
        用例描述：
        测试点：新建一键联动
        用例步骤：1、新建一键联动
        校验：1、拿到最新一键联动的名称与创建的名称做比较
        :return:
        """
        self.RulePage.into_rulePage()
        rule_name = "一键联动" + str(random.randint(0,99))
        self.RulePage.into_oneKey_page()
        self.RulePage.into_cloud_rule()
        self.RulePage.set_rule_name(rule_name)
        self.RulePage.add_one_key_type()
        self.RulePage.add_actionOrCondition(0,0,0,1,1)
        self.RulePage.save_rule()
        actual_name = self.RulePage.get_rule_name()
        assert actual_name == rule_name, "新建一键联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)

    @allure.feature("联动管理模块")
    @allure.story("新建联动--正向用例")
    @allure.title("新建云端联动测试")
    def test_02_add_autoCloudRule(self):
        """
        用例描述：
        测试点：新建云端联动
        用例步骤：1、新建云端联动
        校验：1、拿到最新联动的名称与创建的名称做校验
        :return:
        """
        rule_name = "云端联动" + str(random.randint(0,9999))
        self.RulePage.into_autoRule_page()
        self.RulePage.into_cloud_rule()
        self.RulePage.set_rule_name(rule_name)
        self.RulePage.add_actionOrCondition(0,0,0,0,1)
        self.RulePage.add_actionOrCondition(4,0,0,1,1)
        self.RulePage.save_rule()
        actual_name = self.RulePage.get_rule_name()
        assert actual_name == rule_name, "新建云端自动化联动失败, 期望: %s, 实际: %s" % (rule_name, actual_name)

