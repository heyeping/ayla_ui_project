#@project:  ayla_ui_project
#@author: heyeping
#@file: Device_client.py.py
#@ide: PyCharm
#@time: 2021/3/26 4:54 PM

import grpc
import DeviceService_pb2
import DeviceService_pb2_grpc

def bindDeviceTest():

    #连接rpc服务器
    channel = grpc.insecure_channel('106.15.231.103:9098')
    # 调用rpc服务
    stub = DeviceService_pb2_grpc.DeviceServiceStub(channel)

    #请求设备列表接口
    token ='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMzAwNjA1NzAyNjE5ODUyODQyIiwidXNlck5hbWUiOiIxMzI2NzkyNTA3NSIsImxvZ2luVHlwZSI6IjMiLCJsb2dpblNvdXJjZSI6IjExIiwiYXlsYUFwcGxpY2F0aW9uSWQiOiIxMCIsInR5cGUiOiJhdXRoX3Rva2VuIiwiaWF0IjoxNjE3MjU2NDg0fQ.P63_aEEUfYNxanf8M2zZPRo8dbnXaIdmJf6BwfCTyVU'
    #token2 = token.lower()
    #print(token2)
    response = stub.bindDevice(
        request=DeviceService_pb2.BindDeviceReq(cuId=0, deviceId="  ", nickName=""),
        metadata=(
            ('authorization', token),
        ))
    print(response)
    #print(call)

if __name__ == '__main__':
    bindDeviceTest()