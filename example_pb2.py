# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\"5\n\x07Request\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x17\n\x0fmessage_content\x18\x02 \x01(\t\"!\n\x08Response\x12\x15\n\rreply_content\x18\x01 \x01(\t2/\n\tMyService\x12\"\n\x0bSendMessage\x12\x08.Request\x1a\t.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=17
  _globals['_REQUEST']._serialized_end=70
  _globals['_RESPONSE']._serialized_start=72
  _globals['_RESPONSE']._serialized_end=105
  _globals['_MYSERVICE']._serialized_start=107
  _globals['_MYSERVICE']._serialized_end=154
# @@protoc_insertion_point(module_scope)
