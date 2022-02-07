# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='worker.proto',
  package='worker',
  syntax='proto3',
  serialized_options=b'\n\034com.drosocode.bluerpc.workerB\013WorkerProtoP\001Z$github.com/BlueRPC/server/pkg/worker',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cworker.proto\x12\x06worker\";\n\x0bWriteDevice\x12\x1e\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x0e.worker.Device\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"Z\n\nReadDevice\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.worker.Status\x12\x1e\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\x0e.worker.Device\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"<\n\nDeviceScan\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.worker.DeviceType\x12\x0c\n\x04time\x18\x02 \x01(\x03\"/\n\rStatusMessage\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.worker.Status\"\x1a\n\nBLEService\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"Y\n\x15ListBLEServicesResult\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.worker.Status\x12 \n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x12.worker.BLEService\"h\n\x1dListBLECharactersisticsResult\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.worker.Status\x12\'\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x19.worker.BLECharacteristic\"_\n\x18ListBLEDescriptorsResult\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.worker.Status\x12#\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x15.worker.BLEDescriptor\"O\n\x0bScanResults\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.worker.Status\x12 \n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x12.worker.ScanResult\"[\n\nScanResult\x12\x1e\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x0e.worker.Device\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04rssi\x18\x03 \x01(\x02\x12\x11\n\tconnected\x18\x04 \x01(\x08\"\x07\n\x05\x45mpty\"Y\n\x06\x44\x65vice\x12\x0b\n\x03mac\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.worker.DeviceType\x12 \n\x03\x62le\x18\x03 \x01(\x0b\x32\x13.worker.BLESettings\"\x90\x01\n\x0b\x42LESettings\x12#\n\x07service\x18\x01 \x01(\x0b\x32\x12.worker.BLEService\x12\x31\n\x0e\x63haracteristic\x18\x02 \x01(\x0b\x32\x19.worker.BLECharacteristic\x12)\n\ndescriptor\x18\x03 \x01(\x0b\x32\x15.worker.BLEDescriptor\"|\n\x11\x42LECharacteristic\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x32\n\nproperties\x18\x02 \x03(\x0e\x32\x1e.worker.CharacteristicProperty\x12\x10\n\x08security\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scriptors\x18\x04 \x01(\x03\"\x1d\n\rBLEDescriptor\x12\x0c\n\x04uuid\x18\x01 \x01(\t*E\n\x16\x43haracteristicProperty\x12\x0c\n\x08READ_CHR\x10\x00\x12\r\n\tWRITE_CHR\x10\x01\x12\x0e\n\nNOTIFY_CHR\x10\x02*+\n\nDeviceType\x12\x08\n\x04\x42LE4\x10\x00\x12\n\n\x06\x42\x45\x41\x43ON\x10\x01\x12\x07\n\x03\x42LS\x10\x02*u\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x13\n\x0f\x45RR_UNAVAILABLE\x10\x01\x12\x19\n\x15\x45RR_CONNECTION_FAILED\x10\x02\x12\x17\n\x13\x45RR_UNKNOWN_SERVICE\x10\x03\x12\x1a\n\x16\x45RR_UNKNOWN_DESCRIPTOR\x10\x04\x32\xf0\x05\n\x06Worker\x12\x31\n\x04Scan\x12\x12.worker.DeviceScan\x1a\x13.worker.ScanResults\"\x00\x12\x32\n\x07\x43onnect\x12\x0e.worker.Device\x1a\x15.worker.StatusMessage\"\x00\x12\x35\n\nDisconnect\x12\x0e.worker.Device\x1a\x15.worker.StatusMessage\"\x00\x12\x42\n\x0fListBLEServices\x12\x0e.worker.Device\x1a\x1d.worker.ListBLEServicesResult\"\x00\x12Q\n\x16ListBLECharactersistic\x12\x0e.worker.Device\x1a%.worker.ListBLECharactersisticsResult\"\x00\x12H\n\x12ListBLEDescriptors\x12\x0e.worker.Device\x1a .worker.ListBLEDescriptorsResult\"\x00\x12\x39\n\x11ReadBLEDescriptor\x12\x0e.worker.Device\x1a\x12.worker.ReadDevice\"\x00\x12\x42\n\x12WriteBLEDescriptor\x12\x13.worker.WriteDevice\x1a\x15.worker.StatusMessage\"\x00\x12\x34\n\tSubscribe\x12\x0e.worker.Device\x1a\x15.worker.StatusMessage\"\x00\x12\x36\n\x0bUnsubscribe\x12\x0e.worker.Device\x1a\x15.worker.StatusMessage\"\x00\x12=\n\x14ReceiveNotifications\x12\r.worker.Empty\x1a\x12.worker.ReadDevice\"\x00\x30\x01\x12;\n\x12ReceiveBroadcasted\x12\r.worker.Empty\x1a\x12.worker.ReadDevice\"\x00\x30\x01\x42S\n\x1c\x63om.drosocode.bluerpc.workerB\x0bWorkerProtoP\x01Z$github.com/BlueRPC/server/pkg/workerb\x06proto3'
)

_CHARACTERISTICPROPERTY = _descriptor.EnumDescriptor(
  name='CharacteristicProperty',
  full_name='worker.CharacteristicProperty',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ_CHR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WRITE_CHR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOTIFY_CHR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1188,
  serialized_end=1257,
)
_sym_db.RegisterEnumDescriptor(_CHARACTERISTICPROPERTY)

CharacteristicProperty = enum_type_wrapper.EnumTypeWrapper(_CHARACTERISTICPROPERTY)
_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='worker.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLE4', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BEACON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1259,
  serialized_end=1302,
)
_sym_db.RegisterEnumDescriptor(_DEVICETYPE)

DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='worker.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERR_UNAVAILABLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERR_CONNECTION_FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERR_UNKNOWN_SERVICE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERR_UNKNOWN_DESCRIPTOR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1304,
  serialized_end=1421,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
READ_CHR = 0
WRITE_CHR = 1
NOTIFY_CHR = 2
BLE4 = 0
BEACON = 1
BLS = 2
OK = 0
ERR_UNAVAILABLE = 1
ERR_CONNECTION_FAILED = 2
ERR_UNKNOWN_SERVICE = 3
ERR_UNKNOWN_DESCRIPTOR = 4



_WRITEDEVICE = _descriptor.Descriptor(
  name='WriteDevice',
  full_name='worker.WriteDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='worker.WriteDevice.device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='worker.WriteDevice.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=83,
)


_READDEVICE = _descriptor.Descriptor(
  name='ReadDevice',
  full_name='worker.ReadDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='worker.ReadDevice.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='worker.ReadDevice.device', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='worker.ReadDevice.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=175,
)


_DEVICESCAN = _descriptor.Descriptor(
  name='DeviceScan',
  full_name='worker.DeviceScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='worker.DeviceScan.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='worker.DeviceScan.time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=237,
)


_STATUSMESSAGE = _descriptor.Descriptor(
  name='StatusMessage',
  full_name='worker.StatusMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='worker.StatusMessage.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=286,
)


_BLESERVICE = _descriptor.Descriptor(
  name='BLEService',
  full_name='worker.BLEService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='worker.BLEService.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=314,
)


_LISTBLESERVICESRESULT = _descriptor.Descriptor(
  name='ListBLEServicesResult',
  full_name='worker.ListBLEServicesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='worker.ListBLEServicesResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='worker.ListBLEServicesResult.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=405,
)


_LISTBLECHARACTERSISTICSRESULT = _descriptor.Descriptor(
  name='ListBLECharactersisticsResult',
  full_name='worker.ListBLECharactersisticsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='worker.ListBLECharactersisticsResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='worker.ListBLECharactersisticsResult.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=511,
)


_LISTBLEDESCRIPTORSRESULT = _descriptor.Descriptor(
  name='ListBLEDescriptorsResult',
  full_name='worker.ListBLEDescriptorsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='worker.ListBLEDescriptorsResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='worker.ListBLEDescriptorsResult.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=608,
)


_SCANRESULTS = _descriptor.Descriptor(
  name='ScanResults',
  full_name='worker.ScanResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='worker.ScanResults.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='worker.ScanResults.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=689,
)


_SCANRESULT = _descriptor.Descriptor(
  name='ScanResult',
  full_name='worker.ScanResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='worker.ScanResult.device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='worker.ScanResult.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='worker.ScanResult.rssi', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connected', full_name='worker.ScanResult.connected', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=782,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='worker.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=784,
  serialized_end=791,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='worker.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='worker.Device.mac', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='worker.Device.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ble', full_name='worker.Device.ble', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=793,
  serialized_end=882,
)


_BLESETTINGS = _descriptor.Descriptor(
  name='BLESettings',
  full_name='worker.BLESettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='worker.BLESettings.service', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='characteristic', full_name='worker.BLESettings.characteristic', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='worker.BLESettings.descriptor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=1029,
)


_BLECHARACTERISTIC = _descriptor.Descriptor(
  name='BLECharacteristic',
  full_name='worker.BLECharacteristic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='worker.BLECharacteristic.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='worker.BLECharacteristic.properties', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security', full_name='worker.BLECharacteristic.security', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descriptors', full_name='worker.BLECharacteristic.descriptors', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1031,
  serialized_end=1155,
)


_BLEDESCRIPTOR = _descriptor.Descriptor(
  name='BLEDescriptor',
  full_name='worker.BLEDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='worker.BLEDescriptor.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1157,
  serialized_end=1186,
)

_WRITEDEVICE.fields_by_name['device'].message_type = _DEVICE
_READDEVICE.fields_by_name['status'].enum_type = _STATUS
_READDEVICE.fields_by_name['device'].message_type = _DEVICE
_DEVICESCAN.fields_by_name['type'].enum_type = _DEVICETYPE
_STATUSMESSAGE.fields_by_name['status'].enum_type = _STATUS
_LISTBLESERVICESRESULT.fields_by_name['status'].enum_type = _STATUS
_LISTBLESERVICESRESULT.fields_by_name['data'].message_type = _BLESERVICE
_LISTBLECHARACTERSISTICSRESULT.fields_by_name['status'].enum_type = _STATUS
_LISTBLECHARACTERSISTICSRESULT.fields_by_name['data'].message_type = _BLECHARACTERISTIC
_LISTBLEDESCRIPTORSRESULT.fields_by_name['status'].enum_type = _STATUS
_LISTBLEDESCRIPTORSRESULT.fields_by_name['data'].message_type = _BLEDESCRIPTOR
_SCANRESULTS.fields_by_name['status'].enum_type = _STATUS
_SCANRESULTS.fields_by_name['data'].message_type = _SCANRESULT
_SCANRESULT.fields_by_name['device'].message_type = _DEVICE
_DEVICE.fields_by_name['type'].enum_type = _DEVICETYPE
_DEVICE.fields_by_name['ble'].message_type = _BLESETTINGS
_BLESETTINGS.fields_by_name['service'].message_type = _BLESERVICE
_BLESETTINGS.fields_by_name['characteristic'].message_type = _BLECHARACTERISTIC
_BLESETTINGS.fields_by_name['descriptor'].message_type = _BLEDESCRIPTOR
_BLECHARACTERISTIC.fields_by_name['properties'].enum_type = _CHARACTERISTICPROPERTY
DESCRIPTOR.message_types_by_name['WriteDevice'] = _WRITEDEVICE
DESCRIPTOR.message_types_by_name['ReadDevice'] = _READDEVICE
DESCRIPTOR.message_types_by_name['DeviceScan'] = _DEVICESCAN
DESCRIPTOR.message_types_by_name['StatusMessage'] = _STATUSMESSAGE
DESCRIPTOR.message_types_by_name['BLEService'] = _BLESERVICE
DESCRIPTOR.message_types_by_name['ListBLEServicesResult'] = _LISTBLESERVICESRESULT
DESCRIPTOR.message_types_by_name['ListBLECharactersisticsResult'] = _LISTBLECHARACTERSISTICSRESULT
DESCRIPTOR.message_types_by_name['ListBLEDescriptorsResult'] = _LISTBLEDESCRIPTORSRESULT
DESCRIPTOR.message_types_by_name['ScanResults'] = _SCANRESULTS
DESCRIPTOR.message_types_by_name['ScanResult'] = _SCANRESULT
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['BLESettings'] = _BLESETTINGS
DESCRIPTOR.message_types_by_name['BLECharacteristic'] = _BLECHARACTERISTIC
DESCRIPTOR.message_types_by_name['BLEDescriptor'] = _BLEDESCRIPTOR
DESCRIPTOR.enum_types_by_name['CharacteristicProperty'] = _CHARACTERISTICPROPERTY
DESCRIPTOR.enum_types_by_name['DeviceType'] = _DEVICETYPE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteDevice = _reflection.GeneratedProtocolMessageType('WriteDevice', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDEVICE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.WriteDevice)
  })
_sym_db.RegisterMessage(WriteDevice)

ReadDevice = _reflection.GeneratedProtocolMessageType('ReadDevice', (_message.Message,), {
  'DESCRIPTOR' : _READDEVICE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.ReadDevice)
  })
_sym_db.RegisterMessage(ReadDevice)

DeviceScan = _reflection.GeneratedProtocolMessageType('DeviceScan', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESCAN,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.DeviceScan)
  })
_sym_db.RegisterMessage(DeviceScan)

StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)

BLEService = _reflection.GeneratedProtocolMessageType('BLEService', (_message.Message,), {
  'DESCRIPTOR' : _BLESERVICE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.BLEService)
  })
_sym_db.RegisterMessage(BLEService)

ListBLEServicesResult = _reflection.GeneratedProtocolMessageType('ListBLEServicesResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTBLESERVICESRESULT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.ListBLEServicesResult)
  })
_sym_db.RegisterMessage(ListBLEServicesResult)

ListBLECharactersisticsResult = _reflection.GeneratedProtocolMessageType('ListBLECharactersisticsResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTBLECHARACTERSISTICSRESULT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.ListBLECharactersisticsResult)
  })
_sym_db.RegisterMessage(ListBLECharactersisticsResult)

ListBLEDescriptorsResult = _reflection.GeneratedProtocolMessageType('ListBLEDescriptorsResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTBLEDESCRIPTORSRESULT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.ListBLEDescriptorsResult)
  })
_sym_db.RegisterMessage(ListBLEDescriptorsResult)

ScanResults = _reflection.GeneratedProtocolMessageType('ScanResults', (_message.Message,), {
  'DESCRIPTOR' : _SCANRESULTS,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.ScanResults)
  })
_sym_db.RegisterMessage(ScanResults)

ScanResult = _reflection.GeneratedProtocolMessageType('ScanResult', (_message.Message,), {
  'DESCRIPTOR' : _SCANRESULT,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.ScanResult)
  })
_sym_db.RegisterMessage(ScanResult)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.Empty)
  })
_sym_db.RegisterMessage(Empty)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.Device)
  })
_sym_db.RegisterMessage(Device)

BLESettings = _reflection.GeneratedProtocolMessageType('BLESettings', (_message.Message,), {
  'DESCRIPTOR' : _BLESETTINGS,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.BLESettings)
  })
_sym_db.RegisterMessage(BLESettings)

BLECharacteristic = _reflection.GeneratedProtocolMessageType('BLECharacteristic', (_message.Message,), {
  'DESCRIPTOR' : _BLECHARACTERISTIC,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.BLECharacteristic)
  })
_sym_db.RegisterMessage(BLECharacteristic)

BLEDescriptor = _reflection.GeneratedProtocolMessageType('BLEDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _BLEDESCRIPTOR,
  '__module__' : 'worker_pb2'
  # @@protoc_insertion_point(class_scope:worker.BLEDescriptor)
  })
_sym_db.RegisterMessage(BLEDescriptor)


DESCRIPTOR._options = None

_WORKER = _descriptor.ServiceDescriptor(
  name='Worker',
  full_name='worker.Worker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1424,
  serialized_end=2176,
  methods=[
  _descriptor.MethodDescriptor(
    name='Scan',
    full_name='worker.Worker.Scan',
    index=0,
    containing_service=None,
    input_type=_DEVICESCAN,
    output_type=_SCANRESULTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Connect',
    full_name='worker.Worker.Connect',
    index=1,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Disconnect',
    full_name='worker.Worker.Disconnect',
    index=2,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListBLEServices',
    full_name='worker.Worker.ListBLEServices',
    index=3,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_LISTBLESERVICESRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListBLECharactersistic',
    full_name='worker.Worker.ListBLECharactersistic',
    index=4,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_LISTBLECHARACTERSISTICSRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListBLEDescriptors',
    full_name='worker.Worker.ListBLEDescriptors',
    index=5,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_LISTBLEDESCRIPTORSRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadBLEDescriptor',
    full_name='worker.Worker.ReadBLEDescriptor',
    index=6,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_READDEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WriteBLEDescriptor',
    full_name='worker.Worker.WriteBLEDescriptor',
    index=7,
    containing_service=None,
    input_type=_WRITEDEVICE,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='worker.Worker.Subscribe',
    index=8,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Unsubscribe',
    full_name='worker.Worker.Unsubscribe',
    index=9,
    containing_service=None,
    input_type=_DEVICE,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveNotifications',
    full_name='worker.Worker.ReceiveNotifications',
    index=10,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_READDEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveBroadcasted',
    full_name='worker.Worker.ReceiveBroadcasted',
    index=11,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_READDEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKER)

DESCRIPTOR.services_by_name['Worker'] = _WORKER

# @@protoc_insertion_point(module_scope)
