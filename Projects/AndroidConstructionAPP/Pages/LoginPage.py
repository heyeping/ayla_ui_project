#coding= utf-8
from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
import unittest,time,allure

class LoginPage(ElementLoader):
    driver = AutoDriver()

    def __init__(self):
        ElementLoader.__init__(self, self.__class__.__name__)

    def login_user_field(self, user_ele):
        username_field = self.driver.find_element_until_visibility(self.locator("username_field"))
        return username_field

    def login_pass_field(self, user_pass):
        password_field = self.driver.find_element_until_visibility(self.locator("password_field"))
        return password_feild

    def login_btn(self, loginBtn):
        login_btn = self.driver.find_element_until_visibility(self.locator("login_button"))
        return login_btn

    @allure.step("登录")
    def app_login(self, username, password):
        """
        登录APP
        :param username: 用户名
        :param password: 密码
        :return:
        """
        username_field = self.driver.find_element_until_visibility(self.locator("username_field"))
        self.driver.send_keys(username_field, username)
        password_field = self.driver.find_element_until_visibility(self.locator("password_field"))
        self.driver.send_keys(password_field, password)
        time.sleep(2)
        login_btn = self.driver.find_element_until_visibility(self.locator("login_button"))
        self.driver.click(login_btn)

    @allure.step("注册账号")
    def user_register(self, register_user_name, register_account, register_pass):
        """
        注册账号
        :param register_user_name: 用户名
        :param register_account: 账号
        :param register_pass: 密码
        :return:
        """
        register_page_btn = self.driver.find_element_until_visibility(self.locator("register_page_btn"))
        self.driver.click(register_page_btn)#进入注册页面
        register_user_name_field = self.driver.find_element_until_visibility(self.locator("register_user_name"))
        self.driver.clear(register_user_name_field)
        self.driver.send_keys(register_user_name_field,register_user_name)
        register_account_field = self.driver.find_element_until_visibility(self.locator("register_account"))
        self.driver.clear(register_account_field)
        self.driver.send_keys(register_account_field, register_account)
        register_pass_field = self.driver.find_element_until_visibility(self.locator("register_pass"))
        self.driver.clear(register_pass_field)
        self.driver.send_keys(register_pass_field, register_pass)
        register_btn = self.driver.find_element_until_visibility(self.locator("register_btn"))
        self.driver.click(register_btn)

    @allure.step("返回登录页面")
    def back_login_page(self):
        """
        返回登录页面
        :return:
        """
        back_login = self.driver.find_element_until_visibility(self.locator("login_page_btn"))
        self.driver.click(back_login)

    @allure.step("判断是否在登录页面")
    def is_in_login_page(self):
        """用于判断是否是在登录页面"""
        flag = self.driver.is_element(self.locator("register_page_btn"), 3)
        return flag

    #以下用于toast验证
    def account_null_toast(self):
        """
        账号为空
        :return:
        """
        #toast = self.driver.is_toast_exist(self.locator("account_null")).text
        toast = self.driver.get_toast("登录账号不能为空")
        if toast == "Toast no found":
            return "获取不到toast"
        else:
            toast_text = toast.text
        #print(toast_text)
        return toast_text

    def password_null_toast(self):
        """
        密码为空
        :return:
        """
        #toast = self.driver.is_toast_exist(self.locator("password_null")).text
        toast_text = self.driver.get_toast("登陆密码不能为空").text
        return toast_text

    def password_error_toast(self):
        """
        密码错误
        :return:
        """
        toast_text = self.driver.get_toast("密码错误").text
        #print(toast)
        return toast_text

    def account_error_toast(self):
        """
        错误的账号
        :return:
        """
        toast = self.driver.get_toast("请输入正确的邮箱或手机号码").text
        return toast

    def account_no_exist_toast(self):
        """
        不存在的用户账号或错误的密码
        :return:
        """
        toast = self.driver.find_element_until_visibility(self.locator("error_show")).text
        return toast

    def register_account_error_toast(self):
        """
        错误格式的账号
        :return:
        """
        toast = self.driver.get_toast("请输入正确的邮箱或手机号码").text
        return toast

    def register_username_null_toast(self):
        """
        注册用户名为空
        :return:
        """
        toast = self.driver.get_toast("用户名不能为空").text
        return toast

    def register_pass_error_toast(self):
        """
        不符合规范的密码
        :return:
        """
        toast = self.driver.get_toast("密码长度不能少于6位").text
        return toast

    def register_succ_toast(self):
        """注册成功"""
        toast = self.driver.get_toast("注册成功").text
        return toast

