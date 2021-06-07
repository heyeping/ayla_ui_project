from appium import webdriver as adriver
from selenium import webdriver as sdriver
from selenium.webdriver.support.ui import Select as sselect
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import time
import datetime
import os
import yaml
import subprocess
import requests
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
import math
import operator
from functools import reduce
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image, ImageFile
import imagehash
import allure


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class AutoDriver(Singleton):
    driver = None
    currentFileDir = os.path.dirname(__file__)
    eutDir = os.path.abspath(currentFileDir + os.path.sep + "..")
    p = os.path.join(os.path.abspath(currentFileDir + os.path.sep + ".."), "Conf", "running.yaml")
    with open(p, 'r') as f:
        data = yaml.load(f)
    timeOut = data["timeOut"]
    logLevel = data["logLevel"]
    projectName = data['project']
    projectDir = os.path.join(eutDir, "Projects", "%s" % projectName)
    unicodeKeyboard = data["unicodeKeyBoard"]
    soundResourceDir = os.path.join(eutDir, "Projects", projectName, "SoundResource")
    c = os.path.join(projectDir, "%s.yaml" % projectName)
    with open(c, 'r', encoding="utf-8") as f:
        dataProject = yaml.load(f)
    projectType = dataProject["projectType"]
    desired_caps = {}
    if projectType == 'APP':
        # Parson
        # 应用脚本启动appium
        # os.system("nohup appium --session-override &")
        # time.sleep(30)
        platformName = dataProject["platformName"]
        # Parson
        # 新增noReset参数，设置App不用重新安装
        noReset = dataProject["noReset"]
        if platformName == "Android":
            # Parson
            # 获取toast时需要用到
            desired_caps["automationName"] = "uiautomator2"
            desired_caps["appPackage"] = dataProject["appPackage"]
            desired_caps["appActivity"] = dataProject["appActivity"]
            # Parson
            # 新增以下判断，如果设置App不重装，安卓不用写apk路径
            if noReset:
                # desired_caps["app"] = dataProject["app"]
                desired_caps["noReset"] = dataProject["noReset"]
            else:
                desired_caps["app"] = dataProject["app"]
        else:
            desired_caps["xcodeOrgId"] = dataProject["xcodeOrgId"]
            desired_caps["xcodeSigningId"] = dataProject["iPhoneDeveloper"]
            desired_caps["automationName"] = "XCUITest"
            # Parson
            # 新增以下2行代码
            desired_caps["app"] = dataProject["app"]
            desired_caps["noReset"] = dataProject["noReset"]
            desired_caps["udid"] = dataProject["udid"]
        fullReset = dataProject["fullReset"]
        desired_caps["platformName"] = platformName
        desired_caps["platformVersion"] = dataProject["platformVersion"]
        desired_caps["deviceName"] = dataProject["deviceName"]
        # desired_caps["udid"] = dataProject["udid"]
        # Parson
        # 已将desired_caps里的app参数上移，主要是设置是否重装App时参数IOS和Android不一样
        # desired_caps["app"] = dataProject["app"]
        # 以下暂时注释掉2019-04-09
        # desired_caps['newCommandTimeout'] = 9000
        # desired_caps["recreateChromeDriverSessions"] = True
        # desired_caps["fullReset"] = fullReset
        # desired_caps["unicodeKeyboard"] = unicodeKeyboard
        desired_caps["resetKeyboard"] = True
        desired_caps["androidInstallTimeout"] = 90000 * 2
        # print(desired_caps)
        subprocess.Popen("appium --log-level %s --log-timestamp --local-timezone" % logLevel, shell=True)
        while 1:
            time.sleep(1)
            try:
                response = requests.get('http://127.0.0.1:4723/wd/hub/status').status_code
                if response == 200:
                    break
            except Exception:
                pass
        driver = adriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    elif projectType == "Web":
        browser = dataProject["Browser"]
        startPage = dataProject["startPage"]
        if not driver:
            driver = eval("sdriver.%s()" % browser)
            driver.get("%s" % startPage)
    else:
        print("projectType must be APP or Web ")
        raise BaseException("projectType must be APP or Web")

    @classmethod
    def instant_find_element(self, locator):
        # 单次查找一个元素
        return self.driver.find_element(locator[0], locator[1])

    @classmethod
    def instant_find_elements(self, locator):
        # 单次查找多个元素
        return self.driver.find_elements(locator[0], locator[1])

    @classmethod
    def get_all_contexts(self):
        # 获取所有上下文
        ctx = self.driver.contexts
        print(ctx)
        return ctx

    @classmethod
    def get_current_context(self):
        # 获取所有上下文
        return self.driver.context

    @classmethod
    def find_element_until_displayed(self, locator):
        # 超时时间内循环查找元素，直至找到并且在页面上展示出来为止 - 有时候driver已经找到元素，但是页面还没渲染完全，导致下一步点击会失败
        # 下面一行是调试用代码
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.now()
        passed_time = (d2 - d1).seconds
        while passed_time < self.timeOut:
            try:
                ele = self.driver.find_element(locator[0], locator[1])
                if ele.is_displayed():
                    return ele
                else:
                    continue
            except NoSuchElementException:
                try:
                    # 如果遇到网络不好的情况，开发应在此定义一个页面加载超时出现的元素，点击后触发重新加载
                    time_out_element = self.driver.find_element_by_id("com.hongfans.rearview:id/iv_error_load")
                    time_out_element.click()
                    continue
                except NoSuchElementException:
                    print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
                os.system("echo Retrying to find element...")
                time.sleep(0.5)
                d2 = datetime.datetime.now()
                passed_time = (d2 - d1).seconds
        print("Can not find element specified -> ", locator)
        raise NoSuchElementException

    @classmethod
    def find_element(self, locator):
        # 超时时间内循环查找元素，直至找到为止
        # 下面一行是调试用代码
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.now()
        passed_time = (d2 - d1).seconds
        while passed_time < self.timeOut:
            try:
                ele = self.driver.find_element(locator[0], locator[1])
                return ele
            except NoSuchElementException:
                try:
                    # 如果遇到网络不好的情况，开发应在此定义一个页面加载超时出现的元素，点击后触发重新加载
                    time_out_element = self.driver.find_element_by_id("com.hongfans.rearview:id/iv_error_load")
                    time_out_element.click()
                    continue
                except NoSuchElementException:
                    print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
                os.system("echo Retrying to find element...")
                time.sleep(0.5)
                d2 = datetime.datetime.now()
                passed_time = (d2 - d1).seconds
        print("Can not find element specified -> ", locator)
        raise NoSuchElementException

    @classmethod
    def find_elements(self, locator, allow_none_list=False):
        # 超时时间内循环查找元素集，直至找到为止
        # allow_none_list: 是否允许返回空的结果集
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.now()
        passed_time = (d2 - d1).seconds
        while passed_time < self.timeOut:
            try:
                elements = self.driver.find_elements(locator[0], locator[1])
                if allow_none_list:
                    return elements
                else:
                    if not elements:
                        try:
                            # 如果遇到网络不好的情况，开发应在此定义一个页面加载超时出现的元素，点击后触发重新加载
                            time_out_element = self.driver.find_element_by_id("com.hongfans.rearview:id/iv_error_load")
                            time_out_element.click()
                        except NoSuchElementException:
                            d2 = datetime.datetime.now()
                            passed_time = (d2 - d1).seconds
                            continue
                    else:
                        return elements
            except NoSuchElementException:
                print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
                time.sleep(0.5)
                d2 = datetime.datetime.now()
                passed_time = (d2 - d1).seconds
        print("Can not find elements specified ->", locator)
        raise NoSuchElementException

    @classmethod
    def set_input_method(self, keyboard_name):
        # 安卓可用，设置输入法
        dic = {"fly": "com.iflytek.inputmethod.pad/.FlyIME", "appium": "io.appium.android.ime/.UnicodeIME",
               "adb": "com.android.adbkeyboard/.AdbIME"}
        os.system("adb shell ime set %s" % dic[keyboard_name])

    @classmethod
    def clear(self, element):
        # 清除输入框内容
        return element.clear()

    @classmethod
    def click(self, element):
        # 点击
        return element.click()

    @classmethod
    def send_keys(self, element, content):
        # 输入，不替换原有内容
        return element.send_keys(content)

    @classmethod
    def set_value(self, element, content):
        # 输入，将会替换掉原有内容
        return self.driver.set_value(element, content)

    @classmethod
    def assert_true(self, p, error_info):
        # 断言真: 表达式p若为假, 则抛错, 并显示error_info
        try:
            assert p, error_info
        except AssertionError:
            raise

    @classmethod
    def page_should_contains_text(self, expected_text):
        # 5秒内，检查页面是否出现指定文本
        d1 = datetime.datetime.now()
        d2 = datetime.datetime.now()
        passed_time = (d2 - d1).seconds
        while passed_time < 5:
            try:
                page_source = self.driver.page_source
                self.assert_true(expected_text in page_source, "%s is NOT in current Page, retrying" % expected_text)
                return
            except AssertionError:
                time.sleep(0.5)
                d2 = datetime.datetime.now()
                passed_time = (d2 - d1).seconds
                continue
        raise Exception("5秒内校验页面包含文本 %s 失败。" % expected_text)

    @classmethod
    def switch_to_context(self, context_name):
        # 切换上下文
        return self.driver.switch_to.context(context_name)

    @classmethod
    def get_page_source(self):
        # web及app的webview页面可用，用于返回页面源码
        return self.driver.page_source

    @classmethod
    def get_android_display_resolution(self):
        # 安卓可用，获取安卓屏幕分辨率
        r = os.popen("adb shell dumpsys display | findstr PhysicalDisplayInfo").read()
        if "not found" in r or not r:
            r = os.popen("adb shell wm size").read()
            resolution = r.replace("\n", "").replace("\r", "").split(": ")[1].split("x")
        else:
            resolution = r.split('{')[1].split(',')[0].replace(' ', '').split("x")
        width = resolution[0]
        height = resolution[1]
        print("获取到分辨率：%sx%s" % (width, height))
        return int(width), int(height)

    @classmethod
    def swipe(self, start_x, start_y, end_x, end_y, dur=800):
        # start_x: 滑动起始点横坐标
        # start_y: 滑动起始点纵坐标
        # end_x：滑动终点横坐标
        # end_y：滑动终点纵坐标
        # dur：在多少时间内完成滑动动作（单位：ms毫秒）
        return self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=dur)

    @classmethod
    def restart_app(self):
        # 安卓可用，重启app
        self.driver.close_app()
        self.driver.launch_app()

    @classmethod
    def restart(self):
        self.driver.quit()
        self.driver = sdriver.Chrome()
        self.driver.get(self.dataProject["startPage"])

    @classmethod
    def quit(self):
        self.driver.quit()

    @classmethod
    def restart_browser(self, func):
        # web可用，重启浏览器
        def wraper(*arg, **kwargs):
            self.restart()
            return func(*arg, **kwargs)

        return wraper

    @classmethod
    def close_browser(self, func):
        # 关闭Web浏览器
        def wraper(*arg, **kwargs):
            self.quit()
            return func(*arg, **kwargs)

        return wraper

    @classmethod
    def access_new_tab_by_click_link(self, locator):
        # 仅Web测试可用: 通过点击链接进入新页签
        try:
            windows_before = self.driver.window_handles
            el = self.find_element(locator)
            self.click(el)
            windows_after = self.driver.window_handles
            while windows_before == windows_after:
                time.sleep(1)
                windows_after = self.driver.window_handles
            for newWindow in windows_after:
                if newWindow not in windows_before:
                    self.driver.switch_to.window(newWindow)
                    print("Switched to new window")
        except Exception:
            raise

    @classmethod
    def hide_app_to_backend(self):
        # 按Home键隐藏app到后台
        return self.driver.press_keycode(3)

    @classmethod
    def compare_image_the_same_use_pil(self, source_image_element_path_original, source_image_element_path_current):
        # Deprecated, PIL对比图片相似度
        image1 = Image.open(source_image_element_path_original)
        image2 = Image.open(source_image_element_path_current)
        histogram1 = image1.histogram()
        histogram2 = image2.histogram()
        differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))))
        print("差异度:", differ)
        if differ <= 100:
            return True
        else:
            return False

    @classmethod
    def drag_from_to(self, locator_original, locator_destination):
        e1 = self.find_element(locator_original)
        e2 = self.find_element(locator_destination)
        return self.driver.drag_and_drop(e1, e2)

    @classmethod
    def execute_script(self, script):
        return self.driver.execute_script(script)

    @classmethod
    def get_current_url(self):
        return self.driver.current_url

    @classmethod
    def goto_url(self, url):
        return self.driver.get(url)

    # 获取该元素并点击
    @classmethod
    def find_and_click(self, locator):
        aim_element = self.find_element(locator)
        return self.click(aim_element)

    @classmethod
    def find_and_send_keys(self, locator, text):
        aim_element = self.find_element(locator)
        return self.send_keys(aim_element, text)

    @classmethod
    def find_select_element(self, locator):
        # 轮询查找Select（下拉列表）类型的元素
        return sselect(self.find_element(locator))

    @classmethod
    def select_by_value(self, element, text):
        """
        按照select的value选择列表中的选项。由于列表经常加载缓慢，所以采用轮询的方式
        :param element:
        :param text:
        :return:
        """
        for i in range(0, self.timeOut, 1):
            try:
                return element.select_by_value(text)
            except NoSuchElementException:
                time.sleep(1)

    @classmethod
    def find_and_select_by_value(self, locator, text):
        # 查找并选择元素
        select_element = self.find_select_element(locator)
        return self.select_by_value(select_element, text)

    @classmethod
    def find_element_text(self, locator):
        # 获取该元素的文本
        aim_element = self.find_element(locator)
        return aim_element.text

    """Author：tyw"""

    @classmethod
    def click_until_clickable(self, locator):
        """
        在超时时间内尝试点击，直到点击成功
        :param locator:
        :return:
        """
        for i in range(self.timeOut * 2):
            try:
                aim_element = self.find_element(locator)
                self.click(aim_element)
            except WebDriverException:
                time.sleep(0.5)

    # Parson
    @classmethod
    def click_device_btn(self, key_num):
        # 安卓设备物理按键
        return self.driver.keyevent(key_num)

    @classmethod
    def wait_activity_display(self, activity, timeout=10):
        # 等待对应的Activity出现，超时时间默认设置10s
        return self.driver.wait_activity(activity, timeout)

    # @classmethod
    @property
    def contexts(self):
        return self.driver.contexts

    @property
    def switch_to(self):
        return self.driver.switch_to

    # @classmethod
    # def find_element_until_clickable(self, locator):
    #     # 超时时间内循环查找元素，直到元素可用为止 - 有时候driver已经找到元素，但是页面还没渲染完全，导致下一步点击会失败
    #     # 下面一行是调试用代码
    #     d1 = datetime.datetime.now()
    #     d2 = datetime.datetime.now()
    #     passed_time = (d2 - d1).seconds
    #     while passed_time < self.timeOut:
    #         try:
    #             ele = self.driver.find_element(locator[0], locator[1])
    #             if ele.is_enabled():
    #                 return ele
    #             else:
    #                 continue
    #         except NoSuchElementException:
    #             try:
    #                 # 如果遇到网络不好的情况，开发应在此定义一个页面加载超时出现的元素，点击后触发重新加载
    #                 time_out_element = self.driver.find_element_by_id("com.hongfans.rearview:id/iv_error_load")
    #                 time_out_element.click()
    #                 continue
    #             except NoSuchElementException:
    #                 print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
    #             os.system("echo Retrying to find element...")
    #             time.sleep(0.5)
    #             d2 = datetime.datetime.now()
    #             passed_time = (d2 - d1).seconds
    #     print("Can not find element specified -> ", locator)
    #     raise NoSuchElementException

    @classmethod
    def find_element_until_visibility(self, locator, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    @classmethod
    def find_element_until_clickable(self, locator, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    @classmethod
    def long_press(self, el=None, x=None, y=None, duration=1000):
        # 模拟长按操作
        return TouchAction(self.driver).long_press(el, x, y, duration).perform()

    @classmethod
    def press_btn(self,el=None, x=None,y=None):
        # 通过坐标点击操作
        return TouchAction(self.driver).press(el,x,y).perform()


    @classmethod
    def is_toast_exist(self, locator, timeout=10):
        # 获取toast
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    @classmethod
    def is_toast(self, locator, timeout=10):
        # 用于校验toast是否存在
        Flag = None
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            Flag = True
            return Flag
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
            Flag = False
            return Flag
        finally:
            return Flag

    @classmethod
    def get_toast(self, text=None, timeout=5, poll_frequency=0.5):
        if text:
            toast_loc = ("//*[contains(@text, '%s')]" %text)
        else:
            toast_loc= "//*[@class='android.widget.Toast']"
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(('xpath', toast_loc)))
            toast_ele = self.driver.find_element_by_xpath(toast_loc)
            return toast_ele
        except:
            return "Toast no found"

    @classmethod
    def get_text_ele(self, ele_class=None, text=None, timeout=5):
        """根据传入的text值来返回该元素"""
        if text:
            #text_xpath = ("//android.widget.TextView[@text='%s']" %text)
            text_xpath = ("//%s[@text='%s']" %(ele_class, text))
        else:
            text_xpath = "//android.widget.TextView"
        try:
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located('xpath', text_xpath))
            text_ele = self.driver.find_element_by_xpath(text_xpath)
            return text_ele
        except:
            return "ele no found"

    @classmethod
    def app_close(self):
        self.driver.close_app()

    @classmethod
    def get_timestamp(self):
        # 获取时间戳,仅获取时间戳小数点前面一串
        t = str(time.time()).split('.')[0]
        return t

    @classmethod
    def save_screen_shot(self, filename):
        # 获取手机截屏并保存文件
        self.driver.get_screenshot_as_file(filename)

    def save_screen_png(self):
        #获取手机截屏
        self.driver.get_screenshot_as_png()

    @classmethod
    def get_display_size(self, filename):
        # 此方法结合save_screenshot方法可获取IOS/Android的像素尺寸
        self.save_screen_shot(filename)
        with open(filename, 'rb') as fp:
            img = Image.open(fp)
            width = img.size[0]
            height = img.size[1]
        print("获取到分辨率：%sx%s" % (width, height))
        return int(width), int(height)

    @classmethod
    def cut_images(self, source_path, size_list, target_path):
        """
        此方法用于裁剪图片，主要是避免手机的时间及电量不同造成图片不同
        :param source_path: 目标图片，一般是屏幕截图
        :param size_list: 截取图片的大小，传入一个列表，前两位表示截取的起始坐标，后两位表示截取的目标坐标
        :param target_path: 截取完，保存图片的路径及文件名
        下面的x表示横坐标偏移的尺寸，y表示纵坐标偏移的尺寸
        """
        image = Image.open(source_path)
        newIM = image.crop((size_list[0], size_list[1], size_list[2], size_list[3]))
        x = size_list[2] - size_list[0]
        y = size_list[3] - size_list[1]
        newIM.resize((x, y), Image.ANTIALIAS).save(target_path)

    @classmethod
    def compare_image_with_hash(self, image_file1, image_file2, max_dif=0):
        """
        均值哈希算法比对，此算法精确度不够
        :param image_file1: 图片1，使用绝对路径
        :param image_file2: 图片2，使用绝对路径
        :param max_dif: 允许最大hash差值, 越小越精确,最小为0，推荐使用0
        :return:
        """
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        hash_1 = None
        hash_2 = None
        with open(image_file1, 'rb') as fp:
            hash_1 = imagehash.average_hash(Image.open(fp))
            # print(hash_1)
        with open(image_file2, 'rb') as fp:
            hash_2 = imagehash.average_hash(Image.open(fp))
            # print(hash_2)
        dif = hash_1 - hash_2
        print("两张图片差异度：%s" % dif)
        if dif < 0:
            dif = -dif
        if dif <= max_dif:
            return True
        else:
            return False

    @classmethod
    def compare_image_with_phash(self, image_file1, image_file2, max_dif=0):
        """
        感知哈希算法比对，此算法精确度较比值哈希算法高
        :param image_file1: 图片1，使用绝对路径
        :param image_file2: 图片2，使用绝对路径
        :param max_dif: 允许最大hash差值, 越小越精确,最小为0，推荐使用0
        :return:
        """
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        hash_1 = None
        hash_2 = None
        with open(image_file1, 'rb') as fp:
            hash_1 = imagehash.phash(Image.open(fp))
            # print(hash_1)
        with open(image_file2, 'rb') as fp:
            hash_2 = imagehash.phash(Image.open(fp))
            # print(hash_2)
        dif = hash_1 - hash_2
        print("两张图片差异度：%s" % dif)
        if dif < 0:
            dif = -dif
        if dif <= max_dif:
            return True
        else:
            return False

    @classmethod
    def find_elements_until_visibility(self, locator, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))
            return ele
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException


    @classmethod
    def is_element(self, locator, timeout=10):
        # 判断当前页面包含某元素,有返回True,无返回FALSE
        Flag = None
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            Flag = True
        except NoSuchElementException:
            print("Retrying to find element by %s: %s" % (locator[0], locator[1]))
            Flag = False
        # raise NoSuchElementException
        finally:
            return Flag

    @classmethod
    def get_screenshot_by_base64(self):
        """截图操作,用于将截图呈现于报告中"""
        return self.driver.get_screenshot_as_base64()

    @classmethod
    def adb_button(self,keyboard):
        # 安卓可用,通过adb指令模拟键盘输入
        str = "adb shell input keyevent {keyboard}".format(keyboard=keyboard)
        os.system(str)

    @classmethod
    def adb_press(self, x,y):
        # 安卓可用,通过adb指令模拟键盘输入
        str = "adb shell input tap {X} {Y}".format(X=x,Y=y)
        os.system(str)

    @classmethod
    def swipeElementLeft(self, element, t=800):
        """
        向左滑动指定元素
        :param element: 滑动的元素
        :param t: 持续时间
        :return:
        """
        #获取屏幕宽度和高度
        screen_width = int(self.driver.get_window_size()['width'])
        screen_height = int(self.driver.get_window_size()['height'])
        #获取元素开始坐标
        #获取组件高度和宽度
        #获取组件的坐标
        x_location = element.getLocation().getX()
        pass

    def swipeElement(self, ele):
        """
        滑动到指定元素
        :param ele:
        :param t:
        :return:
        """
        # 获取屏幕宽度和高度
        screen_width = int(self.driver.get_window_size()['width'])
        screen_height = int(self.driver.get_window_size()['height'])
        #默认没找到元素
        is_find = False
        while is_find is not True:
            try:
                ele_find = self.driver.find_element_by_id(ele)
                is_find = True

            except NoSuchElementException:
                #操作上滑
                self.swipe(screen_width*0.5, screen_height*0.9, screen_width*0.5, screen_height*0.2, 1000)
        return ele_find

    def save_screenshot(self):
        """
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        """
        base_url = os.getcwd()
        file_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        file_name = base_url + str(file_time) + '.png'
        self.driver.save_screenshot(file_name)
        with open(file_name, mode="rb") as f:
            file = f.read()
        return file

    def getSize(self):
        """
        获取屏幕宽高
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipe_control(self, direction = 'd'):
        """
        滑动，根据传入的参数控制滑动的方向：
        swipe与flick，swipe函数支持设置滑动的持续时间，
        flick将屏幕从一个点快速滑动到另一个点
        :param direction: 滑动方向，默认向下，左l，右r，上u
        :return:
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x_c = width * 0.5
        x_l = width * 0.2
        x_r = width * 0.8
        y_c = height * 0.5
        y_d = height * 0.8
        y_u = height * 0.2
        if direction == 'd':
            self.swipe(x_c, y_c, x_c, y_d)
        elif direction == 'u':
            self.swipe(x_c, y_c, x_c, y_u)
        elif direction == 'l':
            self.swipe(x_c, y_c, x_l, y_c)
        else:
            self.swipe(x_c, y_c, x_r, y_c)




if __name__ == '__main__':
    ele_class = "android.widget.RelativeLayout"
    text = "哈哈哈"
    driver = AutoDriver()
    driver.get_text_ele(ele_class, text)