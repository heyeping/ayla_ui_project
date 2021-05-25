from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
import unittest, time
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Pages.RoomPage import RoomPage

class RulePage(ElementLoader, unittest.TestCase):
    driver = AutoDriver()
    ProjectPage = ProjectPage()
    RoomPage = RoomPage()

    def __init__(self):
        ElementLoader.__init__(self, self.__class__.__name__)

    def into_rulePage(self):
        """
        进入规则模块
        :return:
        """
        # 进入房间列表页面
        self.ProjectPage.intoProjectInfo()
        # 进入设备列表页面
        self.RoomPage.into_rommPage()
        #进入规则列表页面
        rulePage_btn = self.driver.find_element_until_visibility(self.locator("rule_page"))
        self.driver.click(rulePage_btn)

    def into_oneKey_page(self):
        """
        进入一键联动列表
        :return:
        """
        onekey_page_btn = self.driver.find_element_until_visibility(self.locator("rule_onekey_list"))
        self.driver.click(onekey_page_btn)

    def into_autoRule_page(self):
        """
        进入自动化列表页面
        :return:
        """
        autoRule_page_btn = self.driver.find_element_until_visibility(self.locator("rule_auto_list"))
        self.driver.click(autoRule_page_btn)

    def get_rule_name(self,num=0):
        """
        获取联动名称
        :param num:默认为第一个
        :return: 联动名称
        """
        rule_names = self.driver.find_elements_until_visibility(self.locator("device_names"))
        rule_name = rule_names[num].text
        return rule_name

    def get_oneKey_rule_num(self):
        """
        从一键联动列表中获取一键联动的个数
        :return: 一键联动的个数
        """
        oneKey_rules = self.driver.find_elements_until_visibility(self.locator("rule_names"))
        oneKey_rule_num = len(oneKey_rules)
        return oneKey_rule_num

    def into_cloud_rule(self):
        """
        进入添加云端联动页面
        :return:
        """
        add_btn = self.driver.find_element_until_visibility(self.locator("add_btn"))
        self.driver.click(add_btn)
        cloud_rule_btn = self.driver.find_element_until_visibility(self.locator("cloud_rule_btn"))
        self.driver.click(cloud_rule_btn)

    def into_local_rule(self):
        """
        进入添加本地联动页面
        :return:
        """
        add_btn = self.driver.find_element_until_visibility(self.locator("add_btn"))
        self.driver.click(add_btn)
        local_rule_btn = self.driver.find_element_until_visibility(self.locator("local_rule_btn"))
        self.driver.click(local_rule_btn)

    def set_rule_name(self, ruleName=None):
        """
        设置规则名称
        :return:
        """
        rule_name_btn = self.driver.find_element_until_visibility(self.locator("rule_name"))
        self.driver.click(rule_name_btn)
        rule_name_text = self.driver.find_element_until_visibility(self.locator("rule_name_field"))
        self.driver.send_keys(rule_name_text, ruleName)
        ensure_btn = self.driver.find_element_until_visibility(self.locator("done_btn"))
        self.driver.click(ensure_btn)

    def add_one_key_type(self):
        """
        条件添加一键执行按钮
        :return:
        """
        add_condition_btn = self.driver.find_element_until_visibility(self.locator("add_condition_btn"))
        self.driver.click(add_condition_btn)
        type_one_key = self.driver.find_element_until_visibility(self.locator("type_one_key"))
        self.driver.click(type_one_key)



    def add_actionOrCondition(self, device_num=0, function1_num=0, function2_num=0, flag_AC=0, AC_num=1):
        """
        添加条件或动作
        :param device_num:选择的设备，默认为第一个
        :param function1_num:选择功能，默认第一个
        :param function2_num:选择最终功能，默认第一个
        :param flag_AC:默认为添加条件，值不为0是添加动作
        :param AC_num:添加多少个，默认添加1个
        :return:
        """
        i = 0
        while i < AC_num:

            if flag_AC==0:
                """进入的是添加条件页面"""
                add_condition_btn = self.driver.find_element_until_visibility(self.locator("add_condition_btn"))
                self.driver.click(add_condition_btn)
            else:
                """进入的是添加动作页面"""
                add_action_btn = self.driver.find_element_until_visibility(self.locator("add_action_btn"))
                self.driver.click(add_action_btn)
            #进入选择设备功能页面
            device_changed_btn = self.driver.find_element_until_visibility(self.locator("type_device_changed"))
            self.driver.click(device_changed_btn)
            flag = self.driver.is_element(self.locator("device_names"))
            if flag:
                device_names = self.driver.find_elements_until_visibility(self.locator("device_names"))
                self.driver.click(device_names[device_num])
                function_name_btn = self.driver.find_elements_until_visibility(self.locator("function_name_btn"))
                self.driver.click(function_name_btn[function1_num])
                cb_function_checkeds = self.driver.find_elements_until_visibility(self.locator("cb_function_checked"))
                self.driver.click(cb_function_checkeds[function2_num])
                save_btn = self.driver.find_element_until_visibility(self.locator("save_btn"))
                self.driver.click(save_btn)
            else:
                print("暂无设备")
            i += 1

    def save_rule(self):
        """
        保存操作
        :return:
        """
        save_btn = self.driver.find_element_until_visibility(self.locator("save_btn"))
        self.driver.click(save_btn)

    def rule_nums(self):
        """
        统计联动的个数：通过tv_device_name元素的个数统计
        判断是否存在tv_device_name元素
        :return:
        """
        flag = self.driver.is_element(self.locator("device_names"))
        if flag:
            rule = self.driver.find_elements_until_visibility(self.locator("device_names"))
            rule_nums = len(oneKey)
        else:
            rule_nums = 0
        return rule_nums

    def get_rule_status(self, mun=0):
        """
        获取某个联动当前的状态：开启/关闭
        :param num:默认第一个
        :return:
        """
        flag = self.driver.is_element(self.locator("device_names"))
        if flag:
            rules = self.driver.find_elements_until_visibility(self.locator("rule_status"))
            rule_status = rules[mun].text
            return rule_status
        else:
            return "no rule"

    def change_rule_status(self, num=0):
        """
        改变联动状态
        :param mun:默认第一个
        :return:
        """
        flag = self.driver.is_element(self.locator("device_names"))
        if flag:
            status = self.driver.find_elements_until_visibility(self.locator("rule_status"))
            self.driver.click(status[num])
        else:
            return "no rule"

    def into_auto_rule(self, num=0):
        """
        进入原有的联动编辑页
        :param num: 默认第一个
        :return:
        """
        rules = self.driver.find_elements_until_visibility(self.locator("device_names"))
        self.driver.click(rules[num])

    def del_rule(self):
        """
        删除联动
        :return:
        """
        rule_del_btn = self.driver.swipeElement("rule_del_btn")
        self.driver.click(rule_del_btn)


