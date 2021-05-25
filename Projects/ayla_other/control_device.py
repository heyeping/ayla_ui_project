#@project:  ayla_ui_project
#@author: heyeping
#@file: control_device.py
#@ide: PyCharm
#@time: 2021/3/12 10:47 AM

"""控制设备
 post  https://miya-h5-test.ayla.com.cn/api/v1/build/device/{deviceId}/property

{
	"propertyCode": "1:0x0006:Onoff",
	"propertyValue": 1
}

"""
import requests,time,datetime
from threading import Timer
from loguru import logger

def get_token():
    """
    获取token
    :return:
    """
    login_url = "https://abp-test.ayla.com.cn/api/v1/build/user/login"
    header_login = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    param_login = {
        "account": "18002549655",
        "password": "Aa123456"
    }
    res = requests.post(url=login_url, json= param_login).json()
    #print(res)
    token = res['data']['authToken']
    return token

def set_property(deviceId, propertyCode, propertyValue, header):
    """
    设置设备属性
    :param deviceId:
    :param propertyCode:
    :param propertyValue:
    :param header:
    :return:
    """
    url = "https://miya-h5-test.ayla.com.cn/api/v1/build/device/{deviceId}/property".format(deviceId=deviceId)
    param1 = {
        "propertyCode": propertyCode,
        "propertyValue": propertyValue
    }
    now_time = datetime.datetime.now()
    res = requests.put(url=url, json= param1,headers=header).json()
    if res['msg'] == 'success':
        logger.info("{now_time}指令=={propertyValue}成功".format(now_time=now_time, propertyValue=propertyValue))
    else:
        print("下发失败")

def get_property(deviceId, propertyCode, header):
    """
    获取设备单个属性
    :param deviceId:
    :param propertyCode:
    :param header:
    :return:
    """
    url = "https://miya-h5-test.ayla.com.cn/api/v1/build/device/{deviceId}/property/{propertyCode}".format(
        deviceId=deviceId,propertyCode=propertyCode)
    res = requests.get(url=url, headers=header).json()
    return res


if __name__ == "__main__":
    token = get_token()
    print(token)
    deviceId = "VR00ZN000028022"
    header = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': token,
        'serviceId': "3"
    }
    propertyCode = "1:0x0006:Onoff"
    propertyCode2 = "2:0x0006:Onoff"
    n = 1
    #get_property(deviceId, propertyCode, header)
    now_time = datetime.datetime.now()
    #循环下发20次
    for i in range(n):
        set_property(deviceId,propertyCode,0,header)
        i += 1
        time.sleep(5)
        res = get_property(deviceId, propertyCode2, header)
        #print(flag)
        time_get = res['data']['updateTime'] / 1000
        #print(time_get)
        time_array = time.localtime(time_get)
        format_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        if res['data']['propertyValue'] == '0':
            logger.info("{format_time}获取到的动作值=={value},本地联动触发成功".format(
                format_time=format_time,value=res['data']['propertyValue']))
        else:
            print("本地联动触发失败")
        time.sleep(20)
        set_property(deviceId,propertyCode,1,header)
        time.sleep(5)
        res = get_property(deviceId, propertyCode2, header)
        #print(flag)
        time_get = res['data']['updateTime'] / 1000
        time_array = time.localtime(time_get)
        format_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        if res['data']['propertyValue'] == '1':
            logger.info("{format_time}获取到的动作值=={value},云端联动触发成功".format(
                format_time=format_time, value=res['data']['propertyValue']))
        else:
            print("云端联动触发失败")
        time.sleep(20)