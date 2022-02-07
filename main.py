import grpc
from worker.worker_pb2_grpc import Worker
from worker import worker_pb2, worker_pb2_grpc
import asyncio
from bleak import BleakScanner

class Worker(worker_pb2_grpc.WorkerServicer):
    async def Scan(self, request: worker_pb2.DeviceScan, context: grpc.aio.ServicerContext) -> worker_pb2.ScanResults:
        
        if request.type == worker_pb2.DeviceType.BLE4:
            async with BleakScanner() as scanner:
                await asyncio.sleep(request.time)
            
            resp = worker_pb2.ScanResults(status=worker_pb2.Status.OK)

            for d in scanner.discovered_devices:
                print(d)
                resp.data.append(
                    worker_pb2.ScanResult(
                        device=worker_pb2.Device(
                            mac=d.address,
                            type=worker_pb2.DeviceType.BLE4,
                            ble=None
                        ),
                        name=d.name,
                        rssi=d.rssi,
                        connected=False
                    )
                )
            return resp

        else:
            return None

async def serve():
    server = grpc.aio.server()
    worker_pb2_grpc.add_WorkerServicer_to_server(Worker(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()

asyncio.run(serve())