# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: android_env/proto/snapshot.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n android_env/proto/snapshot.proto\x12\x11\x65mulator_snapshot\"\xaf\x03\n\x05Image\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.emulator_snapshot.Image.Type\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0f\n\x07present\x18\x03 \x01(\x08\x12\x0c\n\x04size\x18\x04 \x01(\x03\x12\x19\n\x11modification_time\x18\x05 \x01(\x03\"\xb0\x02\n\x04Type\x12\x16\n\x12IMAGE_TYPE_UNKNOWN\x10\x00\x12\x15\n\x11IMAGE_TYPE_KERNEL\x10\x01\x12\x1c\n\x18IMAGE_TYPE_KERNEL_RANCHU\x10\x02\x12\x15\n\x11IMAGE_TYPE_SYSTEM\x10\x03\x12\x1a\n\x16IMAGE_TYPE_SYSTEM_COPY\x10\x04\x12\x13\n\x0fIMAGE_TYPE_DATA\x10\x05\x12\x18\n\x14IMAGE_TYPE_DATA_COPY\x10\x06\x12\x16\n\x12IMAGE_TYPE_RAMDISK\x10\x07\x12\x15\n\x11IMAGE_TYPE_SDCARD\x10\x08\x12\x14\n\x10IMAGE_TYPE_CACHE\x10\t\x12\x15\n\x11IMAGE_TYPE_VENDOR\x10\n\x12\x1d\n\x19IMAGE_TYPE_ENCRYPTION_KEY\x10\x0b\".\n\x04Host\x12\x12\n\ngpu_driver\x18\x04 \x01(\t\x12\x12\n\nhypervisor\x18\x05 \x01(\x05\"m\n\x06\x43onfig\x12\x18\n\x10\x65nabled_features\x18\x01 \x03(\x05\x12\x19\n\x11selected_renderer\x18\x02 \x01(\x05\x12\x16\n\x0e\x63pu_core_count\x18\x03 \x01(\x05\x12\x16\n\x0eram_size_bytes\x18\x04 \x01(\x03\"M\n\tSaveStats\x12\x13\n\x0bincremental\x18\x01 \x01(\r\x12\x10\n\x08\x64uration\x18\x02 \x01(\x04\x12\x19\n\x11ram_changed_bytes\x18\x03 \x01(\x04\"\x8d\x04\n\x08Snapshot\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x15\n\rcreation_time\x18\x02 \x01(\x03\x12(\n\x06images\x18\x03 \x03(\x0b\x32\x18.emulator_snapshot.Image\x12%\n\x04host\x18\x04 \x01(\x0b\x32\x17.emulator_snapshot.Host\x12)\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x19.emulator_snapshot.Config\x12\"\n\x1a\x66\x61iled_to_load_reason_code\x18\x07 \x01(\x03\x12$\n\x1cguest_data_partition_mounted\x18\x08 \x01(\x08\x12\x10\n\x08rotation\x18\t \x01(\x05\x12\x15\n\rinvalid_loads\x18\n \x01(\x05\x12\x18\n\x10successful_loads\x18\x0b \x01(\x05\x12\x14\n\x0clogical_name\x18\x0c \x01(\t\x12\x0e\n\x06parent\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t\x12\x30\n\nsave_stats\x18\x0f \x03(\x0b\x32\x1c.emulator_snapshot.SaveStats\x12\x0e\n\x06\x66olded\x18\x10 \x01(\x08\x12\x19\n\x11launch_parameters\x18\x11 \x03(\t\x12\x19\n\x11\x65mulator_build_id\x18\x12 \x01(\t\x12\x1d\n\x15system_image_build_id\x18\x13 \x01(\tB\x1f\n\x1d\x63om.android.emulator.snapshot')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'android_env.proto.snapshot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.android.emulator.snapshot'
  _globals['_IMAGE']._serialized_start=56
  _globals['_IMAGE']._serialized_end=487
  _globals['_IMAGE_TYPE']._serialized_start=183
  _globals['_IMAGE_TYPE']._serialized_end=487
  _globals['_HOST']._serialized_start=489
  _globals['_HOST']._serialized_end=535
  _globals['_CONFIG']._serialized_start=537
  _globals['_CONFIG']._serialized_end=646
  _globals['_SAVESTATS']._serialized_start=648
  _globals['_SAVESTATS']._serialized_end=725
  _globals['_SNAPSHOT']._serialized_start=728
  _globals['_SNAPSHOT']._serialized_end=1253
# @@protoc_insertion_point(module_scope)
