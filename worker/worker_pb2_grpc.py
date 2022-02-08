# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import worker.worker_pb2 as worker__pb2


class BluetoothClassicServiceStub(object):
    """Bluetooth Classic service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_unary(
                '/worker.BluetoothClassicService/Scan',
                request_serializer=worker__pb2.DeviceScan.SerializeToString,
                response_deserializer=worker__pb2.ScanResult.FromString,
                )
        self.ScanBackground = channel.unary_stream(
                '/worker.BluetoothClassicService/ScanBackground',
                request_serializer=worker__pb2.DeviceScan.SerializeToString,
                response_deserializer=worker__pb2.ScanResult.FromString,
                )


class BluetoothClassicServiceServicer(object):
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


def add_BluetoothClassicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=worker__pb2.DeviceScan.FromString,
                    response_serializer=worker__pb2.ScanResult.SerializeToString,
            ),
            'ScanBackground': grpc.unary_stream_rpc_method_handler(
                    servicer.ScanBackground,
                    request_deserializer=worker__pb2.DeviceScan.FromString,
                    response_serializer=worker__pb2.ScanResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'worker.BluetoothClassicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BluetoothClassicService(object):
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
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothClassicService/Scan',
            worker__pb2.DeviceScan.SerializeToString,
            worker__pb2.ScanResult.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/worker.BluetoothClassicService/ScanBackground',
            worker__pb2.DeviceScan.SerializeToString,
            worker__pb2.ScanResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BluetoothLEServiceStub(object):
    """Bluetooth Low Energy
    Common bluetooth commands
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_unary(
                '/worker.BluetoothLEService/Scan',
                request_serializer=worker__pb2.DeviceScan.SerializeToString,
                response_deserializer=worker__pb2.ScanResult.FromString,
                )
        self.ScanBackground = channel.unary_stream(
                '/worker.BluetoothLEService/ScanBackground',
                request_serializer=worker__pb2.DeviceScan.SerializeToString,
                response_deserializer=worker__pb2.ScanResult.FromString,
                )
        self.Connect = channel.unary_unary(
                '/worker.BluetoothLEService/Connect',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.StatusMessage.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/worker.BluetoothLEService/Disconnect',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.StatusMessage.FromString,
                )
        self.ListBLEServices = channel.unary_unary(
                '/worker.BluetoothLEService/ListBLEServices',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.ListBLEServicesResult.FromString,
                )
        self.ListBLECharactersistics = channel.unary_unary(
                '/worker.BluetoothLEService/ListBLECharactersistics',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.ListBLECharactersisticsResult.FromString,
                )
        self.ListBLEDescriptors = channel.unary_unary(
                '/worker.BluetoothLEService/ListBLEDescriptors',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.ListBLEDescriptorsResult.FromString,
                )
        self.ReadBLEDescriptor = channel.unary_unary(
                '/worker.BluetoothLEService/ReadBLEDescriptor',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.BluetoothData.FromString,
                )
        self.WriteBLEDescriptor = channel.unary_unary(
                '/worker.BluetoothLEService/WriteBLEDescriptor',
                request_serializer=worker__pb2.BluetoothData.SerializeToString,
                response_deserializer=worker__pb2.StatusMessage.FromString,
                )
        self.Subscribe = channel.unary_unary(
                '/worker.BluetoothLEService/Subscribe',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.StatusMessage.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/worker.BluetoothLEService/Unsubscribe',
                request_serializer=worker__pb2.Device.SerializeToString,
                response_deserializer=worker__pb2.StatusMessage.FromString,
                )
        self.ReceiveNotifications = channel.unary_stream(
                '/worker.BluetoothLEService/ReceiveNotifications',
                request_serializer=worker__pb2.Empty.SerializeToString,
                response_deserializer=worker__pb2.BluetoothData.FromString,
                )
        self.ReceiveBroadcasted = channel.unary_stream(
                '/worker.BluetoothLEService/ReceiveBroadcasted',
                request_serializer=worker__pb2.Empty.SerializeToString,
                response_deserializer=worker__pb2.BluetoothData.FromString,
                )


class BluetoothLEServiceServicer(object):
    """Bluetooth Low Energy
    Common bluetooth commands
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

    def Connect(self, request, context):
        """Connect to a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Disconnect from a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBLEServices(self, request, context):
        """Bluetooth Low Energy

        list services for a device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBLECharactersistics(self, request, context):
        """list characterisitcs for a service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBLEDescriptors(self, request, context):
        """list descriptors for a characteristic
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadBLEDescriptor(self, request, context):
        """read a descriptor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteBLEDescriptor(self, request, context):
        """write a descriptor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """subscribe to the notification emitted by a characteristic
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """unsubscribe from a characteristic's notifications
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveNotifications(self, request, context):
        """global method to receive all the subscribed notifications
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveBroadcasted(self, request, context):
        """global method to receive all the broadcasted data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BluetoothLEServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=worker__pb2.DeviceScan.FromString,
                    response_serializer=worker__pb2.ScanResult.SerializeToString,
            ),
            'ScanBackground': grpc.unary_stream_rpc_method_handler(
                    servicer.ScanBackground,
                    request_deserializer=worker__pb2.DeviceScan.FromString,
                    response_serializer=worker__pb2.ScanResult.SerializeToString,
            ),
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.StatusMessage.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.StatusMessage.SerializeToString,
            ),
            'ListBLEServices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBLEServices,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.ListBLEServicesResult.SerializeToString,
            ),
            'ListBLECharactersistics': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBLECharactersistics,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.ListBLECharactersisticsResult.SerializeToString,
            ),
            'ListBLEDescriptors': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBLEDescriptors,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.ListBLEDescriptorsResult.SerializeToString,
            ),
            'ReadBLEDescriptor': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadBLEDescriptor,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.BluetoothData.SerializeToString,
            ),
            'WriteBLEDescriptor': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteBLEDescriptor,
                    request_deserializer=worker__pb2.BluetoothData.FromString,
                    response_serializer=worker__pb2.StatusMessage.SerializeToString,
            ),
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.StatusMessage.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=worker__pb2.Device.FromString,
                    response_serializer=worker__pb2.StatusMessage.SerializeToString,
            ),
            'ReceiveNotifications': grpc.unary_stream_rpc_method_handler(
                    servicer.ReceiveNotifications,
                    request_deserializer=worker__pb2.Empty.FromString,
                    response_serializer=worker__pb2.BluetoothData.SerializeToString,
            ),
            'ReceiveBroadcasted': grpc.unary_stream_rpc_method_handler(
                    servicer.ReceiveBroadcasted,
                    request_deserializer=worker__pb2.Empty.FromString,
                    response_serializer=worker__pb2.BluetoothData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'worker.BluetoothLEService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BluetoothLEService(object):
    """Bluetooth Low Energy
    Common bluetooth commands
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
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/Scan',
            worker__pb2.DeviceScan.SerializeToString,
            worker__pb2.ScanResult.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/worker.BluetoothLEService/ScanBackground',
            worker__pb2.DeviceScan.SerializeToString,
            worker__pb2.ScanResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/Connect',
            worker__pb2.Device.SerializeToString,
            worker__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/Disconnect',
            worker__pb2.Device.SerializeToString,
            worker__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBLEServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/ListBLEServices',
            worker__pb2.Device.SerializeToString,
            worker__pb2.ListBLEServicesResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBLECharactersistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/ListBLECharactersistics',
            worker__pb2.Device.SerializeToString,
            worker__pb2.ListBLECharactersisticsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBLEDescriptors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/ListBLEDescriptors',
            worker__pb2.Device.SerializeToString,
            worker__pb2.ListBLEDescriptorsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadBLEDescriptor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/ReadBLEDescriptor',
            worker__pb2.Device.SerializeToString,
            worker__pb2.BluetoothData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteBLEDescriptor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/WriteBLEDescriptor',
            worker__pb2.BluetoothData.SerializeToString,
            worker__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/Subscribe',
            worker__pb2.Device.SerializeToString,
            worker__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.BluetoothLEService/Unsubscribe',
            worker__pb2.Device.SerializeToString,
            worker__pb2.StatusMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveNotifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/worker.BluetoothLEService/ReceiveNotifications',
            worker__pb2.Empty.SerializeToString,
            worker__pb2.BluetoothData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveBroadcasted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/worker.BluetoothLEService/ReceiveBroadcasted',
            worker__pb2.Empty.SerializeToString,
            worker__pb2.BluetoothData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class WorkerServiceStub(object):
    """WorkerService 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WorkerInfo = channel.unary_unary(
                '/worker.WorkerService/WorkerInfo',
                request_serializer=worker__pb2.Empty.SerializeToString,
                response_deserializer=worker__pb2.WorkerConfig.FromString,
                )


class WorkerServiceServicer(object):
    """WorkerService 
    """

    def WorkerInfo(self, request, context):
        """information on the worker
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WorkerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.WorkerInfo,
                    request_deserializer=worker__pb2.Empty.FromString,
                    response_serializer=worker__pb2.WorkerConfig.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'worker.WorkerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkerService(object):
    """WorkerService 
    """

    @staticmethod
    def WorkerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.WorkerService/WorkerInfo',
            worker__pb2.Empty.SerializeToString,
            worker__pb2.WorkerConfig.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
