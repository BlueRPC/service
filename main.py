import grpc
from rpc import (
    worker_pb2,
    worker_pb2_grpc,
    ble_pb2,
    ble_pb2_grpc,
    btc_pb2,
    btc_pb2_grpc,
    common_pb2,
)
import asyncio
from bleak import BleakScanner, BleakClient
import time
import re
from enum import Enum
from functools import partial

START_TIME = time.time()


def validateMAC(addr: str):
    return bool(
        re.match("^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$", addr)
    )


def validateUUID(u: str):
    return bool(
        re.match(
            "[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}",
            u,
        )
    )


class VFlags(Enum):
    MAC = 1
    CONN = 2
    SERVICE = 3
    CHARACTERISTIC = 4
    DESCRIPTOR = 5
    NO_CONN = 6


class Worker(worker_pb2_grpc.WorkerServicer):
    async def WorkerInfo(
        self, request: common_pb2.Empty, context: grpc.aio.ServicerContext
    ) -> worker_pb2.WorkerInfoResponse:
        return worker_pb2.WorkerInfoResponse(
            uptime=round(time.time() - START_TIME),
            max_devices=-1,
            supported_types=[
                common_pb2.DeviceType.DEVICE_TYPE_BLE4,
                common_pb2.DeviceType.DEVICE_TYPE_CLASSIC,
            ],
        )


class BluetoothLE(ble_pb2_grpc.BluetoothLEServicer):
    currentScanResponse = common_pb2.ScanResult(status=common_pb2.Status.STATUS_OK)
    disconnectEvents = []
    notifications = []
    backgroundScan = True
    connections = {}

    def validate_device(self, request, flags):
        ble = False
        try:
            ble = True
            dev = request.device
        except:
            dev = request

        if VFlags.MAC in flags and not validateMAC(dev.mac):
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_INVALID_CONNECTION_SETTINGS,
                message="invalid mac addr",
            )

        if VFlags.CONN in flags and dev.mac not in self.connections:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_INVALID_CONNECTION_SETTINGS,
                message="device not connected",
            )

        if VFlags.NO_CONN in flags and dev.mac in self.connections:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_INVALID_CONNECTION_SETTINGS,
                message="device already connected",
            )

        if ble and VFlags.SERVICE in flags and not validateUUID(request.service.uuid):
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_INVALID_CONNECTION_SETTINGS,
                message="invalid service UUID",
            )

        if (
            ble
            and VFlags.CHARACTERISTIC in flags
            and not validateUUID(request.characteristic.uuid)
        ):
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_INVALID_CONNECTION_SETTINGS,
                message="invalid characteristic UUID",
            )

        if (
            ble
            and VFlags.DESCRIPTOR in flags
            and not validateUUID(request.descriptor.uuid)
        ):
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_INVALID_CONNECTION_SETTINGS,
                message="invalid descriptor UUID",
            )

        return None

    # region BLE Scan
    async def Scan(
        self, request: common_pb2.DeviceScan, context: grpc.aio.ServicerContext
    ) -> common_pb2.ScanResult:
        async with BleakScanner(
            scanning_mode=("active" if request.active else "passive")
        ) as scanner:
            await asyncio.sleep(request.time)

        resp = common_pb2.ScanResult(status=common_pb2.Status.STATUS_OK)

        for d in scanner.discovered_devices:
            resp.data.append(
                common_pb2.ScanData(
                    device=common_pb2.Device(
                        mac=d.address,
                        type=common_pb2.DeviceType.DEVICE_TYPE_BLE4,
                        name=d.name,
                    ),
                    rssi=d.rssi,
                    manufacturerData=d.metadata.get("manufacturer_data"),
                    time=round(time.time()),
                )
            )
        return resp

    def detection_callback(self, d, advertisement_data):
        self.currentScanResponse.data.append(
            common_pb2.ScanData(
                device=common_pb2.Device(
                    mac=d.address,
                    type=common_pb2.DeviceType.DEVICE_TYPE_BLE4,
                    name=d.name,
                ),
                rssi=d.rssi,
                manufacturer_data=(d.metadata.get("manufacturer_data") or {}).update(
                    advertisement_data.manufacturer_data or {}
                ),
                time=round(time.time()),
            )
        )

    async def ScanBackground(self, request: common_pb2.DeviceScan, context):
        scanner = BleakScanner()
        scanner.register_detection_callback(self.detection_callback)
        await scanner.start()
        while self.backgroundScan:
            await asyncio.sleep(request.time)
            yield self.currentScanResponse
            self.currentScanResponse = common_pb2.ScanResult(
                status=common_pb2.Status.STATUS_OK
            )

    async def ScanBackgroundStop(self, request, context):
        self.backgroundScan = False
        return common_pb2.StatusMessage(status=common_pb2.Status.STATUS_OK)

    # endregion

    # region BLE Connection

    async def Connect(self, request, context):
        v = self.validate_device(request, [VFlags.MAC, VFlags.NO_CONN])
        if v is not None:
            return v

        client = BleakClient(request.mac)
        try:
            await client.connect()
            client.set_disconnected_callback(self.disconnect_callback)
            self.connections[request.mac] = client
        except Exception as e:
            await client.disconnect()
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_CONNECTION_FAILED, message=str(e)
            )
        return common_pb2.StatusMessage(status=common_pb2.Status.STATUS_OK)

    async def Disconnect(self, request, context):
        v = self.validate_device(request, [VFlags.MAC, VFlags.CONN])
        if v is not None:
            return v
        await self.connections[request.mac].disconnect()
        # removal from array will be handled by disconnect_callback
        return common_pb2.StatusMessage(
            status=common_pb2.Status.STATUS_OK, message="ok"
        )

    def disconnect_callback(self, client):
        if client.address in self.connections:
            del self.connections[client.address]
            self.disconnectEvents.append(
                common_pb2.Device(
                    mac=client.address
                )
            )

    async def ReceiveDisconnect(self, request, context) -> common_pb2.Device:
        while self.disconnectEvents:
            await asyncio.sleep(0.5)
            try:
                yield self.disconnectEvents.pop()
            except:
                pass

    # endregion

    # region BLE Listings
    async def ListBLEServices(self, request, context):
        v = self.validate_device(request, [VFlags.CONN, VFlags.MAC])
        if v is not None:
            return v
        try:
            s = await self.connections[request.device.mac].get_services()
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        ret = ble_pb2.ListBLEServicesResult(
            status=common_pb2.Status.STATUS_OK, device=request.device
        )
        for i in s.services.values():
            ret.data.append(
                ble_pb2.BLEService(
                    uuid=i.uuid, handle=i.handle, description=i.description
                )
            )
        return ret

    async def ListBLECharactersistics(self, request, context):
        v = self.validate_device(request, [VFlags.CONN, VFlags.MAC, VFlags.SERVICE])
        if v is not None:
            return v

        try:
            s = (await self.connections[request.device.mac].get_services()).get_service(
                request.service.uuid
            )
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        ret = ble_pb2.ListBLECharactersisticsResult(
            status=common_pb2.Status.STATUS_OK, device=request.device
        )
        for i in s.characteristics:
            props = []
            for j in i.properties:
                if j == "read":
                    props.append(ble_pb2.ChrProperty.CHR_PROPERTY_READ)
                elif j == "write":
                    props.append(ble_pb2.ChrProperty.CHR_PROPERTY_WRITE)
                elif j == "notify":
                    props.append(ble_pb2.ChrProperty.CHR_PROPERTY_NOTIFY)
            ret.data.append(
                ble_pb2.BLECharacteristic(
                    uuid=i.uuid,
                    descriptors=len(i.descriptors),
                    properties=props,
                    description=i.description,
                    handle=i.handle,
                )
            )
        return ret

    async def ListBLEDescriptors(self, request, context):
        v = self.validate_device(
            request, [VFlags.CONN, VFlags.MAC, VFlags.SERVICE, VFlags.CHARACTERISTIC]
        )
        if v is not None:
            return v
        try:
            s = (
                await self.connections[request.device.mac].get_services()
            ).get_characteristic(request.characteristic.uuid)
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        ret = ble_pb2.ListBLEDescriptorsResult(
            status=common_pb2.Status.STATUS_OK, device=request.device
        )
        for i in s.descriptors:
            ret.data.append(
                ble_pb2.BLEDescriptor(
                    uuid=i.uuid, handle=i.handle, description=i.description
                )
            )
        return ret

    # endregion

    # region BLE Read/Write

    async def ReadBLECharactersistic(
        self, request: ble_pb2.BLEDevice, context
    ) -> ble_pb2.BLEData:
        v = self.validate_device(
            request, [VFlags.CONN, VFlags.MAC, VFlags.CHARACTERISTIC]
        )
        if v is not None:
            return v

        try:
            ret = await self.connections[request.device.mac].read_gatt_char(
                request.characteristic.uuid
            )
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        return ble_pb2.BLEData(device=request, data=bytes(ret))

    async def WriteBLECharactersistic(
        self, request: ble_pb2.BLEData, context
    ) -> common_pb2.StatusMessage:
        v = self.validate_device(
            request, [VFlags.CONN, VFlags.MAC, VFlags.CHARACTERISTIC]
        )
        if v is not None:
            return v

        try:
            await self.connections[request.device.mac].write_gatt_char(
                request.device.characteristic.uuid, request.data
            )
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        return common_pb2.StatusMessage(
            status=common_pb2.Status.STATUS_OK, message="ok"
        )

    async def ReadBLEDescriptor(
        self, request: ble_pb2.BLEDevice, context
    ) -> ble_pb2.BLEData:
        v = self.validate_device(request, [VFlags.CONN, VFlags.MAC, VFlags.DESCRIPTOR])
        if v is not None:
            return v

        try:
            ret = await self.connections[request.device.mac].read_gatt_descriptor(
                request.descriptor.uuid
            )
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        return ble_pb2.BLEData(device=request, data=bytes(ret))

    async def WriteBLEDescriptor(
        self, request: ble_pb2.BLEData, context
    ) -> common_pb2.StatusMessage:
        v = self.validate_device(
            request, [VFlags.CONN, VFlags.MAC, VFlags.CHARACTERISTIC]
        )
        if v is not None:
            return v

        try:
            await self.connections[request.device.mac].write_gatt_descriptor(
                request.device.descriptor.uuid, request.data
            )
        except Exception as e:
            return common_pb2.StatusMessage(
                status=common_pb2.Status.STATUS_UNK, message=str(e)
            )

        return common_pb2.StatusMessage(
            status=common_pb2.Status.STATUS_OK, message="ok"
        )

    # endregion

    # region BLE Notifications

    async def Subscribe(
        self, request: ble_pb2.BLEDevice, context
    ) -> common_pb2.StatusMessage:
        v = self.validate_device(
            request, [VFlags.CONN, VFlags.MAC, VFlags.CHARACTERISTIC]
        )
        if v is not None:
            return v

        self.connections[request.device.mac].start_notify(
            request.characteristic.uuid, partial(self.notification_callback, request)
        )

        self.notificationSubscriptions[request.device.mac].append(
            request.characteristic.uuid
        )

        return common_pb2.StatusMessage(
            status=common_pb2.Status.STATUS_OK, message="ok"
        )

    def notification_callback(self, device: ble_pb2.BLEDevice, sender: int, data: bytearray):
        device.characteristic.handle = sender
        self.notifications.append(
            ble_pb2.BLEData(
                device=device,
                data=data,
            )
        )

    async def Unsubscribe(
        self, request: ble_pb2.BLEDevice, context
    ) -> common_pb2.StatusMessage:
        v = self.validate_device(
            request, [VFlags.CONN, VFlags.MAC, VFlags.CHARACTERISTIC]
        )
        if v is not None:
            return v
        self.connections[request.device.mac].stop_notify(request.characteristic.uuid)
        return common_pb2.StatusMessage(
            status=common_pb2.Status.STATUS_OK, message="ok"
        )

    async def ReceiveNotifications(self, request, context) -> ble_pb2.BLEData:
        while self.notifications:
            await asyncio.sleep(0.5)
            try:
                yield self.notifications.pop()
            except:
                pass

    # endregion


async def serve():
    server = grpc.aio.server()
    worker_pb2_grpc.add_WorkerServicer_to_server(Worker(), server)
    ble_pb2_grpc.add_BluetoothLEServicer_to_server(BluetoothLE(), server)
    server.add_insecure_port("[::]:50052")
    await server.start()
    await server.wait_for_termination()


asyncio.run(serve())
