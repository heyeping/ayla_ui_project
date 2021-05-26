#@project:  ayla_ui_project
#@author: heyeping
#@file: conftest.py.py
#@ide: PyCharm
#@time: 2021/5/25 4:16 PM

import pytest
from selenium import webdriver
import os
import allure

_driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    #获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    #仅仅获取用例call执行结果是失败的情况，不包含setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ''
            f.write(rep.nodeid + extra + "\n")
        #添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_pngg"):
            with allure.step("添加失败截图..."):
                allure.attach(_driver.get_screenshot_as_pngg(), "失败截图", allure.attachment_type.PNG)

@pytest.fixture(scope='session')
def appdriver():
    global _driver
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platfromVersion'] = '10'
    desired_caps['udid'] = '9YEDU18926003029'
    desired_caps['appPackage'] = 'com.ayla.hotelsaas'
    desired_caps['appActivity'] = 'com.ayla.hotelsaas.ui.SPlashActivity'
    desired_caps['noReset'] = True
    desired_caps['deviceName'] = 'Honor 10'
    if _driver is None:
        _driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wb/hub", desired_capabilities=desired_caps)
    yield _driver