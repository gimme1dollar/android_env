# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: android_env/proto/snapshot_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from android_env.proto import snapshot_pb2 as android__env_dot_proto_dot_snapshot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(android_env/proto/snapshot_service.proto\x12\x19\x61ndroid.emulation.control\x1a android_env/proto/snapshot.proto\"\xd3\x01\n\x0fSnapshotPackage\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x0b\n\x03\x65rr\x18\x04 \x01(\x0c\x12\x41\n\x06\x66ormat\x18\x05 \x01(\x0e\x32\x31.android.emulation.control.SnapshotPackage.Format\x12\x0c\n\x04path\x18\x06 \x01(\t\"+\n\x06\x46ormat\x12\t\n\x05TARGZ\x10\x00\x12\x07\n\x03TAR\x10\x01\x12\r\n\tDIRECTORY\x10\x02\"\x87\x01\n\x0eSnapshotFilter\x12J\n\x0cstatusFilter\x18\x01 \x01(\x0e\x32\x34.android.emulation.control.SnapshotFilter.LoadStatus\")\n\nLoadStatus\x12\x12\n\x0e\x43ompatibleOnly\x10\x00\x12\x07\n\x03\x41ll\x10\x01\"\xe5\x01\n\x0fSnapshotDetails\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12,\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1b.emulator_snapshot.Snapshot\x12\x45\n\x06status\x18\x03 \x01(\x0e\x32\x35.android.emulation.control.SnapshotDetails.LoadStatus\x12\x0c\n\x04size\x18\x04 \x01(\x04\":\n\nLoadStatus\x12\x0e\n\nCompatible\x10\x00\x12\x10\n\x0cIncompatible\x10\x01\x12\n\n\x06Loaded\x10\x02\"M\n\x0cSnapshotList\x12=\n\tsnapshots\x18\x01 \x03(\x0b\x32*.android.emulation.control.SnapshotDetails\"\x80\x01\n\x0cIceboxTarget\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x14\n\x0cpackage_name\x18\x02 \x01(\t\x12\x13\n\x0bsnapshot_id\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61iled\x18\x04 \x01(\x08\x12\x0b\n\x03\x65rr\x18\x05 \x01(\t\x12\x1b\n\x13max_snapshot_number\x18\x06 \x01(\x05\x32\xf4\x05\n\x0fSnapshotService\x12\x65\n\rListSnapshots\x12).android.emulation.control.SnapshotFilter\x1a\'.android.emulation.control.SnapshotList\"\x00\x12j\n\x0cPullSnapshot\x12*.android.emulation.control.SnapshotPackage\x1a*.android.emulation.control.SnapshotPackage\"\x00\x30\x01\x12j\n\x0cPushSnapshot\x12*.android.emulation.control.SnapshotPackage\x1a*.android.emulation.control.SnapshotPackage\"\x00(\x01\x12h\n\x0cLoadSnapshot\x12*.android.emulation.control.SnapshotPackage\x1a*.android.emulation.control.SnapshotPackage\"\x00\x12h\n\x0cSaveSnapshot\x12*.android.emulation.control.SnapshotPackage\x1a*.android.emulation.control.SnapshotPackage\"\x00\x12j\n\x0e\x44\x65leteSnapshot\x12*.android.emulation.control.SnapshotPackage\x1a*.android.emulation.control.SnapshotPackage\"\x00\x12\x62\n\x0cTrackProcess\x12\'.android.emulation.control.IceboxTarget\x1a\'.android.emulation.control.IceboxTarget\"\x00\x42&\n\x1c\x63om.android.emulator.controlP\x01\xa2\x02\x03\x41\x45\x43\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'android_env.proto.snapshot_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.android.emulator.controlP\001\242\002\003AEC'
  _globals['_SNAPSHOTPACKAGE']._serialized_start=106
  _globals['_SNAPSHOTPACKAGE']._serialized_end=317
  _globals['_SNAPSHOTPACKAGE_FORMAT']._serialized_start=274
  _globals['_SNAPSHOTPACKAGE_FORMAT']._serialized_end=317
  _globals['_SNAPSHOTFILTER']._serialized_start=320
  _globals['_SNAPSHOTFILTER']._serialized_end=455
  _globals['_SNAPSHOTFILTER_LOADSTATUS']._serialized_start=414
  _globals['_SNAPSHOTFILTER_LOADSTATUS']._serialized_end=455
  _globals['_SNAPSHOTDETAILS']._serialized_start=458
  _globals['_SNAPSHOTDETAILS']._serialized_end=687
  _globals['_SNAPSHOTDETAILS_LOADSTATUS']._serialized_start=629
  _globals['_SNAPSHOTDETAILS_LOADSTATUS']._serialized_end=687
  _globals['_SNAPSHOTLIST']._serialized_start=689
  _globals['_SNAPSHOTLIST']._serialized_end=766
  _globals['_ICEBOXTARGET']._serialized_start=769
  _globals['_ICEBOXTARGET']._serialized_end=897
  _globals['_SNAPSHOTSERVICE']._serialized_start=900
  _globals['_SNAPSHOTSERVICE']._serialized_end=1656
# @@protoc_insertion_point(module_scope)