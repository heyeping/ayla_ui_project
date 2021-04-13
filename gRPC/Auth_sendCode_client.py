#@project:  ayla_ui_project
#@author: heyeping
#@file: Auth_sendCode_client.py.py
#@ide: PyCharm
#@time: 2021/3/25 2:50 PM

import grpc
import auth_pb2
import auth_pb2_grpc
from gRPC.util.CertCreate import CertCreate

def run():

    #获取安全证书
    cert = CertCreate()
    #连接rpc服务器，不是HTTPS不需要证书可以使用grpc.insecure_channel()
    channel = grpc.secure_channel(target="referenceapp-test.ayla.com.cn:9098",credentials=cert)
    #调用rpc服务
    stub = auth_pb2_grpc.AuthServiceStub(channel)
    #response1 = stub.login(auth_pb2.LoginReq(phone="13267925075",verificationCode="123456"))
    #请求验证码接口
    response2 = stub.sendVerificationCode(auth_pb2.VerificationCodeReq(phone="13267925075"))
    print("received:", response2)
    print(type(response2))

if __name__ == '__main__':
    run()


