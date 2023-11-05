# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/proto/hashmap.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from generated import general_pb2 as src_dot_proto_dot_general__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17src/proto/hashmap.proto\x12\x07hashmap\x1a\x17src/proto/general.proto\"A\n\x0fGetItemsPayload\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04part\x18\x02 \x01(\x05\x12\x0f\n\x07keyword\x18\x03 \x01(\t\"0\n\x10GetItemsResponse\x12\x1c\n\x05items\x18\x01 \x03(\x0b\x32\r.hashmap.Item\"-\n\x0fGetTagsResponse\x12\x1a\n\x04tags\x18\x01 \x03(\x0b\x32\x0c.hashmap.Tag\"]\n\x11\x43reateItemPayload\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\r\n\x05\x65xtra\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x03(\t\" \n\x12\x43reateItemResponse\x12\n\n\x02id\x18\x01 \x01(\r\"5\n\x11RemoveItemPayload\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07item_id\x18\x02 \x01(\r\"l\n\x0f\x45\x64itItemPayload\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07item_id\x18\x02 \x01(\r\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\x12\r\n\x05\x65xtra\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\"Y\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\r\n\x05\x65xtra\x18\x04 \x01(\t\x12\x1a\n\x04tags\x18\x05 \x03(\x0b\x32\x0c.hashmap.Tag\"#\n\x03Tag\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06usages\x18\x02 \x01(\r2\xc2\x02\n\nHashmapRPC\x12?\n\x08GetItems\x12\x18.hashmap.GetItemsPayload\x1a\x19.hashmap.GetItemsResponse\x12\x34\n\x07GetTags\x12\x0f.general.UserId\x1a\x18.hashmap.GetTagsResponse\x12\x45\n\nCreateItem\x12\x1a.hashmap.CreateItemPayload\x1a\x1b.hashmap.CreateItemResponse\x12<\n\nRemoveItem\x12\x1a.hashmap.RemoveItemPayload\x1a\x12.general.IsSuccess\x12\x38\n\x08\x45\x64itItem\x12\x18.hashmap.EditItemPayload\x1a\x12.general.IsSuccessB6Z4github.com/dehwyy/makoto/libs/grpc/generated/hashmapb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.proto.hashmap_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/dehwyy/makoto/libs/grpc/generated/hashmap'
  _globals['_GETITEMSPAYLOAD']._serialized_start=61
  _globals['_GETITEMSPAYLOAD']._serialized_end=126
  _globals['_GETITEMSRESPONSE']._serialized_start=128
  _globals['_GETITEMSRESPONSE']._serialized_end=176
  _globals['_GETTAGSRESPONSE']._serialized_start=178
  _globals['_GETTAGSRESPONSE']._serialized_end=223
  _globals['_CREATEITEMPAYLOAD']._serialized_start=225
  _globals['_CREATEITEMPAYLOAD']._serialized_end=318
  _globals['_CREATEITEMRESPONSE']._serialized_start=320
  _globals['_CREATEITEMRESPONSE']._serialized_end=352
  _globals['_REMOVEITEMPAYLOAD']._serialized_start=354
  _globals['_REMOVEITEMPAYLOAD']._serialized_end=407
  _globals['_EDITITEMPAYLOAD']._serialized_start=409
  _globals['_EDITITEMPAYLOAD']._serialized_end=517
  _globals['_ITEM']._serialized_start=519
  _globals['_ITEM']._serialized_end=608
  _globals['_TAG']._serialized_start=610
  _globals['_TAG']._serialized_end=645
  _globals['_HASHMAPRPC']._serialized_start=648
  _globals['_HASHMAPRPC']._serialized_end=970
# @@protoc_insertion_point(module_scope)
