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
        "account": "13267925075",
        "password": "123456"
    }
    res = requests.post(url=login_url, json= param_login).json()
    #print(res)
    token = res['data']['authToken']
    return token

def set_property(deviceId, propertyCode, propertyValue, header):
    url = "https://miya-h5-test.ayla.com.cn/api/v1/build/device/{deviceId}/property".format(deviceId=deviceId)
    param1 = {
        "propertyCode": propertyCode,
        "propertyValue": propertyValue
    }
    now_time = datetime.datetime.now()
    res = requests.put(url=url, json= param1,headers=header).json()
    print(res)
    if res['msg'] == 'success':
        print("{now_time}下发成功".format(now_time=now_time))
    else:
        print("下发失败")


if __name__ == "__main__":
    token = get_token()
    print(token)
    deviceId = "VR00ZN000025134"
    header = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': token,
        'serviceId': "3"
    }
    propertyCode = "1:0x0006:Onoff"
    n = 10
    now_time = datetime.datetime.now()
    #循环下发20次
    for i in range(n):
        set_property(deviceId,propertyCode,0,header)
        i += 1
        time.sleep(1)
        set_property(deviceId,propertyCode,1,header)
        time.sleep(1)