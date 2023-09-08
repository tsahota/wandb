# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wandb/proto/wandb_server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wandb.proto import wandb_base_pb2 as wandb_dot_proto_dot_wandb__base__pb2
from wandb.proto import wandb_internal_pb2 as wandb_dot_proto_dot_wandb__internal__pb2
from wandb.proto import wandb_settings_pb2 as wandb_dot_proto_dot_wandb__settings__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ewandb/proto/wandb_server.proto\x12\x0ewandb_internal\x1a\x1cwandb/proto/wandb_base.proto\x1a wandb/proto/wandb_internal.proto\x1a wandb/proto/wandb_settings.proto\"D\n\x15ServerShutdownRequest\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x18\n\x16ServerShutdownResponse\"B\n\x13ServerStatusRequest\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x16\n\x14ServerStatusResponse\"r\n\x17ServerInformInitRequest\x12*\n\x08settings\x18\x01 \x01(\x0b\x32\x18.wandb_internal.Settings\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x1a\n\x18ServerInformInitResponse\"s\n\x18ServerInformStartRequest\x12*\n\x08settings\x18\x01 \x01(\x0b\x32\x18.wandb_internal.Settings\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x1b\n\x19ServerInformStartResponse\"H\n\x19ServerInformFinishRequest\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x1c\n\x1aServerInformFinishResponse\"H\n\x19ServerInformAttachRequest\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"u\n\x1aServerInformAttachResponse\x12*\n\x08settings\x18\x01 \x01(\x0b\x32\x18.wandb_internal.Settings\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"H\n\x19ServerInformDetachRequest\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x1c\n\x1aServerInformDetachResponse\"]\n\x1bServerInformTeardownRequest\x12\x11\n\texit_code\x18\x01 \x01(\x05\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\x1e\n\x1cServerInformTeardownResponse\"w\n\x1eServerInformConsoleDataRequest\x12\x13\n\x0boutput_type\x18\x01 \x01(\t\x12\x13\n\x0boutput_data\x18\x02 \x01(\t\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"!\n\x1fServerInformConsoleDataResponse\"^\n\x1fServerInformConsoleStartRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"\"\n ServerInformConsoleStartResponse\"]\n\x1eServerInformConsoleStopRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12+\n\x05_info\x18\xc8\x01 \x01(\x0b\x32\x1b.wandb_internal._RecordInfo\"!\n\x1fServerInformConsoleStopResponse\"\x93\x06\n\rServerRequest\x12\x30\n\x0erecord_publish\x18\x01 \x01(\x0b\x32\x16.wandb_internal.RecordH\x00\x12\x34\n\x12record_communicate\x18\x02 \x01(\x0b\x32\x16.wandb_internal.RecordH\x00\x12>\n\x0binform_init\x18\x03 \x01(\x0b\x32\'.wandb_internal.ServerInformInitRequestH\x00\x12\x42\n\rinform_finish\x18\x04 \x01(\x0b\x32).wandb_internal.ServerInformFinishRequestH\x00\x12\x42\n\rinform_attach\x18\x05 \x01(\x0b\x32).wandb_internal.ServerInformAttachRequestH\x00\x12\x42\n\rinform_detach\x18\x06 \x01(\x0b\x32).wandb_internal.ServerInformDetachRequestH\x00\x12\x46\n\x0finform_teardown\x18\x07 \x01(\x0b\x32+.wandb_internal.ServerInformTeardownRequestH\x00\x12@\n\x0cinform_start\x18\x08 \x01(\x0b\x32(.wandb_internal.ServerInformStartRequestH\x00\x12M\n\x13inform_console_data\x18\t \x01(\x0b\x32..wandb_internal.ServerInformConsoleDataRequestH\x00\x12O\n\x14inform_console_start\x18\n \x01(\x0b\x32/.wandb_internal.ServerInformConsoleStartRequestH\x00\x12M\n\x13inform_console_stop\x18\x0b \x01(\x0b\x32..wandb_internal.ServerInformConsoleStopRequestH\x00\x42\x15\n\x13server_request_type\"\xbd\x06\n\x0eServerResponse\x12\x34\n\x12result_communicate\x18\x02 \x01(\x0b\x32\x16.wandb_internal.ResultH\x00\x12H\n\x14inform_init_response\x18\x03 \x01(\x0b\x32(.wandb_internal.ServerInformInitResponseH\x00\x12L\n\x16inform_finish_response\x18\x04 \x01(\x0b\x32*.wandb_internal.ServerInformFinishResponseH\x00\x12L\n\x16inform_attach_response\x18\x05 \x01(\x0b\x32*.wandb_internal.ServerInformAttachResponseH\x00\x12L\n\x16inform_detach_response\x18\x06 \x01(\x0b\x32*.wandb_internal.ServerInformDetachResponseH\x00\x12P\n\x18inform_teardown_response\x18\x07 \x01(\x0b\x32,.wandb_internal.ServerInformTeardownResponseH\x00\x12J\n\x15inform_start_response\x18\x08 \x01(\x0b\x32).wandb_internal.ServerInformStartResponseH\x00\x12W\n\x1cinform_console_data_response\x18\t \x01(\x0b\x32/.wandb_internal.ServerInformConsoleDataResponseH\x00\x12Y\n\x1dinform_console_start_response\x18\n \x01(\x0b\x32\x30.wandb_internal.ServerInformConsoleStartResponseH\x00\x12W\n\x1cinform_console_stop_response\x18\x0b \x01(\x0b\x32/.wandb_internal.ServerInformConsoleStopResponseH\x00\x42\x16\n\x14server_response_typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wandb.proto.wandb_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVERSHUTDOWNREQUEST._serialized_start=148
  _SERVERSHUTDOWNREQUEST._serialized_end=216
  _SERVERSHUTDOWNRESPONSE._serialized_start=218
  _SERVERSHUTDOWNRESPONSE._serialized_end=242
  _SERVERSTATUSREQUEST._serialized_start=244
  _SERVERSTATUSREQUEST._serialized_end=310
  _SERVERSTATUSRESPONSE._serialized_start=312
  _SERVERSTATUSRESPONSE._serialized_end=334
  _SERVERINFORMINITREQUEST._serialized_start=336
  _SERVERINFORMINITREQUEST._serialized_end=450
  _SERVERINFORMINITRESPONSE._serialized_start=452
  _SERVERINFORMINITRESPONSE._serialized_end=478
  _SERVERINFORMSTARTREQUEST._serialized_start=480
  _SERVERINFORMSTARTREQUEST._serialized_end=595
  _SERVERINFORMSTARTRESPONSE._serialized_start=597
  _SERVERINFORMSTARTRESPONSE._serialized_end=624
  _SERVERINFORMFINISHREQUEST._serialized_start=626
  _SERVERINFORMFINISHREQUEST._serialized_end=698
  _SERVERINFORMFINISHRESPONSE._serialized_start=700
  _SERVERINFORMFINISHRESPONSE._serialized_end=728
  _SERVERINFORMATTACHREQUEST._serialized_start=730
  _SERVERINFORMATTACHREQUEST._serialized_end=802
  _SERVERINFORMATTACHRESPONSE._serialized_start=804
  _SERVERINFORMATTACHRESPONSE._serialized_end=921
  _SERVERINFORMDETACHREQUEST._serialized_start=923
  _SERVERINFORMDETACHREQUEST._serialized_end=995
  _SERVERINFORMDETACHRESPONSE._serialized_start=997
  _SERVERINFORMDETACHRESPONSE._serialized_end=1025
  _SERVERINFORMTEARDOWNREQUEST._serialized_start=1027
  _SERVERINFORMTEARDOWNREQUEST._serialized_end=1120
  _SERVERINFORMTEARDOWNRESPONSE._serialized_start=1122
  _SERVERINFORMTEARDOWNRESPONSE._serialized_end=1152
  _SERVERINFORMCONSOLEDATAREQUEST._serialized_start=1154
  _SERVERINFORMCONSOLEDATAREQUEST._serialized_end=1273
  _SERVERINFORMCONSOLEDATARESPONSE._serialized_start=1275
  _SERVERINFORMCONSOLEDATARESPONSE._serialized_end=1308
  _SERVERINFORMCONSOLESTARTREQUEST._serialized_start=1310
  _SERVERINFORMCONSOLESTARTREQUEST._serialized_end=1404
  _SERVERINFORMCONSOLESTARTRESPONSE._serialized_start=1406
  _SERVERINFORMCONSOLESTARTRESPONSE._serialized_end=1440
  _SERVERINFORMCONSOLESTOPREQUEST._serialized_start=1442
  _SERVERINFORMCONSOLESTOPREQUEST._serialized_end=1535
  _SERVERINFORMCONSOLESTOPRESPONSE._serialized_start=1537
  _SERVERINFORMCONSOLESTOPRESPONSE._serialized_end=1570
  _SERVERREQUEST._serialized_start=1573
  _SERVERREQUEST._serialized_end=2360
  _SERVERRESPONSE._serialized_start=2363
  _SERVERRESPONSE._serialized_end=3192
# @@protoc_insertion_point(module_scope)
