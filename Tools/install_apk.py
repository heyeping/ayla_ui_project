#@project:  ayla_ui_project
#@author: heyeping
#@file: install_apk.py
#@ide: PyCharm
#@time: 2021/4/13 2:36 PM

import os
from loguru import logger
import time
from multiprocessing import Pool
curPath = os.path.abspath(os.path.dirname(__file__))
#print(curPath)
rootPath = os.path.split(curPath)[0]
#print(rootPath)

class appInstall(object):

    def __init__(self, filePath):
        self.filePath = filePath

    def get_devices(self):
        """获取devices数量和名称"""
        devices = []
        try:
            for dName in os.popen("adb devices"):
                if "\t" in dName:
                    if dName.find("emulator") < 0:
                        devices.append(dName.split('\t')[0])
            devices.sort(key=None, reverse=False)
            print(devices)
        except Exception as e:
            raise
        logger.info("\n设备名称:{} \n总数量:{}".format(devices, len(devices)))
        return devices

    def install_apk(self):
        """读取apk文件夹下的所有app文件，进行批量安装"""
        files = os.listdir(self.filePath)
        for apk in files:
            logger.info("正在安装{}-----".format(apk))
            apk_path = os.path.join(self.filePath, apk)
            os.system("adb install -d -r %s" % apk_path)
            logger.info("安装{}完毕".format(apk))
        logger.info("所有app已经安装完毕！")

    def install_apk2(self, device):
        """读取apk文件夹下的所有app文件，进行批量安装"""
        files = os.listdir(self.filePath)
        for apk in files:
            logger.info("正在安装{}-----".format(apk))
            apk_path = os.path.join(self.filePath, apk)
            os.system('adb -s' + device + ' install ' + apk_path)
            logger.info("安装{}完毕".format(apk))
        logger.info("所有app已经安装完毕！")

    def task_install(self, devices):
        startTime = time.time()
        #创建任务池
        pool = Pool(2)
        result = pool.map(self.install_apk2, devices)
        endTime = time.time()
        pool.close()
        pool.join()
        print(endTime)

    def uninstall_apk(self):
        """读取第三方apk列表并进行卸载"""


if __name__ == '__main__':
    path = os.path.join(rootPath, 'apk_files')
    #print(path)
    a = appInstall(path)
    devices = a.get_devices()
    a.task_install(devices)
    #a.install_apk()

