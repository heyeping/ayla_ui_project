# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gRPC.pb_files import Base_pb2 as Base__pb2
from gRPC.pb_files import DeviceService_pb2 as DeviceService__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DeviceServiceStub(object):
    """*
    设备相关接口
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.bindDevice = channel.unary_unary(
                '/DeviceService/bindDevice',
                request_serializer=DeviceService__pb2.BindDeviceReq.SerializeToString,
                response_deserializer=Base__pb2.Result.FromString,
                )
        self.getDeviceList = channel.unary_unary(
                '/DeviceService/getDeviceList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=DeviceService__pb2.DeviceListResp.FromString,
                )
        self.getDeviceInfo = channel.unary_unary(
                '/DeviceService/getDeviceInfo',
                request_serializer=DeviceService__pb2.DeviceReq.SerializeToString,
                response_deserializer=DeviceService__pb2.Device.FromString,
                )
        self.unBindDevice = channel.unary_unary(
                '/DeviceService/unBindDevice',
                request_serializer=DeviceService__pb2.UnBindDeviceReq.SerializeToString,
                response_deserializer=DeviceService__pb2.UnBindDeviceResp.FromString,
                )
        self.setDeviceProperty = channel.unary_unary(
                '/DeviceService/setDeviceProperty',
                request_serializer=DeviceService__pb2.SetDevicePropertyReq.SerializeToString,
                response_deserializer=Base__pb2.Result.FromString,
                )
        self.getDeviceProperty = channel.unary_unary(
                '/DeviceService/getDeviceProperty',
                request_serializer=DeviceService__pb2.GetDevicePropertyReq.SerializeToString,
                response_deserializer=DeviceService__pb2.DevicePropertyResp.FromString,
                )
        self.getDeviceProperties = channel.unary_unary(
                '/DeviceService/getDeviceProperties',
                request_serializer=DeviceService__pb2.GetDevicePropertiesReq.SerializeToString,
                response_deserializer=DeviceService__pb2.GetDevicePropertiesResp.FromString,
                )
        self.updateDevice = channel.unary_unary(
                '/DeviceService/updateDevice',
                request_serializer=DeviceService__pb2.UpdateDeviceReq.SerializeToString,
                response_deserializer=DeviceService__pb2.Device.FromString,
                )


class DeviceServiceServicer(object):
    """*
    设备相关接口
    """

    def bindDevice(self, request, context):
        """*
        绑定设备
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDeviceList(self, request, context):
        """*
        设备列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDeviceInfo(self, request, context):
        """*
        设备详情
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unBindDevice(self, request, context):
        """*
        设备解绑
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setDeviceProperty(self, request, context):
        """*
        设置设备属性值
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDeviceProperty(self, request, context):
        """*
        获取设备属性值
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDeviceProperties(self, request, context):
        """*
        获取设备所有属性值
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateDevice(self, request, context):
        """*
        编辑设备信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'bindDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.bindDevice,
                    request_deserializer=DeviceService__pb2.BindDeviceReq.FromString,
                    response_serializer=Base__pb2.Result.SerializeToString,
            ),
            'getDeviceList': grpc.unary_unary_rpc_method_handler(
                    servicer.getDeviceList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=DeviceService__pb2.DeviceListResp.SerializeToString,
            ),
            'getDeviceInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getDeviceInfo,
                    request_deserializer=DeviceService__pb2.DeviceReq.FromString,
                    response_serializer=DeviceService__pb2.Device.SerializeToString,
            ),
            'unBindDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.unBindDevice,
                    request_deserializer=DeviceService__pb2.UnBindDeviceReq.FromString,
                    response_serializer=DeviceService__pb2.UnBindDeviceResp.SerializeToString,
            ),
            'setDeviceProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.setDeviceProperty,
                    request_deserializer=DeviceService__pb2.SetDevicePropertyReq.FromString,
                    response_serializer=Base__pb2.Result.SerializeToString,
            ),
            'getDeviceProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.getDeviceProperty,
                    request_deserializer=DeviceService__pb2.GetDevicePropertyReq.FromString,
                    response_serializer=DeviceService__pb2.DevicePropertyResp.SerializeToString,
            ),
            'getDeviceProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.getDeviceProperties,
                    request_deserializer=DeviceService__pb2.GetDevicePropertiesReq.FromString,
                    response_serializer=DeviceService__pb2.GetDevicePropertiesResp.SerializeToString,
            ),
            'updateDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.updateDevice,
                    request_deserializer=DeviceService__pb2.UpdateDeviceReq.FromString,
                    response_serializer=DeviceService__pb2.Device.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DeviceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceService(object):
    """*
    设备相关接口
    """

    @staticmethod
    def bindDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/bindDevice',
            DeviceService__pb2.BindDeviceReq.SerializeToString,
            Base__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDeviceList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/getDeviceList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            DeviceService__pb2.DeviceListResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDeviceInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/getDeviceInfo',
            DeviceService__pb2.DeviceReq.SerializeToString,
            DeviceService__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def unBindDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/unBindDevice',
            DeviceService__pb2.UnBindDeviceReq.SerializeToString,
            DeviceService__pb2.UnBindDeviceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setDeviceProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/setDeviceProperty',
            DeviceService__pb2.SetDevicePropertyReq.SerializeToString,
            Base__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDeviceProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/getDeviceProperty',
            DeviceService__pb2.GetDevicePropertyReq.SerializeToString,
            DeviceService__pb2.DevicePropertyResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDeviceProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/getDeviceProperties',
            DeviceService__pb2.GetDevicePropertiesReq.SerializeToString,
            DeviceService__pb2.GetDevicePropertiesResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DeviceService/updateDevice',
            DeviceService__pb2.UpdateDeviceReq.SerializeToString,
            DeviceService__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
