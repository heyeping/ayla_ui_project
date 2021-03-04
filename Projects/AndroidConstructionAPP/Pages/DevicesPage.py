from BaseDriver.Driver import AutoDriver
from Helper.ElementLoader import ElementLoader
import unittest, time
from Projects.AndroidConstructionAPP.Pages.ProjectPage import ProjectPage
from Projects.AndroidConstructionAPP.Pages.RoomPage import RoomPage

class DevicesPage(ElementLoader, unittest.TestCase):
    driver = AutoDriver()
    ElementLoader = ElementLoader()
    ProjectPage = ProjectPage()
    RoomPage = RoomPage()
    device_names = self.driver.find_elements_until_visibility(ElementLoader.locator("device_name"))

    #def __init__(self):
        #ElementLoader.__init__(self, self.__class__.__name__)

    def into_devicePage(self):
        """
        进入设备列表页面
        :return:
        """
        #进入房间列表页面
        self.ProjectPage.intoProjectInfo()
        #进入设备列表页面
        self.RoomPage.into_rommPage()

    def get_device_name(self, num=0):
        """
        获取设备名称
        :param num:默认获取第一个设备
        :return:
        """
        device_name = self.device_names[num].text
        return device_name


