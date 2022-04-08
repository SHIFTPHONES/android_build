# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ota_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12ota_metadata.proto\x12\x18\x62uild.tools.releasetools\"X\n\x0ePartitionState\x12\x16\n\x0epartition_name\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x03(\t\x12\r\n\x05\x62uild\x18\x03 \x03(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\"\xce\x01\n\x0b\x44\x65viceState\x12\x0e\n\x06\x64\x65vice\x18\x01 \x03(\t\x12\r\n\x05\x62uild\x18\x02 \x03(\t\x12\x19\n\x11\x62uild_incremental\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x11\n\tsdk_level\x18\x05 \x01(\t\x12\x1c\n\x14security_patch_level\x18\x06 \x01(\t\x12\x41\n\x0fpartition_state\x18\x07 \x03(\x0b\x32(.build.tools.releasetools.PartitionState\"{\n\x08\x41pexInfo\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x15\n\ris_compressed\x18\x03 \x01(\x08\x12\x19\n\x11\x64\x65\x63ompressed_size\x18\x04 \x01(\x03\x12\x16\n\x0esource_version\x18\x05 \x01(\x03\"E\n\x0c\x41pexMetadata\x12\x35\n\tapex_info\x18\x01 \x03(\x0b\x32\".build.tools.releasetools.ApexInfo\"\xd7\x04\n\x0bOtaMetadata\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.build.tools.releasetools.OtaMetadata.OtaType\x12\x0c\n\x04wipe\x18\x02 \x01(\x08\x12\x11\n\tdowngrade\x18\x03 \x01(\x08\x12P\n\x0eproperty_files\x18\x04 \x03(\x0b\x32\x38.build.tools.releasetools.OtaMetadata.PropertyFilesEntry\x12;\n\x0cprecondition\x18\x05 \x01(\x0b\x32%.build.tools.releasetools.DeviceState\x12<\n\rpostcondition\x18\x06 \x01(\x0b\x32%.build.tools.releasetools.DeviceState\x12#\n\x1bretrofit_dynamic_partitions\x18\x07 \x01(\x08\x12\x16\n\x0erequired_cache\x18\x08 \x01(\x03\x12\x15\n\rspl_downgrade\x18\t \x01(\x08\x12\x1d\n\x15shift_device_codename\x18\n \x01(\t\x12\x1c\n\x14shift_pre_build_type\x18\x0b \x01(\t\x12 \n\x18shift_post_build_version\x18\x0c \x01(\t\x1a\x34\n\x12PropertyFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x07OtaType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02\x41\x42\x10\x01\x12\t\n\x05\x42LOCK\x10\x02\x12\t\n\x05\x42RICK\x10\x03\x42#\n\x0b\x61ndroid.otaB\x12OtaPackageMetadataH\x03\x62\x06proto3')



_PARTITIONSTATE = DESCRIPTOR.message_types_by_name['PartitionState']
_DEVICESTATE = DESCRIPTOR.message_types_by_name['DeviceState']
_APEXINFO = DESCRIPTOR.message_types_by_name['ApexInfo']
_APEXMETADATA = DESCRIPTOR.message_types_by_name['ApexMetadata']
_OTAMETADATA = DESCRIPTOR.message_types_by_name['OtaMetadata']
_OTAMETADATA_PROPERTYFILESENTRY = _OTAMETADATA.nested_types_by_name['PropertyFilesEntry']
_OTAMETADATA_OTATYPE = _OTAMETADATA.enum_types_by_name['OtaType']
PartitionState = _reflection.GeneratedProtocolMessageType('PartitionState', (_message.Message,), {
  'DESCRIPTOR' : _PARTITIONSTATE,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.PartitionState)
  })
_sym_db.RegisterMessage(PartitionState)

DeviceState = _reflection.GeneratedProtocolMessageType('DeviceState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESTATE,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.DeviceState)
  })
_sym_db.RegisterMessage(DeviceState)

ApexInfo = _reflection.GeneratedProtocolMessageType('ApexInfo', (_message.Message,), {
  'DESCRIPTOR' : _APEXINFO,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.ApexInfo)
  })
_sym_db.RegisterMessage(ApexInfo)

ApexMetadata = _reflection.GeneratedProtocolMessageType('ApexMetadata', (_message.Message,), {
  'DESCRIPTOR' : _APEXMETADATA,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.ApexMetadata)
  })
_sym_db.RegisterMessage(ApexMetadata)

OtaMetadata = _reflection.GeneratedProtocolMessageType('OtaMetadata', (_message.Message,), {

  'PropertyFilesEntry' : _reflection.GeneratedProtocolMessageType('PropertyFilesEntry', (_message.Message,), {
    'DESCRIPTOR' : _OTAMETADATA_PROPERTYFILESENTRY,
    '__module__' : 'ota_metadata_pb2'
    # @@protoc_insertion_point(class_scope:build.tools.releasetools.OtaMetadata.PropertyFilesEntry)
    })
  ,
  'DESCRIPTOR' : _OTAMETADATA,
  '__module__' : 'ota_metadata_pb2'
  # @@protoc_insertion_point(class_scope:build.tools.releasetools.OtaMetadata)
  })
_sym_db.RegisterMessage(OtaMetadata)
_sym_db.RegisterMessage(OtaMetadata.PropertyFilesEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\013android.otaB\022OtaPackageMetadataH\003'
  _OTAMETADATA_PROPERTYFILESENTRY._options = None
  _OTAMETADATA_PROPERTYFILESENTRY._serialized_options = b'8\001'
  _PARTITIONSTATE._serialized_start=48
  _PARTITIONSTATE._serialized_end=136
  _DEVICESTATE._serialized_start=139
  _DEVICESTATE._serialized_end=345
  _APEXINFO._serialized_start=347
  _APEXINFO._serialized_end=470
  _APEXMETADATA._serialized_start=472
  _APEXMETADATA._serialized_end=541
  _OTAMETADATA._serialized_start=544
  _OTAMETADATA._serialized_end=1143
  _OTAMETADATA_PROPERTYFILESENTRY._serialized_start=1037
  _OTAMETADATA_PROPERTYFILESENTRY._serialized_end=1089
  _OTAMETADATA_OTATYPE._serialized_start=1091
  _OTAMETADATA_OTATYPE._serialized_end=1143
# @@protoc_insertion_point(module_scope)
