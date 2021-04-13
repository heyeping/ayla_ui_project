#@project:  ayla_ui_project
#@author: heyeping
#@file: grpc_common.py.py
#@ide: PyCharm
#@time: 2021/4/2 5:41 PM

import grpc
import time

def common(service_dependence, request, _response, server='0.0.0.0:7000', **kwargs):
    # proto生成两个python文件：pd2_grpc结尾的service_stub的文件和pd2结尾的服务定义的文件
    pb2_grpc = service_dependence['pb2_grpc']
    # pb2_grpc_func 是生成stub对象的方法
    pb2_grpc_func = service_dependence['pb2_grpc_func']
    pb2 = service_dependence['pb2']
    # pb2_func 是关联服务中方法和请求参数的方法
    pb2_func = service_dependence['pb2_func']

    # 引用proto生成的两个文件
    import_pb2_grpc = 'import ' + pb2_grpc
    import_pb2 = 'import ' + pb2
    exec(import_pb2_grpc)
    exec(import_pb2)

    # 通用调用
    grpc_stub = pb2_grpc + '.' + pb2_grpc_func
    grpc_request = pb2 + '.' + pb2_func
    channel = grpc.insecure_channel(server)
    stub = eval(grpc_stub)(channel)
    start_time = time.time()
    response = eval("stub." + request)(eval(grpc_request)(**kwargs))
    end_time = time.time()
    # 服务耗时：以毫秒为单位
    elapsed = str(round((end_time - start_time)*1000, 3)) + 'ms'
    # 主要返回内容：如果方法的返回字段不能统一，也可以考虑传入一个返回字段的列表，把此处改写
    content = response.error_msg if response.code else eval("response." + _response)
    return response.code, content, elapsed