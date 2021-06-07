from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
import unittest, time
from loguru import logger

class MyInfoPage(ElementLoader):
    driver = AutoDriver()
    ProjectPage = ProjectPage()

    def __init__(self):
        ElementLoader.__init__(self, self.__class__.__name__)

    def into_myInfo(self):
        """
        进入个人中心页面
        :return:
        """
        #判断是否在项目列表页面，在则返回True
        flag = self.ProjectPage.is_project_page()
        if flag:
            into_btn = self.driver.find_element_until_visibility(self.locator("into_myinfo"))
            self.driver.click(into_btn)
        else:
            return "不在项目列表页面"

    def is_myInfoPage(self):
        """
        判断是否在个人中心页面
        :return:
        """
        flag = self.driver.is_element(self.locator("myinfo_flag"), 3)
        return flag

    def logout(self):
        """
        退出登录
        :return:
        """
        #判断是否在个人中心页面
        flag = self.is_myInfoPage()
        if flag:
            logout_btn = self.driver.find_element_until_visibility(self.locator("myinfo_logout"))
            self.driver.click(logout_btn)
            v_done = self.driver.find_element_until_visibility(self.locator("v_done"))
            self.driver.click(v_done)
        else:
            return "not found"
