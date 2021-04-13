#@project:  ayla_ui_project
#@author: heyeping
#@file: Base.py.py
#@ide: PyCharm
#@time: 2021/4/12 3:25 PM

import grpc
import importlib
import sys
import os
import re

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
print(rootPath)
sys.path.append(rootPath)
sys.path.append(curPath)

class BaseRpc(object):

    def __init__(self, url, proto):
        channel = grpc.insecure_channel(url)
        #导入pb2，pb2_grpc
        self.pb2_grpc = importlib.import_module('pb_files.' + proto + '_pb2_grpc')
        self.pb2 = importlib.import_module('pb_files.' + proto + '_pb2')
        #获取pb2_grpc文件的具体内容
        self.pb2_grpc_path = self.pb2_grpc.__file__
        print(self.pb2_grpc_path)
        self.pb2_grpc_data = self.__get_pb2_grpc__()
        print(self.pb2_grpc_data)
        #获取stub服务名称
        self.server = self.__get_server__()
        #创建stub服务
        self.stub = getattr(self.pb2_grpc, self.server)(channel)

    def __get_server__(self):
        """ 正则提取stub服务名称 """
        pattern = 'class (.+?Stub)\\(object\\):'
        try:
            cl = re.findall(pattern,self.pb2_grpc_data)
            if len(cl) != 1:
                raise 'stub服务提取失败'
        except Exception as e:
            print('生成的pb2_grpc文件中的stub数量错误:',repr(e))
            raise
        return cl[0]

    def __get_pb2_grpc__(self):
        """ 获取pb2_grpc文件内容，方便后续正则提取 """
        with open(self.pb2_grpc_path,'r') as f:
            data = f.read()
        return data

    def __get_request__(self, rpc):
        """正则提取要调用的rpc接口的request_serializer的值"""
        pattern = self.server.replace('Stub', '') + '/' + rpc + '\',\n[\\s\\S]*?request_serializer=([\\s\\S]*?),\n'
        try:
            rq = re.findall(pattern, self.pb2_grpc_data)
            if len(rq) != 1:
                raise 'request_serializer提取失败'
        except Exception as e:
            print('生成的pb2_grpc文件中的rq数量错误：', repr(e))
            raise
        rq = rq[0].split('.')[:-1]
        return rq

    def __req_join__(self, key, value):
        """当rpc请求的message部分有嵌套调用时，重新组合传递的参数"""
        if isinstance(value, str):
            return str(key)+ '=\'' + str(value) + '\','
        else:
            return str(key)+ '=' + str(value) + ','

    def __reg_nest__(self, head_req, data):
        """判断rpc请求的message部分是否有嵌套调用，处理嵌套部分的参数"""
        is_d = False
        d_req = ''
        for i in list(data.keys()):
            if '@' in i:
                s_req = ''
                message_func, item = i.split('.')
                message_func = message_func.replace('@', '')
                for j in data[i]:
                    s_req += self.__req_join__(j, data[i][j])
                if head_req not in dir(self.pb2):
                    data[item] = 'self.pb2.' + mgessage_func + '(' + str(s_req[:-1]) + ')'
                else:
                    data[item] = str('self.pb2.' + head_req) + '.' + mgessage_func + '(' + str(s_req[:-1]) + ')'



if __name__ == '__main__':
    b = BaseRpc("106.15.231.103:9098", 'Auth')
    rq = b.__get_request__('login')
    print(rq)