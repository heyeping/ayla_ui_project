#@project:  ayla_ui_project
#@author: heyeping
#@file: ap_android.py
#@ide: PyCharm
#@time: 2021/3/10 4:42 PM

import serial
import time
# from appium import webdriver
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
    time.sleep(2)


def find_element_until_visibility(driver, by=By.ID, locator="", timeout=10):
    ele = WebDriverWait(driver, timeout,poll_frequency=0.1).until(EC.visibility_of_any_elements_located((by, locator)))
    return ele


# 判断元素是否存在
def isElement(driver, ele, timeout=5):
    Flag = None
    try:
        driver.find_element_by_id(ele)
        Flag = True
    except NoSuchElementException:
        Flag = False
    finally:
        return Flag


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)  # 获取当前脚本的绝对路径
    file_name = "Wifi_join_" + str(time.strftime('%Y%m%d_%H:%M', time.localtime())) + ".txt"
    result_file = os.path.join(base_path, file_name)  # 存储配网情况的文件
    ser = serial.Serial('/dev/cu.usbserial-AB0JJH2D', 115200, timeout=3)  # 串口工具初始化,串口的端口需要根据实际情况更改
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    ayla_name = "Ayla-286dcd2becc9"  # 设备的WiFi信号
    # device_dsn = "SC000W000169643"                                               # 设备DSN
    # wifi = "sunseagroup"                                                         # 指定要连接的WiFi
    wifi = "TP-LINK_5660"
    wifi_pwd = "aylatest"  # WiFi密码
    # result_file = os.path.join(base_path, "Wifi_join.txt")  # 存储配网情况的文件
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
        # 设备配网
        k = done_time + i + 1
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/add_device").click()  # 添加设备按钮
        send_command(ser)  # 通过串口下发指令
        send_time = datetime.datetime.now()
        time.sleep(3)
        log_command(ser)
        # driver.tap([(370, 288), (490, 408)])  # 华为
        # os.system("adb shell input tap 430 350")  # 华为
        os.system("adb shell input tap 266 230")  # OPPO
        time.sleep(1)
        switch_Ap = driver.find_element_by_xpath("//android.widget.TextView[@text='慢闪模式']").click()
        time.sleep(1)
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/ck_how_to_config").click()  # 慢闪指示灯
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/btn_bottom").click()  # 慢闪界面的下一步
        time.sleep(2)
        # wifi_filed = find_element_until_visibility(driver, "com.sunseaaiot.app.lark:id/tv_wifi_ssid")  # 获取当前连接的WiFi
        # wifi_name = wifi_filed[0].text
        wifi_name = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_wifi_ssid").text
        # 异常处理,连接的WiFi不是指定的WiFi需切换
        if wifi_name != wifi:
            change_btn = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_change_network")  # 切换网络按钮
            change_btn.click()
            time.sleep(5)
            # ss_wifi = driver.find_element_by_xpath("//android.widget.TextView[@text='{wifi}']".format(wifi=wifi))  # 选择指定的WiFi
            # ss_wifi.click()
            ss_wifi = find_element_until_visibility(driver, By.XPATH,
                                                    "//android.widget.TextView[@text='{wifi}']".format(wifi=wifi), 90)
            ss_wifi[0].click()
            time.sleep(5)
            driver.keyevent(4)
            time.sleep(2)
        # driver.keyevent(4)
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_next").click()  # 选择wifi界面的点击下一步按钮
        set_ayla = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_goto_setup")  # 前往wi-fi设置
        set_ayla.click()
        # time.sleep(10)
        ayla_wifi = find_element_until_visibility(driver, By.XPATH, "//android.widget.TextView[@text='{wifi}']".format(
            wifi=ayla_name), 90)
        ayla_wifi[0].click()
        time.sleep(3)
        # driver.find_element_by_xpath("//android.widget.Button[@text='连接']").click()                 # 华为手机选择WiFi后需要点击连接按钮
        # time.sleep(5)
        # driver.keyevent(4)
        os.system("adb shell input keyevent 4")
        conn_time = datetime.datetime.now()
        print("第{i}次配网!配网开始时间:{conn_time}    设备reset factory:{send_time}".format(i=k, conn_time=conn_time,
                                                                                 send_time=send_time))
        finish_btn = find_element_until_visibility(driver, by=By.ID, locator="com.sunseaaiot.app.lark:id/btn_bottom",
                                                   timeout=500)
        with open(result_file, 'a+') as h:
            h.write("第{i}次配网!配网开始时间:{conn_time}    设备reset factory:{send_time}\n".format(i=k, conn_time=conn_time,
                                                                                         send_time=send_time))
        time.sleep(3)
        for i in range(5):
            driver.keyevent(4)
            time.sleep(1)
