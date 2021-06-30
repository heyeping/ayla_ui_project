from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
import unittest, time
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Pages.RoomPage import RoomPage
import allure

class DevicePage(ElementLoader):
    driver = AutoDriver()
    #ElementLoader = ElementLoader()
    ProjectPage = ProjectPage()
    RoomPage = RoomPage()
    #device_names = driver.find_elements_until_visibility(ElementLoader.locator("device_name"))
    #more_btn = driver.find_element_until_visibility(ElementLoader.locator("room_more_btn"))

    def __init__(self):
        ElementLoader.__init__(self, self.__class__.__name__)

    @allure.step("进入设备列表页面")
    def into_devicePage(self):
        """
        进入设备列表页面
        :return:
        """
        #进入房间列表页面
        self.ProjectPage.intoProjectInfo()
        #进入设备列表页面
        self.RoomPage.into_rommPage()
        devicePage_btn = self.driver.find_element_until_visibility(self.locator("device_page"))
        self.driver.click(devicePage_btn)

    @allure.step("返回操作")
    def back(self):
        self.driver.click_device_btn(4)

    @allure.step("获取当前房间的name")
    def get_roomName(self):
        """获取当前房间name"""
        roomName_btn = self.driver.find_element_until_visibility(self.locator("roomName"))
        roomName = roomName_btn.text
        return roomName

    @allure.step("判断是否在device页面")
    def is_in_devicePage(self):
        """
        判断是否在device页面
        :return:
        """
        flag = self.driver.is_element(self.locator("device_page"))
        return flag

    @allure.step("获取设备名称")
    def get_device_name(self, num=0):
        """
        获取设备名称
        :param num:默认获取第一个设备
        :return:
        """
        device_names = self.driver.find_elements_until_visibility(self.locator("device_name"))
        device_name = device_names[num].text
        return device_name

    @allure.step("获取设备数")
    def get_device_num(self):
        """
        获取设备
        :return:设备数
        """
        #判断是否存在tv_device_online_status元素，不存在就返回0
        device_names = self.driver.find_elements_until_visibility(self.locator("device_name"))
        flag = self.driver.is_element(self.locator("device_status"))
        if flag:
            device_nums = len(device_names)
        else:
            device_nums = 0
        return device_nums

    @allure.step("设置房间名称{roomName}")
    def set_room_name(self, roomName=None):
        """
        设置房间名称
        :return:
        """
        room_name_btn = self.driver.find_element_until_visibility(self.locator("room_name_btn"))
        self.driver.click(room_name_btn)
        roomName_text = self.driver.find_element_until_visibility(self.locator("name_text"))
        self.driver.send_keys(roomName_text, roomName)
        done_btn = self.driver.find_element_until_visibility(self.locator("done_btn"))
        self.driver.click(done_btn)

    @allure.step("进入房间更多页")
    def into_room_more(self):
        """
        进入房间更多页
        :return:
        """
        roomMore_btn = self.driver.find_element_until_visibility(self.locator("room_more_btn"))
        self.driver.click(roomMore_btn)
        # flag = self.is_in_devicePage()
        # if flag:
        #
        # else:
        #     return "not in devicePage"

    @allure.step("判断是否在房间更多页")
    def is_in_roomMorePage(self):
        """
        判断是否在房间更多页
        :return:
        """
        flag = self.driver.is_element(self.locator("room_name_btn"))
        return flag

    @allure.step("移除房间")
    def del_room(self):
        """
        删除房间
        :return:
        """
        flag = self.is_in_roomMorePage()
        if flag:
            remove_btn = self.driver.find_element_until_visibility(self.locator("btn_remove_room"))
            self.driver.click(remove_btn)
            v_done = self.driver.find_element_until_visibility(self.locator("done_btn"))
            self.driver.click(v_done)
        else:
            return "not in roomMorePage"

    @allure.step("进入方案设置页")
    def into_plan_page(self):
        """
        进入方案分享页
        :return:
        """
        rl_room_plan = self.driver.find_element_until_visibility(self.locator("rl_room_plan"))
        rl_room_plan.click()

    @allure.step("添加方案")
    def add_plan(self, plan_code=None):
        """
        添加方案
        :param plan_code: 方案包
        :return:
        """
        #判断房间是否已使用过方案，通过room_plan_type元素的text进行判断
        room_plan_type_ele = self.driver.find_element_until_visibility(self.locator("room_plan_type"))
        room_plan_type_text = room_plan_type_ele.text
        if room_plan_type_text == "未使用":
            #操作添加方案按钮
            add_plan_ele = self.driver.find_element_until_visibility(self.locator("add_plan"))
            self.driver.click(add_plan_ele)
            #输入方案包
            code_text = self.driver.find_element_until_visibility(self.locator("code_text"))
            self.driver.send_keys(code_text, plan_code)
            #操作导入
            done_btn = self.driver.find_element_until_visibility(self.locator("room_more_btn"))
            self.driver.click(done_btn)
        elif room_plan_type_text == "已使用":
            # 操作更换方案按钮
            add_plan_ele = self.driver.find_element_until_visibility(self.locator("add_plan"))
            self.driver.click(add_plan_ele)
            #确定清空方案
            v_done = self.driver.find_element_until_visibility(self.locator("done_btn"))
            self.driver.click(v_done)
            # 输入方案包
            code_text = self.driver.find_element_until_visibility(self.locator("code_text"))
            self.driver.send_keys(code_text, plan_code)
            # 操作导入
            done_btn = self.driver.find_element_until_visibility(self.locator("room_more_btn"))
            self.driver.click(done_btn)

    @allure.step("分享方案")
    def get_share_plan(self):
        """
        分享方案
        :return:
        """
        #操作分享
        share_btn = self.driver.find_element_until_visibility(self.locator("share_plan"))
        self.driver.click(share_btn)
        #获取分享码
        share_code_flag = self.driver.is_element(self.locator("plan_code"))
        if share_code_flag:
            share_code_btn = self.driver.find_element_until_visibility(self.locator("plan_code"))
            share_code = share_code_btn.text
        else:
            share_code = None
        return share_code

    @allure.step("判断导入方案是否成功")
    def is_add_plan_succ(self):
        """
        判断待添加设备存在
        :return:
        """
        flag = self.driver.is_element(self.locator("device_no_add"))
        return flag

    @allure.step("返回房间列表页")
    def go_to_room_list(self):
        """
        前往房间列表
        :return:
        """
        v_done = self.driver.find_element_until_visibility(self.locator("done_btn"))
        self.driver.click(v_done)

    @allure.step("进入设备更多页")
    def into_deviceMore_page(self, num=0):
        """
        进入设备更多页面，默认第一个设备
        :param num: 默认第一个设备
        :return:
        """
        device_names = self.driver.find_elements_until_visibility(self.locator("device_name"))
        self.driver.click(device_names[num])
        #time.sleep(2)
        #尝试切换context，用class_name不行，不切context使用原生的xpath可以，前提是包要确保需要开启webview远程调试功能：this.appView.setWebContentsDebuggingEnabled(true);
        #context = self.driver.get_all_contexts()
        #self.driver.switch_to_context("WEBVIEW_com.ayla.hotelsaas")
        #return context
        #判断当前是否存在设备更多页，false则是进入单控页
        flag = self.driver.is_element(self.locator("device_more_title"))
        if flag:
            print("已进入设备更多页")
        else:
            more_btn = self.driver.find_element_until_visibility(self.locator("more_btn"))
            self.driver.click(more_btn)

    @allure.step("设置设备名称")
    def set_device_name(self, name=None):
        """
        设置设备名称
        :param name:
        :return:
        """
        #self.into_deviceMore_page(0)
        device_name_btn = self.driver.find_element_until_visibility(self.locator("device_name"))
        self.driver.click(device_name_btn)
        device_name_text = self.driver.find_element_until_visibility(self.locator("name_text"))
        self.driver.send_keys(device_name_text, name)
        done_btn = self.driver.find_element_until_visibility(self.locator("done_btn"))
        self.driver.click(done_btn)

    @allure.step("设置开关重命名")
    def set_device_function_name(self, name=None):
        """
        设置开关重命名
        :param name:
        :return:
        """
        device_function_name = self.driver.find_element_until_visibility(self.locator("device_function_name"))
        self.driver.click(device_function_name)
        tv_nicknames = self.driver.find_elements_until_visibility(self.locator("tv_nickname"))
        self.driver.click(tv_nicknames[0])
        nickname_text = self.driver.find_element_until_visibility(self.locator("name_text"))
        self.driver.send_keys(nickname_text, name)
        done_btn = self.driver.find_element_until_visibility(self.locator("done_btn"))
        self.driver.click(done_btn)

    @allure.step("设置设备点位")
    def set_device_pointName(self, name=None):
        """
        设置设备点位
        :param name:
        :return:
        """
        rl_location = self.driver.find_element_until_visibility(self.locator("rl_location"))
        self.driver.click(rl_location)
        rl_region_name = self.driver.find_element_until_visibility(self.locator("rl_region_name"))
        self.driver.click(rl_region_name)
        region_name_text = self.driver.find_element_until_visibility(self.locator("name_text"))
        self.driver.send_keys(region_name_text, name)
        done_btn = self.driver.find_element_until_visibility(self.locator("done_btn"))
        self.driver.click(done_btn)

    @allure.step("设置设备位置")
    def set_device_location(self, num=0):
        """
        设置设备位置
        :param num: 默认设置第一个
        :return:
        """
        rl_location = self.driver.find_element_until_visibility(self.locator("rl_location"))
        self.driver.click(rl_location)
        device_location = self.driver.find_element_until_visibility(self.locator("device_location"))
        self.driver.click(device_location)
        device_location_types = self.driver.find_elements_until_visibility(self.locator("device_location_type"))
        self.driver.click(device_location_types[num])

    @allure.step("返回操作")
    def go_back(self):
        """
        返回操作
        :return:
        """
        iv_left = self.driver.find_element_until_visibility(self.locator("iv_left"))
        self.driver.click(iv_left)

    # 以下用于toast验证
    def remove_toast(self):
        """
        移除成功
        :return:
        """
        toast = self.driver.get_toast("移除成功").text
        return toast

    def sucess_toast(self):
        """
        修改成功
        :return:
        """
        toast = self.driver.get_toast("修改成功").text
        return toast

    def add_sucess_toast(self):
        """
        导入成功
        :return:
        """
        toast = self.driver.get_toast("导入成功").text






