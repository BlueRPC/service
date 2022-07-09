# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc/worker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rpc import common_pb2 as rpc_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10rpc/worker.proto\x12\x03rpc\x1a\x10rpc/common.proto\"t\n\x12WorkerInfoResponse\x12\x0e\n\x06uptime\x18\x01 \x01(\x03\x12\x13\n\x0bmax_devices\x18\x02 \x01(\x03\x12(\n\x0fsupported_types\x18\x03 \x03(\x0e\x32\x0f.rpc.DeviceType\x12\x0f\n\x07\x64\x65vices\x18\x04 \x01(\x03\x32;\n\x06Worker\x12\x31\n\nWorkerInfo\x12\n.rpc.Empty\x1a\x17.rpc.WorkerInfoResponseB[\n com.drosocode.bluerpc.rpc.workerB\x0bWorkerProtoP\x01Z(github.com/BlueRPC/server/pkg/rpc/workerb\x06proto3')



_WORKERINFORESPONSE = DESCRIPTOR.message_types_by_name['WorkerInfoResponse']
WorkerInfoResponse = _reflection.GeneratedProtocolMessageType('WorkerInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKERINFORESPONSE,
  '__module__' : 'rpc.worker_pb2'
  # @@protoc_insertion_point(class_scope:rpc.WorkerInfoResponse)
  })
_sym_db.RegisterMessage(WorkerInfoResponse)

_WORKER = DESCRIPTOR.services_by_name['Worker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.drosocode.bluerpc.rpc.workerB\013WorkerProtoP\001Z(github.com/BlueRPC/server/pkg/rpc/worker'
  _WORKERINFORESPONSE._serialized_start=43
  _WORKERINFORESPONSE._serialized_end=159
  _WORKER._serialized_start=161
  _WORKER._serialized_end=220
# @@protoc_insertion_point(module_scope)
