#@project:  ayla_ui_project
#@author: heyeping
#@file: helloworld_test.py.py
#@ide: PyCharm
#@time: 2021/3/25 2:40 PM

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():

    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='test'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()