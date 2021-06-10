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
    @allure.title("登录测试")
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
    @allure.title("新建项目测试")
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
    @allure.title("删除项目测试")
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
    @allure.title("修改房间名称测试")
    def test_04_changeRoomName(self):
        """
        用例描述：
        测试点：修改房间名称
        用例步骤：1、从项目列表进入房间，进入房间更多页，操作修改名称
        校验：1、获取修改后的房间title，与修改的name作校验
        :return:
        """
        #进入设备列表页面
        self.DevicePage.into_devicePage()
        #进入房间更多页
        self.DevicePage.into_room_more()
        NewName = str(random.randint(0,99)) + "楼_" + "房间_" + str(random.randint(0,99))
        self.DevicePage.set_room_name(NewName)
        #返回设备列表页面，获取其房间名称
        self.DevicePage.go_back()
        actual_name = self.DevicePage.get_roomName()
        assert actual_name == NewName, "修改房间名称失败，期望：%s, 实际：%s" % (NewName, actual_name)

    @allure.feature("设备管理模块")
    @allure.story("修改设备名称--正向用例")
    @allure.title("修改设备名称测试")
    def test_05_changeDeviceName(self):
        """
        用例描述：
        测试点：修改设备名称
        用例步骤：1、选择某个设备进去更多页
        校验：1、获取修改后的设备name，与修改的name作校验
        :return:
        """
        #进入设备列表页面
        self.DevicePage.into_devicePage()
        #选择第一个设备进入设备更多页
        con = self.DevicePage.into_deviceMore_page()
        print(con)
        NewName = "米兰_" + str(random.randint(0,99)) + "_设备_" + str(random.randint(0,99))
        self.DevicePage.set_device_name(NewName)
        #actual_toast = self.DevicePage.sucess_toast()
        self.DevicePage.back()
        actual_name = self.DevicePage.get_device_name()
        assert actual_name == NewName

    @allure.feature("设备管理模块")
    @allure.story("修改设备开关名称--正向用例")
    @allure.title("修改设备开关名称测试")
    def test_06_changeOnOffName(self):
        """
        用例描述：
        测试点：修改设备开关名称
        用例步骤：1、选择某个设备进入更多页，操作开关重命名修改
        校验：1、获取修改后的设备开关name，与修改的name作校验
        :return:
        """

    @allure.feature("设备管理模块")
    @allure.story("修改设备位置--正向用例")
    @allure.title("修改设备位置测试")
    def test_07_changeDeviceName(self):
        """
        用例描述：
        测试点：修改设备位置
        用例步骤：1、选择某个设备进入更多页，操作设备位置修改
        校验：1、获取修改后的设备位置，与修改的位置作校验/获取toast
        :return:
        """

    @allure.feature("设备管理模块")
    @allure.story("修改设备点位--正向用例")
    @allure.title("修改设备点位测试")
    def test_08_changeDeviceName(self):
        """
        用例描述：
        测试点：修改设备点位
        用例步骤：1、选择某个设备进入更多页，操作设备点位修改
        校验：1、获取修改后的点位，与修改的点位作校验
        :return:
        """


    @pytest.mark.skip(reason='skip testing this')
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
    @allure.story("编辑联动--正向用例")
    @allure.title("编辑一键联动测试")
    def test_10_edit_oneKeyRule(self):
        """
        用例描述：
        测试点：编辑一键联动
        用例步骤：1、编辑一键联动：名称及条件动作
        校验：1、拿到最新一键联动的名称与创建的名称做比较
        :return:
        """
        self.RulePage.into_rulePage()
        rule_name = "修改" + str(random.randint(0,99)) + "_" + "一键" + str(random.randint(0,99))
        self.RulePage.into_oneKey_page()
        self.RulePage.into_oneKey_rule()
        self.RulePage.set_rule_name(rule_name)


    @allure.feature("联动管理模块")
    @allure.story("删除联动--正向用例")
    @allure.title("删除一键联动测试")
    def test_09_del_oneKeyRule(self):
        """
        用例描述：
        测试点：删除一键联动
        用例步骤：1、删除一键联动
        校验：1、toast校验
        :return:
        """

    @allure.feature("联动管理模块")
    @allure.story("新建联动--正向用例")
    @allure.title("新建云端联动测试")
    def test_10_add_autoCloudRule(self):
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

    @allure.feature("联动管理模块")
    @allure.story("编辑联动--正向用例")
    @allure.title("编辑云端联动测试")
    def test_10_edit_autoCloudRule(self):
        """
        用例描述：
        测试点：编辑云端联动
        用例步骤：1、拿到最新建的云端联动，进行编辑：联动名称、动作、条件
        校验：1、拿到最新联动的名称与创建的名称做校验
        :return:
        """

    @allure.feature("联动管理模块")
    @allure.story("删除联动--正向用例")
    @allure.title("删除云端联动测试")
    def test_09_del_autoCloudRule(self):
        """
        用例描述：
        测试点：删除云端联动
        用例步骤：1、删除云端联动
        校验：1、toast校验
        :return:
        """

    @allure.feature("联动管理模块")
    @allure.story("新建联动--正向用例")
    @allure.title("新建罗马本地联动测试")
    def test_10_add_autoAylaLocalRule(self):
        """
        用例描述：
        测试点：新建罗马本地联动
        用例步骤：1、新建罗马本地联动
        校验：1、拿到最新联动的名称与创建的名称做校验
        :return:
        """

    @allure.feature("联动管理模块")
    @allure.story("新建联动--正向用例")
    @allure.title("新建米兰本地联动测试")
    def test_10_add_autoAliLocalRule(self):
        """
        用例描述：
        测试点：新建米兰本地联动
        用例步骤：1、新建米兰本地联动
        校验：1、拿到最新联动的名称与创建的名称做校验
        :return:
        """

