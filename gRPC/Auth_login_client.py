#@project:  ayla_ui_project
#@author: heyeping
#@file: Auth_login_client.py.py
#@ide: PyCharm
#@time: 2021/3/26 2:29 PM

import grpc
import auth_pb2
import auth_pb2_grpc

def getToken():

    #连接rpc服务器
    channel = grpc.insecure_channel('106.15.231.103:9098')
    #调用rpc服务
    stub = auth_pb2_grpc.AuthServiceStub(channel)
    #请求登录接口
    response = stub.login(auth_pb2.LoginReq(phone="13267925075",verificationCode="163356"))
    #print("received:", response)
    #print("authToken:", response.authToken)
    result = str(response)
    print(result)
    token = str(response.authToken)
    return token

if __name__ == '__main__':
    token = getToken()
    print(token)