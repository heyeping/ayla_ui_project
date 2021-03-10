#@project:  ayla_ui_project
#@author: heyeping
#@file: airkiss_android.py
#@ide: PyCharm
#@time: 2021/3/10 4:44 PM

import serial
import time
# from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import datetime
import os
from appium import webdriver

# samsung
desired_caps = {
    'platformName': 'Android',
    'appPackage': 'com.sunseaaiot.app.lark',
    'appActivity': 'com.sunseaiot.larkapp.refactor.login.SplashActivity',
    'noReset': True,  # 设置不重装app
    'deviceName': 'samsung',
    # 'unicodeKeyboard': True,
    'resetKeyboard': True,  # 运行完成后重置软键盘的状态　　
    # 'automationName': 'uiautomator2',  # 用于toast的获取
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
    # time.sleep(2)


def find_element_until_visibility(driver, by=By.ID, locator="", timeout=10):
    ele = WebDriverWait(driver, timeout,poll_frequency=0.1).until(EC.visibility_of_element_located((by, locator)))
    # ele = WebDriverWait(driver, timeout,poll_frequency=0.1).until(EC.visibility_of_any_elements_located((by, locator)))
    return ele


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)  # 获取当前脚本的绝对路径
    file_name = "Wifi_join_" + str(time.strftime('%Y%m%d_%H:%M', time.localtime())) + ".txt"
    result_file = os.path.join(base_path, file_name)  # 存储配网情况的文件
    ser = serial.Serial('/dev/cu.usbserial-AB0JJZF8', 115200, timeout=3)  # 串口工具初始化,串口的端口需要根据实际情况更改
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    wifi = "TP-LINK_5660"
    wifi_pwd = "sunsea888"  # WiFi密码
    success_time = 0  # 统计成功的次数
    fail_time = 0  # 统计失败的次数
    cycle_time = 400  # 循环次数
    done_time = 0  # 已执行次数,默认是0,具体根据实际情况来
    # 登录App,可以跳过次步骤
    # username = "2212249179@qq.com"
    # password = "123456"
    # driver.find_element_by_id('userNameEditText').clear()
    # user=driver.find_element_by_id('userNameEditText')       # 用户名
    # driver.set_value(user,username)
    # passwd=driver.find_element_by_id('passwordEditText').clear()
    # driver.set_value(passwd,password)
    # driver.find_element_by_id('passwordEditText').send_keys(password)          # 密码
    # driver.keyevent(4)                                                       # 收回键盘
    # driver.find_element_by_id('buttonSignIn').click()
    time.sleep(10)
    for i in range(cycle_time):
        k = done_time + i + 1
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/add_device").click()  # 添加设备按钮
        send_command(ser)  # 通过串口下发指令
        send_time = datetime.datetime.now()
        time.sleep(5)
        # os.system("adb shell input tap 266 230") # 三星
        os.system("adb shell input tap 430 350") # 华为
        # button=driver.find_elements_by_xpath("//*[contains(@text,'插座')]")
        # button[0].click()
        time.sleep(1)
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/ck_how_to_config").click()
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/btn_bottom").click()
        time.sleep(2)
        wifi_name = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_wifi_ssid").text
        if wifi_name != wifi:
            change_btn = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_change_network")  # 切换网络按钮
            change_btn.click()
            time.sleep(5)
            ss_wifi = driver.find_element_by_xpath(
                "//android.widget.TextView[@text='{wifi}']".format(wifi=wifi))  # 选择指定的WiFi
            ss_wifi.click()
            time.sleep(5)
            driver.keyevent(4)
            time.sleep(2)
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_next").click()
        conn_time = datetime.datetime.now()
        print("第{i}次配网!配网开始时间:{conn_time}    设备reset factory:{send_time}".format(i=k, conn_time=conn_time,
                                                                                 send_time=send_time))
        finish_btn = find_element_until_visibility(driver, by=By.ID, locator="btn_bottom", timeout=500)
        with open(result_file, 'a+') as h:
            h.write("第{i}次配网!配网开始时间:{conn_time}    设备reset factory:{send_time}\n".format(i=k, conn_time=conn_time,
                                                                                         send_time=send_time))
        for i in range(4):
            driver.keyevent(4)
            time.sleep(1)
