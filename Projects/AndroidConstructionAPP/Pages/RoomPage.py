from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
import unittest, time
import allure

class RoomPage(ElementLoader, unittest.TestCase):
    driver = AutoDriver()

    def __init__(self):
        ElementLoader.__init__(self, self.__class__.__name__)

    @allure.step("判断是否在房间列表页面")
    def is_room_page(self):
        """判断是否在房间列表页面，是返回True，不是返回False"""
        flag = self.driver.is_element(self.locator("room_page"), 3)

    #@allure.step("进入房间页面")
    def into_rommPage(self):
        """进入房间页面"""
        #room_class = "android.widget.RelativeLayout"
        #room_btn = self.driver.get_text_ele(room_class,"多个本地延时QQ")
        room_btn = self.driver.find_elements_until_visibility(self.locator("room_name"))
        self.driver.click(room_btn[1])

    @allure.step("获取房间名称")
    def get_room_name(self, num = 0):
        """
        从房间列表中获取房间名称
        :param num: 默认为第一个
        :return: 房间名称
        """
        room = self.driver.find_elements_until_visibility(self.locator("room_name"))
        name = room[mun].text
        return name

    @allure.step("获取房间个数")
    def get_room_num(self):
        """
        从房间列表获取房间个数
        :return: 房间个数
        """
        rooms = self.driver.find_elements_until_visibility(self.locator("room_name"))
        num = len(rooms)
        return num


