#@project:  ayla_ui_project
#@author: heyeping
#@file: ap_andriod_con1.py
#@ide: PyCharm
#@time: 2021/3/11 4:09 PM

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
    'platformVersion': '9',
    'appPackage': 'com.sunseaaiot.app.lark',
    # 'appActivity': 'com.sunseaiot.larkapp.SplashActivity',
    'appActivity': 'com.sunseaiot.larkapp.refactor.login.SplashActivity',
    'noReset': True,  # 设置不重装app
    'deviceName': 'samsung',
    # 'unicodeKeyboard': True,
    'resetKeyboard': True,  # 运行完成后重置软键盘的状态　　
    # 'automationName': 'uiautomator2',  # 用于toast的获取
}


def send_command(ser):
    factory = "ayla reset factory\n\r"
    ser.write(factory.encode())
    time.sleep(2)


def find_element_until_visibility(driver, locator, timeout=10):
    ele = WebDriverWait(driver, timeout).until(EC.visibility_of_any_elements_located((By.ID, locator)))
    return ele


def find_element_until_visibility_xpath(driver, locator, timeout=10):
    ele = WebDriverWait(driver, timeout).until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
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
    ser = serial.Serial('/dev/cu.wchusbserial1433330', 115200, timeout=3)  # 串口工具初始化,串口的端口需要根据实际情况更改
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    ayla_name = "Ayla-ac5d5cba7d15"  # 设备的WiFi信号
    # device_dsn = "SC000W000169643"                                               # 设备DSN
    # wifi = "sunseagroup"                                                         # 指定要连接的WiFi
    wifi = "test2.4g"
    wifi_pwd = "sunsea888"  # WiFi密码
    #
    # wifi = "test6"
    # wifi_pwd = "test12345"

    result_file = os.path.join(base_path, "Wifi_join.txt")  # 存储配网情况的文件
    success_time = 0  # 统计成功的次数
    fail_time = 0  # 统计失败的次数
    cycle_time = 300  # 循环次数
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
    for i in range(cycle_time):
        # 设备配网
        k = done_time + i + 1
        # conn_time = datetime.datetime.now()
        # print("第%s次配网开始时间:%s" % (i+1, conn_time))
        # send_command(ser)
        time.sleep(4)

        driver.wait_activity(".MainActivity", 3)
        time.sleep(2)
        add_btn = driver.find_element_by_id("com.sunseaaiot.app.lark:id/add_device").click()  # 添加设备按钮
        time.sleep(2)

        send_command(ser)  # 通过串口下发指令

        time.sleep(2)
        btn_bottom = driver.find_element_by_xpath("//android.widget.TextView[@text='插座']")  # 点击"插座"按钮
        btn_bottom.click()
        time.sleep(2)
        switch_Ap = driver.find_element_by_xpath("//android.widget.TextView[@text='慢闪模式']").click()
        time.sleep(2)
        confirm_Ap = driver.find_element_by_id("com.sunseaaiot.app.lark:id/ck_how_to_config").click()  # 慢闪指示灯
        time.sleep(2)
        btn_next = driver.find_element_by_id("com.sunseaaiot.app.lark:id/btn_bottom")  # 慢闪界面的下一步
        # btn_next = driver.find_element_by_xpath("//android.widget.Button[@text='下一步']")
        btn_next.click()
        time.sleep(2)
        wifi_filed = find_element_until_visibility(driver, "com.sunseaaiot.app.lark:id/tv_wifi_ssid")  # 获取当前连接的WiFi
        wifi_name = wifi_filed[0].text
        # 异常处理,连接的WiFi不是指定的WiFi需切换
        if wifi_name != wifi:
            change_btn = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_change_network")  # 切换网络按钮
            change_btn.click()
            time.sleep(5)
            ss_wifi = driver.find_element_by_xpath(
                "//android.widget.TextView[@text='{wifi}']".format(wifi=wifi))  # 选择指定的WiFi
            ss_wifi.click()
            time.sleep(5)
            # time.sleep(3)
            # ayla_wifi = driver.find_element_by_xpath("//android.widget.TextView[@text='{wifi}']".format(wifi=ayla_name))
            # time.sleep(4)
            # ayla_wifi.click()

            driver.keyevent(4)
        time.sleep(2)
        # driver.keyevent(4)
        driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_next").click()  # 选择wifi界面的点击下一步按钮

        set_ayla = driver.find_element_by_id("com.sunseaaiot.app.lark:id/tv_goto_setup")  # 前往wi-fi设置
        set_ayla.click()
        time.sleep(10)
        ayla_wifi = find_element_until_visibility_xpath(driver, "//android.widget.TextView[@text='{wifi}']".format(
            wifi=ayla_name),30)
        ayla_wifi = driver.find_element_by_xpath("//android.widget.TextView[@text='{wifi}']".format(wifi=ayla_name))
        # ayla_wifi = driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='{wifi}']".format(wifi=ayla_name))    #小米8
        # time.sleep(3)
        ayla_wifi.click()
        # driver.find_element_by_xpath("//android.wifidget.Button[@text='连接']").click()                 # 华为手机选择WiFi后需要点击连接按钮

        # driver.find_element_by_xpath("//android.widget.Button[@text='连接']").click()
        time.sleep(10)
        driver.keyevent(4)

        conn_time = datetime.datetime.now()
        print("第%s次配网开始时间:%s" % (i + 1, conn_time))

        d1 = datetime.datetime.now()  # 开始时间
        time.sleep(3)
        finish_btn = find_element_until_visibility(driver, "com.sunseaaiot.app.lark:id/btn_bottom",
                                                   240)  # 配网完成会出现一个button
        d2 = datetime.datetime.now()  # 结束时间
        text = finish_btn[0].text  # 获取配网结束后的button上的文本
        # 根据button上的文本判断配网是否成功
        if text == "完成":
            result = "Success"
            success_time = success_time + 1
        else:
            result = "Failed"
            fail_time = fail_time + 1
        cost_time = (d2 - d1).seconds
        time.sleep(3)
        # 统计配网情况
        with open(result_file, 'a+') as f:
            f.write("时间{conn_time}!第{i}次配网情况:{result},耗时:{cost_time}s\n".format(conn_time=conn_time, i=k, result=result,
                                                                                cost_time=cost_time))
        # 异常处理,不管设备配网成功与否,点击4次返回按键回主菜单,并重启App
        for i in range(5):
            driver.keyevent(4)
            time.sleep(1)
        time.sleep(3)
        # # 重启App
        # plug_app = driver.find_element_by_xpath("//android.widget.TextView[@text='日海艾拉']")                  # APP名称
        # plug_app.click()

    with open(result_file, 'a+') as f:
        f.write("总体配网情况:成功{success_time}次,失败{fail_time}次\n".format(success_time=success_time, fail_time=fail_time))
