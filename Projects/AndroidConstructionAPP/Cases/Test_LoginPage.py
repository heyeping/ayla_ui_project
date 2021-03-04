from BaseDriver.Driver import AutoDriver
from Projects.AndroidConstructionAPP.Pages.LoginPage import LoginPage
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Config.Config import *
import unittest
import time


class Test_LoginPage(unittest.TestCase):
    driver = AutoDriver()
    LoginPage = LoginPage()
    ProjectPage = ProjectPage()

    # 截图相关
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_by_base64())
        return True

    # 截图相关
    def cleanup(self):
        pass

    def setUp(self):
        print("登录页面：")
        self.imgs = []  # 截图相关
        self.addCleanup(self.cleanup)  # 截图相关
        time.sleep(2)

    def tearDown(self):
        # self.driver.click_device_btn(4)
        pass

    def test_01_login(self):
        """账号为空"""
        self.LoginPage.app_login(login_data['account_null'], login_data['passwd_null'])
        expected_toast = toast_data['account_null']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.account_null_toast()
        print("实际的toast为",actual_toast)
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_02_login(self):
        """密码为空"""
        self.LoginPage.app_login(login_data['account_01'], login_data['passwd_null'])
        expected_toast = toast_data['password_null']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.password_null_toast()
        print("实际的toast为", actual_toast)
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_03_login(self):
        """错误的账号"""
        self.LoginPage.app_login(login_data['account_error'], login_data['passwd_error'])
        #self.driver.wait_activity_display('.ui.LoginActivity')
        expected_toast = toast_data['account_error']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.account_error_toast()
        print("实际的toast为", actual_toast)
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_04_login(self):
        """错误的密码"""
        self.LoginPage.app_login(login_data['account_01'], login_data['passwd_error'])
        #self.driver.wait_activity_display('.ui.LoginActivity')
        expected_toast = toast_data['password_error']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.password_error_toast()
        print("实际的toast为", actual_toast)
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_05_register(self):
        """
        错误的账号
        """
        self.LoginPage.user_register(register_data['register_user_name'], register_data['register_account_error'], register_data['register_pass_01'])
        expected_toast = toast_data['register_account_error']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.register_account_error_toast()
        print("实际的toast为", actual_toast)
        time.sleep(2)
        self.LoginPage.back_login_page()
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_06_register(self):
        """
        用户名为空
        """
        self.LoginPage.user_register(register_data['register_user_name_null'], register_data['register_account_01'], register_data['register_pass_01'])
        expected_toast = toast_data['register_user_null']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.register_username_null_toast()
        print("实际的toast为", actual_toast)
        time.sleep(2)
        self.LoginPage.back_login_page()
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_07_register(self):
        """
        密码小于6位
        """
        self.LoginPage.user_register(register_data['register_user_name'], register_data['register_account_01'], register_data['register_pass_error'])
        expected_toast = toast_data['register_pass_error']
        print("期望的toast为", expected_toast)
        time.sleep(2)
        actual_toast = self.LoginPage.register_pass_error_toast()
        print("实际的toast为", actual_toast)
        time.sleep(2)
        self.LoginPage.back_login_page()
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_08_register(self):
        """注册成功"""
        self.LoginPage.user_register(register_data['register_username_02'], register_data['register_account_02'], register_data['register_pass_02'])
        self.driver.wait_activity_display(".ui.LoginActivity")
        expected_toast = toast_data['register_succ']
        print("期望的toast为", expected_toast)
        time.sleep(4)
        actual_toast = self.LoginPage.register_succ_toast()
        print("实际的toast为", actual_toast)
        assert actual_toast == expected_toast, "验证码校验有问题，期望: %s, 实际: %s" % (expected_toast, actual_toast)

    def test_09_login(self):
        """登录成功"""
        self.LoginPage.app_login(login_data['account_01'], login_data['passwd_01'])
        flag = self.ProjectPage.is_project_page()
        assert flag, '登录失败'


