# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rpc import common_pb2 as rpc_dot_common__pb2


class BluetoothClassicStub(object):
    """Bluetooth Classic service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_unary(
                '/rpc.BluetoothClassic/Scan',
                request_serializer=rpc_dot_common__pb2.DeviceScan.SerializeToString,
                response_deserializer=rpc_dot_common__pb2.ScanResult.FromString,
                )
        self.ScanBackground = channel.unary_stream(
                '/rpc.BluetoothClassic/ScanBackground',
                request_serializer=rpc_dot_common__pb2.DeviceScan.SerializeToString,
                response_deserializer=rpc_dot_common__pb2.ScanResult.FromString,
                )
        self.ScanBackgroundStop = channel.unary_unary(
                '/rpc.BluetoothClassic/ScanBackgroundStop',
                request_serializer=rpc_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=rpc_dot_common__pb2.StatusMessage.FromString,
                )


class BluetoothClassicServicer(object):
    """Bluetooth Classic service
    """

    def Scan(self, request, context):
        """Start a device scan of duration "time"
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScanBackground(self, request, context):
        """Enable background scanning with a reporting interval of "time"
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScanBackgroundStop(self, request, context):
        """Stop background scanning
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BluetoothClassicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=rpc_dot_common__pb2.DeviceScan.FromString,
                    response_serializer=rpc_dot_common__pb2.ScanResult.SerializeToString,
            ),
            'ScanBackground': grpc.unary_stream_rpc_method_handler(
                    servicer.ScanBackground,
                    request_deserializer=rpc_dot_common__pb2.DeviceScan.FromString,
                    response_serializer=rpc_dot_common__pb2.ScanResult.SerializeToString,
            ),
            'ScanBackgroundStop': grpc.unary_unary_rpc_method_handler(
                    servicer.ScanBackgroundStop,
                    request_deserializer=rpc_dot_common__pb2.Empty.FromString,
                    response_serializer=rpc_dot_common__pb2.StatusMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rpc.BluetoothClassic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BluetoothClassic(object):
    """Bluetooth Classic service
    """

    @staticmethod
    def Scan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc.BluetoothClassic/Scan',
            rpc_dot_common__pb2.DeviceScan.SerializeToString,
            rpc_dot_common__pb2.ScanResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScanBackground(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/rpc.BluetoothClassic/ScanBackground',
            rpc_dot_common__pb2.DeviceScan.SerializeToString,
            rpc_dot_common__pb2.ScanResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScanBackgroundStop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpc.BluetoothClassic/ScanBackgroundStop',
            rpc_dot_common__pb2.Empty.SerializeToString,
            rpc_dot_common__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)