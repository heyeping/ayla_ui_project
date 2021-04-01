#@project:  ayla_ui_project
#@author: heyeping
#@file: header_test.py.py
#@ide: PyCharm
#@time: 2021/3/29 6:45 PM

import grpc
import collections
import DeviceService_pb2
import DeviceService_pb2_grpc

class _GenericClientInterceptor(
        grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor,
        grpc.StreamUnaryClientInterceptor, grpc.StreamStreamClientInterceptor):

    def __init__(self, interceptor_function):
        self._fn = interceptor_function

    def intercept_unary_unary(self, continuation, client_call_details, request):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, iter((request,)), False, False)
        response = continuation(new_details, next(new_request_iterator))
        return postprocess(response) if postprocess else response

    def intercept_unary_stream(self, continuation, client_call_details,
                               request):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, iter((request,)), False, True)
        response_it = continuation(new_details, next(new_request_iterator))
        return postprocess(response_it) if postprocess else response_it

    def intercept_stream_unary(self, continuation, client_call_details,
                               request_iterator):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator, True, False)
        response = continuation(new_details, new_request_iterator)
        return postprocess(response) if postprocess else response

    def intercept_stream_stream(self, continuation, client_call_details,
                                request_iterator):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator, True, True)
        response_it = continuation(new_details, new_request_iterator)
        return postprocess(response_it) if postprocess else response_it


def create(intercept_call):
    return _GenericClientInterceptor(intercept_call)

class _ClientCallDetails(
        collections.namedtuple(
            '_ClientCallDetails',
            ('method', 'timeout', 'metadata', 'credentials')),
        grpc.ClientCallDetails):
    pass


def header_adder_interceptor(header, value):

    def intercept_call(client_call_details, request_iterator, request_streaming,
                       response_streaming):
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        metadata.append((
            header,
            value,
        ))
        client_call_details = _ClientCallDetails(
            client_call_details.method, client_call_details.timeout, metadata,
            client_call_details.credentials)
        return client_call_details, request_iterator, None

    return create(intercept_call)

server_address='106.15.231.103:9098'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMzAwNjA1NzAyNjE5ODUyODQyIiwidXNlck5hbWUiOiIxMzI2NzkyNTA3NSIsImxvZ2luVHlwZSI6IjMiLCJsb2dpblNvdXJjZSI6IjExIiwiYXlsYUFwcGxpY2F0aW9uSWQiOiIxMCIsInR5cGUiOiJhdXRoX3Rva2VuIiwiaWF0IjoxNjE3MDE1MjA1fQ.F1_tclk45mF51gukG68UFafGcgr_ZBJ36E9pTOdd1Jc'
header_adder_interceptor = header_adder_interceptor('Authorization', token)
channel = grpc.insecure_channel(server_address) #使用https证书的方法，需要可以参考一下，不需要证书可以使用grpc.insecure_channel()
intercept_channel = grpc.intercept_channel(channel, header_adder_interceptor)
#stub = resume_pb2_grpc.ResumeStub(intercept_channel)
stub = DeviceService_pb2_grpc.DeviceServiceStub(intercept_channel)
response= stub.bindDevice(DeviceService_pb2.BindDeviceReq(cuId=0, deviceId="AC000W017808957", nickName="test"))