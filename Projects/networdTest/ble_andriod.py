#@project:  ayla_ui_project
#@author: heyeping
#@file: ble_andriod.py
#@ide: PyCharm
#@time: 2021/6/17 3:03 PM

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import os,time,datetime
import serial
from loguru import logger

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
    # finally:
    #     return Flag

# # 判断元素是否存在
# def isElement(driver, ele, timeout=5):
#     Flag = None
#     try:
#         driver.find_element_by_id(ele)
#         Flag = True
#     except NoSuchElementException:
#         Flag = False
#     finally:
#         return Flag


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)  # 获取当前脚本的绝对路径
    file_name = "Wifi_join_" + str(time.strftime('%Y%m%d_%H:%M', time.localtime())) + ".txt"
    #存储配网log
    result_file = os.path.join(base_path, file_name)
    #print(result_file)
    # 串口工具初始化,串口的端口需要根据实际情况更改
    ser = serial.Serial('/dev/cu.usbserial-AR0KJ21N', 115200, timeout=3)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    wifi = 'TP-LINK_70B2'
    wifi_pwd = 'aylatest888'
    #循环次数
    cycle_time = 3
    #已执行次数
    done_time = 0
    #统计成功次数
    success_time = 0
    #统计失败次数
    fail_time = 0

    for i in range(cycle_time):
        k = done_time + i + 1
        #添加设备元素定位
        add_device_btn = driver.find_element_by_id("com.ayla.ng.app:id/add_device")
        add_device_btn.click()
        send_command(ser)  # 通过串口下发指令
        #自动搜索元素定位
        driver.find_element_by_xpath("//android.widget.TextView[@text='自动发现']").click()
        #定位搜索到到设备
        time.sleep(8)
        device = driver.find_element_by_id("com.ayla.ng.app:id/textView")
        time.sleep(1)
        device.click()
        #获取当前wifi名称
        wifi_name = driver.find_element_by_id("com.ayla.ng.app:id/tv_ssid").text
        #确保当前手机wifi是要配网的wifi
        if wifi_name != wifi:
            #切换Wi-Fi
            change_wifi_btn = driver.find_element_by_id("com.ayla.ng.app:id/iv_switch")
            change_wifi_btn.click()
            # 选择指定的WiFi
            ss_wifi = driver.find_element_by_xpath("//android.widget.TextView[@text='{wifi}']".format(wifi=wifi))
            ss_wifi.click()
            driver.keyevent(4)
        #填写wifi密码
        wifi_pwd_text = driver.find_element_by_id("com.ayla.ng.app:id/tv_pwd")
        wifi_pwd_text.send_keys(wifi_pwd)
        #点击下一步
        driver.find_element_by_id("com.ayla.ng.app:id/next").click()
        #开始配网时间
        conn_time = datetime.datetime.now()
        logger.info("第%s次配网开始时间：%s" % (i+1, conn_time))
        d1 = datetime.datetime.now()
        #判断跳转到配网成功页则配网成功；否则配网失败
        #或者判断有重试按钮为配网失败
        #com.ayla.ng.app:id/retry --重试按钮
        #配网成功页"//android.widget.TextView[@text='设备名称']"
        #succ_flag = find_element_until_visibility(driver, by=By.XPATH, locator="//android.widget.TextView[@text='设备名称']", timeout=500)
        #失败之后操作三次返回回到首页
        #成功之后操作返回还是继续正常流程？，操作返回，在弹框出现点击确定，再次操作返回就回到首页
        succ_flag = is_element(driver, by=By.XPATH, locator="//android.widget.TextView[@text='设备名称']", timeout=60)
        #fail_flag = isElement(driver, "retry", 20)
        #time.sleep(10)
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
            driver.keyevent(4)
            v_done = find_element_until_visibility(driver, by=By.ID, locator="com.ayla.ng.app:id/tv_right")
            v_done.click()
            driver.keyevent(4)

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
            f.write("第{i}次配网===配网开始时间：{conn_time}！配网情况：{result},    配网花费时间{cost_time}\n".format(i=k, conn_time=conn_time, result=result, cost_time=cost_time))

    #统计配网成功和失败次数
    with open(result_file, 'a+') as f:
        f.write("\n总配网次数：{i},  成功次数：{success_time}，失败次数：{fail_time}\n".format(i=k, success_time=success_time, fail_time=fail_time))






