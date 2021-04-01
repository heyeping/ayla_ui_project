#@project:  ayla_ui_project
#@author: heyeping
#@file: Op_config.py
#@ide: PyCharm
#@time: 2021/4/1 10:20 AM

import os
import yaml, json, configparser
from loguru import logger

class Config(object):

    def __init__(self, file):
        self.file = file

    def readYaml(self, sec, val):
        """
        读yaml文件
        :param sec:
        :param val:
        :return:
        """
        with open(self.file, 'r', encoding='utf-8') as fp:
            result = yaml.load(fp, Loader=yaml.FullLoader)
            data = result[sec][val]
        logger.info("读到数据===>>{}".format(data))
        return data

    def writeYaml(self, value):
        """
        写yaml文件
        :param value: 写入的值
        :return:
        """
        with open(self.file, 'w', encoding="utf-8") as fp:
            yaml.dump(value, stream=fp, allow_unicode=True)

    def readJson(self, key):
        with open(self.file, encoding='utf-8') as fp:
            result = json.load(fp)
            data = result[key]
        logger.info("读到数据===>>{}".format(data))
        return data

    def readIni(self, option, section):
        conf = configparser.ConfigParser()
        conf.read(self.file)
        data = conf.get(option, section)
        logger.info("读到数据===>>{}".format(data))
        return data

if __name__ == "__main__":
    base_url = os.path.abspath(os.path.dirname(os.getcwd()))
    yamlFile = os.path.join(base_url, 'config', 'token.yaml')
    jsonFlie = os.path.join(base_url, 'config', 'token.json')
    iniFlie = os.path.join(base_url, 'config', 'token.ini')
    yamlData = Config(yamlFile).readYaml("common", "token")
    data1 = {
        "common":{
            "token": "xiejinqude"
        }
    }
    Config(yamlFile).writeYaml(value=data1)

