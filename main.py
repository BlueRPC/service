import grpc
from worker.worker_pb2_grpc import Worker
from worker import worker_pb2, worker_pb2_grpc
import asyncio
from bleak import BleakScanner
import time

START_TIME = time.time()


class Worker(worker_pb2_grpc.WorkerServicer):
    async def WorkerInfo(
        self, request: worker_pb2.Empty, context: grpc.aio.ServicerContext
    ) -> worker_pb2.WorkerConfig:
        return worker_pb2.WorkerConfig(
            uptime=round(time.time() - START_TIME),
            maxDevices=-1,
            supportedTypes=[worker_pb2.DeviceType.BLE4, worker_pb2.DeviceType.CLASSIC],
        )


class BluetoothLE(worker_pb2_grpc.BluetoothLEServicer):
    currentScanResponse = worker_pb2.ScanResult(status=worker_pb2.Status.OK)
    backgroundScan = True

    async def Scan(
        self, request: worker_pb2.DeviceScan, context: grpc.aio.ServicerContext
    ) -> worker_pb2.ScanResult:
        async with BleakScanner(
            scanning_mode=("active" if request.active else "passive")
        ) as scanner:
            await asyncio.sleep(request.time)

        resp = worker_pb2.ScanResult(status=worker_pb2.Status.OK)

        for d in scanner.discovered_devices:
            resp.data.append(
                worker_pb2.Device(
                    mac=d.address,
                    type=worker_pb2.DeviceType.BLE4,
                    name=d.name,
                    rssi=d.rssi,
                    manufacturerData=d.metadata.get("manufacturer_data"),
                    time=round(time.time()),
                )
            )
        return resp

    def detection_callback(self, d, advertisement_data):
        self.currentScanResponse.data.append(
            worker_pb2.Device(
                mac=d.address,
                type=worker_pb2.DeviceType.BLE4,
                name=d.name,
                rssi=d.rssi,
                manufacturerData=(d.metadata.get("manufacturer_data") or {}).update(
                    advertisement_data.manufacturer_data or {}
                ),
                time=round(time.time()),
            )
        )

    async def ScanBackground(self, request: worker_pb2.DeviceScan, context):
        scanner = BleakScanner()
        scanner.register_detection_callback(self.detection_callback)
        await scanner.start()
        while self.backgroundScan:
            await asyncio.sleep(request.time)
            yield self.currentScanResponse
            self.currentScanResponse = worker_pb2.ScanResult(
                status=worker_pb2.Status.OK
            )

    async def ScanBackgroundStop(self, request, context):
        self.backgroundScan = False


async def serve():
    server = grpc.aio.server()
    worker_pb2_grpc.add_WorkerServicer_to_server(Worker(), server)
    worker_pb2_grpc.add_BluetoothLEServicer_to_server(BluetoothLE(), server)
    server.add_insecure_port("[::]:50052")
    await server.start()
    await server.wait_for_termination()


asyncio.run(serve())