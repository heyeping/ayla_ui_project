#@project:  testgrouppub
#@author: heyeping
#@file: ap_android_ayla_ng.py
#@ide: PyCharm
#@time: 2021/6/24 11:16 AM

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import os,time,datetime
import serial
from loguru import logger
import random

#小米8
desired_caps = {
    'platformName': 'Android',
    'appPackage': 'com.ayla.ng.app',
    'appActivity': 'com.ayla.ng.app.view.activity.WelcomeActivity',
    'noReset': True,  # 设置不重装app
    'deviceName': 'xiaoxiao8',
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
    ele = WebDriverWait(driver, timeout,poll_frequency=0.1).until(EC.visibility_of_element_located((by, locator)))
    return ele


# 判断元素是否存在
def is_element(driver, by=By.ID, locator="", timeout=50):
    Flag = None
    try:
        ele = WebDriverWait(driver, timeout, poll_frequency=1).until(EC.visibility_of_element_located((by, locator)))
        logger.info("定位到{locator}元素存在".format(locator=locator))
        Flag = True
        return Flag
    except TimeoutException:
        Flag = False
        return Flag

if __name__ == '__main__':
    base_path = os.path.dirname(__file__)  # 获取当前脚本的绝对路径
    file_name = "Wifi_join_" + str(time.strftime('%Y%m%d_%H:%M', time.localtime())) + ".txt"
    #存储配网log
    result_file = os.path.join(base_path, file_name)
    #print(result_file)
    # 串口工具初始化,串口的端口需要根据实际情况更改
    #ser = serial.Serial('/dev/cu.usbserial-AR0KJ21N', 115200, timeout=3)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    #设备AP
    ayla_name = "Ayla-a4cd23017a21"
    wifi = '何三胖的wifi'
    wifi_pwd = 'x1234567'
    #循环次数
    cycle_time = 1
    #已执行次数
    done_time = 0
    #统计成功次数
    success_time = 0
    #统计失败次数
    fail_time = 0

    for i in range(cycle_time):
        k = done_time + i + 1
        #添加设备元素定位
        add_device_btn = driver.find_element_by_id("com.ayla.ng.app:id/ivAdd")
        add_device_btn.click()
        #send_command(ser)  # 通过串口下发指令
        #球泡灯元素
        device_ele = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/tv_name")
        device_ele.click()
        time.sleep(3)
        #切换配网方式元素
        change_btn = find_element_until_visibility(driver, by=By.XPATH, locator="//android.view.View[@text='蓝牙配网']")
        change_btn.click()
        #切换到AP配网
        time.sleep(1)
        AP_btn = find_element_until_visibility(driver, by=By.XPATH, locator="//android.view.View[@text='AP 配网']")
        AP_btn.click()
        #灯光已闪烁选择框
        check_btn = find_element_until_visibility(driver, by=By.XPATH, locator="//android.widget.CheckBox[@text='灯光已闪烁']")
        check_btn.click()
        #下一步按钮
        next_btn= find_element_until_visibility(driver, by=By.XPATH, locator="//android.widget.Button[@text='下一步']")
        next_btn.click()
        # 获取当前wifi名称
        wifi_name_ele = driver.find_element_by_id("com.ayla.ng.app:id/tv_ssid")
        wifi_name = wifi_name_ele.text
        # 确保当前手机wifi是要配网的wifi
        if wifi_name != wifi:
            wifi_name_ele.send_keys(wifi)
        # 填写wifi密码
        wifi_pwd_text = driver.find_element_by_id("com.ayla.ng.app:id/tv_pwd")
        wifi_pwd_text.send_keys(wifi_pwd)
        # 点击下一步
        driver.find_element_by_id("com.ayla.ng.app:id/next").click()
        #前往Wi-Fi设置
        bt_next = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/bt_next")
        bt_next.click()
        time.sleep(3)
        # 选择对应的设备AP
        device_ap = driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='{wifi}']".format(wifi=ayla_name))
        device_ap.click()
        time.sleep(3)
        # 点击返回
        driver.keyevent(4)
        # 开始配网时间
        conn_time = datetime.datetime.now()
        logger.info("第%s次配网开始时间：%s" % (i + 1, conn_time))
        d1 = datetime.datetime.now()
        succ_flag = is_element(driver, by=By.XPATH, locator="//android.widget.TextView[@text='设备名称']", timeout=60)
        logger.info("succ_flag={succ_flag}".format(succ_flag=succ_flag))
        d2_fail = datetime.datetime.now()
        if succ_flag:
            result = "Success"
            success_time = success_time + 1
            succ_flag = find_element_until_visibility(driver, by=By.XPATH,
                                                      locator="//android.widget.TextView[@text='设备名称']", timeout=20)
            d3_succ = datetime.datetime.now()
            cost_time = (d3_succ - d1).seconds
            # 返回首页：弹框确定元素：	com.ayla.ng.app:id/tv_right
            # driver.keyevent(4)
            # v_done = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/tv_right")
            # v_done.click()
            # driver.keyevent(4)
            #第二种方法：填写名称，点击确定，在弹框中点击完成，就回到首页
            device_name_ele = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/custom_container")
            device_name_ele.click()
            #输入设备名称
            device_name = "AP" +str(random.randint(0, 99)) + "配网成功" + str(random.randint(0, 99))
            device_name_text = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/appCompatEditText")
            device_name_text.send_keys(device_name)
            v_done = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/tv_right")
            v_done.click()
            #点击保存按钮
            save_btn = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/next")
            save_btn.click()
            ok_btn = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/tv_right")
            ok_btn.click()
        else:
            result = "Failed"
            fail_time = fail_time + 1
            cost_time = (d2_fail - d1).seconds
            # 返回到首页
            for i in range(3):
                driver.keyevent(4)
                time.sleep(1)

        # 统计配网情况
        with open(result_file, 'a+') as f:
            f.write(
                "第{i}次配网===配网开始时间：{conn_time}！配网情况：{result},    配网花费时间{cost_time}\n".format(i=k, conn_time=conn_time,
                                                                                            result=result,
                                                                                            cost_time=cost_time))

        # 统计配网成功和失败次数
    with open(result_file, 'a+') as f:
        f.write("\n总配网次数：{i},  成功次数：{success_time}，失败次数：{fail_time}\n".format(i=k, success_time=success_time,
                                                                              fail_time=fail_time))





















