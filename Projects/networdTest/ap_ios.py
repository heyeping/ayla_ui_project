#@project:  ayla_ui_project
#@author: heyeping
#@file: ap_ios.py
#@ide: PyCharm
#@time: 2021/3/10 4:45 PM

import serial
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import os

# IOS10
desired_caps = {
    "udid": "18bb82ecefc06c6da48553bec851203161fadf44",
    "xcodeOrgId": "692AM2VNT3",
    "xcodeSigningId": "iPhone Developer",
    "platformName": "ios",
    "deviceName": "Test",
    "app": "/Users/parson/Documents/03_SunseaAyla/Lark_apk/2019/iOS_LarkAPP.ipa",
    "noReset": True,
    "automationName": "XCUITest",
    "platformVersion": "10.0.1"
}


def send_command(ser):
    # W600 Realtek
    factory = "reset factory\n\r"
    # BK
    # factory = "ayla reset factory\n\r"
    ser.write(factory.encode())
    time.sleep(2)


def log_command(ser):
    # W600 Realtek
    factory = "log all\n\r"
    # BK
    # factory = "ayla reset factory\n\r"
    ser.write(factory.encode())


def find_element_until_visibility(driver, by=By.ID, locator="", timeout=10):
    ele = WebDriverWait(driver, timeout).until(EC.visibility_of_any_elements_located((by, locator)))
    return ele


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)  # 获取当前脚本的绝对路径
    file_name = "Wifi_join_" + str(time.strftime('%Y%m%d_%H:%M', time.localtime())) + ".txt"
    result_file = os.path.join(base_path, file_name)  # 存储配网情况的文件
    ayla_name = "Ayla-286dcd2becc9"     # 设备的Wifi信号
    wifi = "tester"  # 需连接的WiFi
    wifi_pwd = "sunsea888"  # WiFi密码
    cycle_time = 400  # 循环次数
    done_time = 0
    ser = serial.Serial('/dev/cu.usbserial-AB0JJH2D', 115200, timeout=3)  # 串口工具初始化,串口的端口需要根据实际情况更改
    driver: webdriver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    for i in range(cycle_time):
        k = done_time + i + 1
        send_command(ser)
        send_time = datetime.datetime.now()
        time.sleep(5)
        log_command(ser)
        time.sleep(10)
        driver.find_element_by_accessibility_id("add device").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("插座").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("Change_Mode").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("Confirm_Mode").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("Config_finish").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("下一步").click()
        time.sleep(1)
        driver.find_element_by_accessibility_id("Config_finish").click()
        # time.sleep(5)
        ayla_btn = find_element_until_visibility(driver, by=MobileBy.ACCESSIBILITY_ID, locator=ayla_name, timeout=120)  # 选Ayla WiFi
        ayla_btn[0].click()
        time.sleep(10)
        driver.find_element_by_accessibility_id("返回“日海艾拉”").click()
        conn_time = datetime.datetime.now()
        print("第{i}次配网!配网开始时间:{conn_time}    设备reset factory:{send_time}".format(i=k, conn_time=conn_time,
                                                                                 send_time=send_time))
        finish_btn = find_element_until_visibility(driver, by=MobileBy.ACCESSIBILITY_ID, locator="Config_finish", timeout=240)
        with open(result_file, 'a+') as h:
            h.write("第{i}次配网!配网开始时间:{conn_time}    设备reset factory:{send_time}\n".format(i=k, conn_time=conn_time,
                                                                                         send_time=send_time))
        time.sleep(3)
        for i in range(5):
            driver.find_element_by_accessibility_id("navBack").click()
        time.sleep(5)
