# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GC_LS.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GC_LS.proto',
  package='GC_LS',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0bGC_LS.proto\x12\x05GC_LS\"i\n\x08\x41skLogin\x12+\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.GC_LS.MsgID:\x0eGC2LS_AskLogin\x12\x10\n\x08platform\x18\x02 \x01(\r\x12\x0c\n\x04mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"]\n\nServerInfo\x12\x12\n\nServerName\x18\x01 \x01(\t\x12\x12\n\nServerAddr\x18\x02 \x01(\t\x12\x12\n\nServerPort\x18\x03 \x01(\x05\x12\x13\n\x0bServerState\x18\x04 \x01(\x05\"l\n\x0cServerBSAddr\x12\x35\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.GC_LS.MsgID:\x18LS2GC_NotifyServerBSAddr\x12%\n\nserverinfo\x18\x02 \x03(\x0b\x32\x11.GC_LS.ServerInfo\"E\n\x08\x45rrorMsg\x12(\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.GC_LS.MsgID:\x0bLS2GC_Error\x12\x0f\n\x07\x65rrorid\x18\x02 \x01(\x05*g\n\x05MsgID\x12\x12\n\x0eGC2LS_AskLogin\x10\x64\x12\x1b\n\x17LS2GC_NotifyLoginResult\x10\x65\x12\x1c\n\x18LS2GC_NotifyServerBSAddr\x10\x66\x12\x0f\n\x0bLS2GC_Error\x10g')
)

_MSGID = _descriptor.EnumDescriptor(
  name='MsgID',
  full_name='GC_LS.MsgID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GC2LS_AskLogin', index=0, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LS2GC_NotifyLoginResult', index=1, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LS2GC_NotifyServerBSAddr', index=2, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LS2GC_Error', index=3, number=103,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=405,
  serialized_end=508,
)
_sym_db.RegisterEnumDescriptor(_MSGID)

MsgID = enum_type_wrapper.EnumTypeWrapper(_MSGID)
GC2LS_AskLogin = 100
LS2GC_NotifyLoginResult = 101
LS2GC_NotifyServerBSAddr = 102
LS2GC_Error = 103



_ASKLOGIN = _descriptor.Descriptor(
  name='AskLogin',
  full_name='GC_LS.AskLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='GC_LS.AskLogin.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='GC_LS.AskLogin.platform', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='GC_LS.AskLogin.mail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='GC_LS.AskLogin.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=127,
)


_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='GC_LS.ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ServerName', full_name='GC_LS.ServerInfo.ServerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ServerAddr', full_name='GC_LS.ServerInfo.ServerAddr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ServerPort', full_name='GC_LS.ServerInfo.ServerPort', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ServerState', full_name='GC_LS.ServerInfo.ServerState', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=222,
)


_SERVERBSADDR = _descriptor.Descriptor(
  name='ServerBSAddr',
  full_name='GC_LS.ServerBSAddr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='GC_LS.ServerBSAddr.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=102,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serverinfo', full_name='GC_LS.ServerBSAddr.serverinfo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=332,
)


_ERRORMSG = _descriptor.Descriptor(
  name='ErrorMsg',
  full_name='GC_LS.ErrorMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='GC_LS.ErrorMsg.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=103,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorid', full_name='GC_LS.ErrorMsg.errorid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=403,
)

_ASKLOGIN.fields_by_name['msgid'].enum_type = _MSGID
_SERVERBSADDR.fields_by_name['msgid'].enum_type = _MSGID
_SERVERBSADDR.fields_by_name['serverinfo'].message_type = _SERVERINFO
_ERRORMSG.fields_by_name['msgid'].enum_type = _MSGID
DESCRIPTOR.message_types_by_name['AskLogin'] = _ASKLOGIN
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['ServerBSAddr'] = _SERVERBSADDR
DESCRIPTOR.message_types_by_name['ErrorMsg'] = _ERRORMSG
DESCRIPTOR.enum_types_by_name['MsgID'] = _MSGID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AskLogin = _reflection.GeneratedProtocolMessageType('AskLogin', (_message.Message,), dict(
  DESCRIPTOR = _ASKLOGIN,
  __module__ = 'GC_LS_pb2'
  # @@protoc_insertion_point(class_scope:GC_LS.AskLogin)
  ))
_sym_db.RegisterMessage(AskLogin)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO,
  __module__ = 'GC_LS_pb2'
  # @@protoc_insertion_point(class_scope:GC_LS.ServerInfo)
  ))
_sym_db.RegisterMessage(ServerInfo)

ServerBSAddr = _reflection.GeneratedProtocolMessageType('ServerBSAddr', (_message.Message,), dict(
  DESCRIPTOR = _SERVERBSADDR,
  __module__ = 'GC_LS_pb2'
  # @@protoc_insertion_point(class_scope:GC_LS.ServerBSAddr)
  ))
_sym_db.RegisterMessage(ServerBSAddr)

ErrorMsg = _reflection.GeneratedProtocolMessageType('ErrorMsg', (_message.Message,), dict(
  DESCRIPTOR = _ERRORMSG,
  __module__ = 'GC_LS_pb2'
  # @@protoc_insertion_point(class_scope:GC_LS.ErrorMsg)
  ))
_sym_db.RegisterMessage(ErrorMsg)


# @@protoc_insertion_point(module_scope)