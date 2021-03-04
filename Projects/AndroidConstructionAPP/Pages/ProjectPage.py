from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
import unittest, time

class ProjectPage(ElementLoader, unittest.TestCase):
    driver = AutoDriver()

    def __init__(self):
        ElementLoader.__init__(self, self.__class__.__name__)

    def is_project_page(self):
        """用于判断是不是在项目页面，是返回True，不是返回False"""
        print("进入校验")
        flag = self.driver.is_element(self.locator("project_page_title"), 3)
        print(flag)
        return flag

    def get_project_name(self, num=0):
        """
        从项目列表中获取项目名称
        :param num: 项目列表序列，默认为第一个
        :return: 项目名称
        """
        project = self.driver.find_elements_until_visibility(self.locator("project_name"))
        name = project[num+1].text#num=0是"我的项目"标题
        return name

    def get_project_num(self):
        """
        从项目列表中获取项目个数
        :return: 项目数
        """
        project = self.driver.find_elements_until_visibility(self.locator("project_type"))
        number = len(project)
        return number

    def add_project(self, name = "", type=False):
        """
        创建项目，默认创建展箱
        :param name:项目名称
        :param type:项目类型默认为展厅
        :return:
        """
        add_project_btn = self.driver.find_element_until_visibility(self.locator("project_add_btn"))
        self.driver.click(add_project_btn)
        time.sleep(1)
        project_name_field = self.driver.find_element_until_visibility(self.locator("project_name_text"))
        self.driver.send_keys(project_name_field, name)
        if type:
            zt_btn = self.driver.find_element_until_visibility(self.locator("project_type_zt"))
            self.driver.click(zt_btn)
        save = self.driver.find_element_until_visibility(self.locator("project_save_btn"))
        self.driver.click(save)

    def intoProjectInfo(self):
        """进入项目详情页面"""
        #project_class = "android.widget.TextView"
        #project_btn = self.driver.get_text_ele(project_class, "验证导入")
        project_btn = self.driver.find_element_until_visibility(self.locator("project_btn"))
        time.sleep(1)
        self.driver.click(project_btn)









