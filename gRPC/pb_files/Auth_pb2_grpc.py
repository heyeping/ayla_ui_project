# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gRPC.pb_files import Auth_pb2 as Auth__pb2
from gRPC.pb_files import Base_pb2 as Base__pb2


class AuthServiceStub(object):
    """*
    登录相关接口
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendVerificationCode = channel.unary_unary(
                '/AuthService/sendVerificationCode',
                request_serializer=Auth__pb2.VerificationCodeReq.SerializeToString,
                response_deserializer=Base__pb2.Result.FromString,
                )
        self.login = channel.unary_unary(
                '/AuthService/login',
                request_serializer=Auth__pb2.LoginReq.SerializeToString,
                response_deserializer=Auth__pb2.Token.FromString,
                )


class AuthServiceServicer(object):
    """*
    登录相关接口
    """

    def sendVerificationCode(self, request, context):
        """*
        发送验证码
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login(self, request, context):
        """*
        登录
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendVerificationCode': grpc.unary_unary_rpc_method_handler(
                    servicer.sendVerificationCode,
                    request_deserializer=Auth__pb2.VerificationCodeReq.FromString,
                    response_serializer=Base__pb2.Result.SerializeToString,
            ),
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=Auth__pb2.LoginReq.FromString,
                    response_serializer=Auth__pb2.Token.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """*
    登录相关接口
    """

    @staticmethod
    def sendVerificationCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService/sendVerificationCode',
            Auth__pb2.VerificationCodeReq.SerializeToString,
            Base__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AuthService/login',
            Auth__pb2.LoginReq.SerializeToString,
            Auth__pb2.Token.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
