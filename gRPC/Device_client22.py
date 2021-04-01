#@project:  ayla_ui_project
#@author: heyeping
#@file: Device_client.py.py
#@ide: PyCharm
#@time: 2021/3/26 4:54 PM

import grpc
import DeviceService_pb2
import DeviceService_pb2_grpc

def bindDeviceTest():

    with grpc.insecure_channel('106.15.231.103:9098') as channel:
        stub = DeviceService_pb2_grpc.DeviceServiceStub(channel)
        metadata = (
            ("Authorization","eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMzAwNjA1NzAyNjE5ODUyODQyIiwidXNlck5hbWUiOiIxMzI2NzkyNTA3NSIsImxvZ2luVHlwZSI6IjMiLCJsb2dpblNvdXJjZSI6IjExIiwiYXlsYUFwcGxpY2F0aW9uSWQiOiIxMCIsInR5cGUiOiJhdXRoX3Rva2VuIiwiaWF0IjoxNjE3MDA0MzQ5fQ.E17EGXeXyOKX2UwAH7BqroJ64OEN6rE-RC3t821scYE"),
        )
        response, call = stub.bindDevice.with_call(
            DeviceService_pb2.BindDeviceReq(cuId=0, deviceId="AC000W017808957", nickName="test"),
            metadata=metadata)

    print("Greeter client received: " + response)

if __name__ == '__main__':
    bindDeviceTest()