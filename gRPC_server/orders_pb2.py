# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: orders.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'orders.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0corders.proto\x12\x06orders\"!\n\x0eMessageRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x0fMessageResponse\x12\x10\n\x08response\x18\x01 \x01(\t2N\n\x0cOrderService\x12>\n\x0bSendMessage\x12\x16.orders.MessageRequest\x1a\x17.orders.MessageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=24
  _globals['_MESSAGEREQUEST']._serialized_end=57
  _globals['_MESSAGERESPONSE']._serialized_start=59
  _globals['_MESSAGERESPONSE']._serialized_end=94
  _globals['_ORDERSERVICE']._serialized_start=96
  _globals['_ORDERSERVICE']._serialized_end=174
# @@protoc_insertion_point(module_scope)
