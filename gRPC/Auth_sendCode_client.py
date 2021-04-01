#@project:  ayla_ui_project
#@author: heyeping
#@file: Auth_sendCode_client.py.py
#@ide: PyCharm
#@time: 2021/3/25 2:50 PM

import grpc
import auth_pb2
import auth_pb2_grpc

def run():

    #连接rpc服务器
    channel = grpc.insecure_channel('106.15.231.103:9098')
    #调用rpc服务
    stub = auth_pb2_grpc.AuthServiceStub(channel)
    #response1 = stub.login(auth_pb2.LoginReq(phone="13267925075",verificationCode="123456"))
    #请求验证码接口
    response2 = stub.sendVerificationCode(auth_pb2.VerificationCodeReq(phone="13267925075"))
    print("received:", response2)
    print(type(response2))

if __name__ == '__main__':
    run()


