#@project:  ayla_ui_project
#@author: heyeping
#@file: Device_client.py.py
#@ide: PyCharm
#@time: 2021/3/30 4:41 PM
#编译命令：python3 -m grpc_tools.protoc --python_out=../pb_files --grpc_python_out=../pb_files -I. DeviceService.proto

from gRPC.conmon.Op_config import Config
from gRPC.pb_files import DeviceService_pb2
from gRPC.pb_files import DeviceService_pb2_grpc
from gRPC.client.Login_client import LoginClient
import grpc,json,os
from loguru import logger

class Device_client():

    def __init__(self, address, file):
        """
        链接服务器
        :param address: 服务器地址
        """
        self.address = address
        self.chanel = grpc.insecure_channel(self.address)
        # 调用gpr服务
        self.stub = DeviceService_pb2_grpc.DeviceServiceStub(self.chanel)
        #调用LogintClient，获取token
        #self.login_client = LoginClient(self.address)
        #self.token = self.login_client.login(phone, verificationCode)
        #print(self.token)
        self.file = file
        #从yaml文件中读取token
        self.token = Config(self.file).readYaml("common", "token")


    def binDevice(self, cuId, deviceId, nickName):
        """
        绑定设备接口
        :param cuId: 设备品牌，0为艾拉，1为阿里
        :param deviceId: 设备dsn
        :param nickName: 设备名称
        :return:
        """
        try:
            #请求绑定设备接口
            response = self.stub.bindDevice(
                request=DeviceService_pb2.BindDeviceReq(cuId=cuId, deviceId=deviceId, nickName=nickName),
                metadata=(('authorization', self.token),)
            )
            print(response)
            logger.info("绑定设备接口返回===>>{}".format(response))
        except grpc.RpcError as e:
            print(e.code())

    def getDeviceList(self):
        """
        获取设备接口
        :return:
        """
        try:
            #请求获取设备列表接口
            response = self.stub.getDeviceList(request=DeviceService_pb2.DeviceListResp(), metadata=(('authorization', self.token),))
            print(response)
        except grpc.RpcError as e:
            print(e.code())

    def getDeviceInfo(self, deviceId):
        """
        获取设备信息
        :param deviceId: dsn
        :return:
        """
        response = self.stub.getDeviceInfo(
            request=DeviceService_pb2.DeviceReq(deviceId=deviceId),
            metadata=(('authorization', self.token),)
        )

    def setDeviceProperty(self, deviceId, propertyName, propertyValue):
        """
        设置设备属性
        :param deviceId: 设备dsn
        :param propertyName: 属性名称
        :param propertyValue: 属性值
        :return:
        """
        try:
            response = self.stub.setDeviceProperty(
                request=DeviceService_pb2.SetDevicePropertyReq(deviceId=deviceId, propertyName=propertyName, propertyValue=propertyValue),
                metadata=(('authorization', self.token),)
            )
            return response
        except grpc.RpcError as e:
            print(e.code())


    def getDeviceProperty(self, deviceId, propertyName):
        """
        获取设备属性
        :param deviceId: 设备dsn
        :param propertyName: 属性名称
        :return:
        """


if __name__ == "__main__":
    ads = "106.15.231.103:9098"
    base_url = os.path.abspath(os.path.dirname(os.getcwd()))
    yamlFile = os.path.join(base_url, 'config', 'token.yaml')
    dc = Device_client(address=ads,file=yamlFile)
    cuId = 4
    deviceId = "  "
    nickName = ""
    dc.binDevice(cuId,deviceId,nickName)
    dc.getDeviceList()

