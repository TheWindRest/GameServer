# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CS_GS.proto

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
  name='CS_GS.proto',
  package='CS_GS',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x43S_GS.proto\x12\x05\x43S_GS\"k\n\x0b\x41skRegister\x12.\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x11\x43S2GS_AskRegister\x12\r\n\x05state\x18\x02 \x01(\x05\x12\x1d\n\x07msgList\x18\x03 \x03(\x0e\x32\x0c.CS_GS.MsgID\"E\n\x08\x45rrorMsg\x12(\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x0bGS2CS_Error\x12\x0f\n\x07\x65rrorid\x18\x02 \x01(\x05\"F\n\x0bTransmitMsg\x12\x0c\n\x04mail\x18\x01 \x01(\t\x12\x1b\n\x05msgid\x18\x02 \x01(\x0e\x32\x0c.CS_GS.MsgID\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"E\n\x08UserInfo\x12+\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x0e\x43S2GS_UserInfo\x12\x0c\n\x04name\x18\x02 \x01(\t\"Y\n\nStartMatch\x12-\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x10\x43S2GS_StartMatch\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\x05\"\x85\x01\n\tEnterRoom\x12,\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x0f\x43S2GS_EnterRoom\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06roomid\x18\x04 \x01(\t\x12\r\n\x05mapid\x18\x05 \x01(\t\x12\x0f\n\x07mapdata\x18\x06 \x01(\t\"P\n\rTransformInfo\x12\x0c\n\x04mail\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x02 \x01(\x02\x12\x10\n\x08position\x18\x03 \x03(\x02\x12\x10\n\x08rotation\x18\x04 \x03(\x02\"\x8c\x01\n\rTransformSync\x12\x30\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x13\x43S2GS_TransformSync\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x0e\n\x06roomid\x18\x03 \x01(\t\x12+\n\rtransforminfo\x18\x04 \x03(\x0b\x32\x14.CS_GS.TransformInfo\"v\n\tStateSync\x12,\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x0f\x43S2GS_StateSync\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x0e\n\x06roomid\x18\x03 \x01(\t\x12\x1d\n\x06\x65ntity\x18\x04 \x01(\x0b\x32\r.CS_GS.Entity\"m\n\x0bShootBullet\x12.\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x11\x43S2GS_ShootBullet\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x0e\n\x06roomid\x18\x03 \x01(\t\x12\x10\n\x08weaponid\x18\x04 \x01(\x05\"`\n\x06\x45ntity\x12%\n\nentitytype\x18\x01 \x01(\x0e\x32\x11.CS_GS.EntityType\x12\x10\n\x08\x65ntityid\x18\x02 \x01(\t\x12\x0e\n\x06health\x18\x03 \x01(\x05\x12\r\n\x05score\x18\x04 \x01(\x05\"\xcc\x01\n\nTakeDamage\x12-\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x10\x43S2GS_TakeDamage\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x0e\n\x06roomid\x18\x03 \x01(\t\x12\x10\n\x08weaponid\x18\x04 \x01(\x05\x12\x10\n\x08\x62ulletid\x18\x05 \x01(\x05\x12\x1e\n\x07shooter\x18\x06 \x01(\x0b\x32\r.CS_GS.Entity\x12\x1d\n\x06target\x18\x07 \x01(\x0b\x32\r.CS_GS.Entity\x12\x0e\n\x06\x64\x61mage\x18\x08 \x01(\x05\"n\n\rEntityDestroy\x12\x30\n\x05msgid\x18\x01 \x01(\x0e\x32\x0c.CS_GS.MsgID:\x13\x43S2GS_EntityDestroy\x12\x0c\n\x04mail\x18\x02 \x01(\t\x12\x1d\n\x06\x65ntity\x18\x03 \x01(\x0b\x32\r.CS_GS.Entity*\xec\x01\n\x05MsgID\x12\x16\n\x11\x43S2GS_AskRegister\x10\xd0\x0f\x12\x10\n\x0bGS2CS_Error\x10\xd1\x0f\x12\x13\n\x0e\x43S2GS_UserInfo\x10\xd2\x0f\x12\x15\n\x10\x43S2GS_StartMatch\x10\xd3\x0f\x12\x14\n\x0f\x43S2GS_EnterRoom\x10\xd4\x0f\x12\x18\n\x13\x43S2GS_TransformSync\x10\xd5\x0f\x12\x14\n\x0f\x43S2GS_StateSync\x10\xd6\x0f\x12\x16\n\x11\x43S2GS_ShootBullet\x10\xd7\x0f\x12\x15\n\x10\x43S2GS_TakeDamage\x10\xd8\x0f\x12\x18\n\x13\x43S2GS_EntityDestroy\x10\xd9\x0f*2\n\nEntityType\x12\x11\n\rEntity_Active\x10\x01\x12\x11\n\rEntity_Static\x10\x02')
)

_MSGID = _descriptor.EnumDescriptor(
  name='MsgID',
  full_name='CS_GS.MsgID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CS2GS_AskRegister', index=0, number=2000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GS2CS_Error', index=1, number=2001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_UserInfo', index=2, number=2002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_StartMatch', index=3, number=2003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_EnterRoom', index=4, number=2004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_TransformSync', index=5, number=2005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_StateSync', index=6, number=2006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_ShootBullet', index=7, number=2007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_TakeDamage', index=8, number=2008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CS2GS_EntityDestroy', index=9, number=2009,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1446,
  serialized_end=1682,
)
_sym_db.RegisterEnumDescriptor(_MSGID)

MsgID = enum_type_wrapper.EnumTypeWrapper(_MSGID)
_ENTITYTYPE = _descriptor.EnumDescriptor(
  name='EntityType',
  full_name='CS_GS.EntityType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Entity_Active', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Entity_Static', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1684,
  serialized_end=1734,
)
_sym_db.RegisterEnumDescriptor(_ENTITYTYPE)

EntityType = enum_type_wrapper.EnumTypeWrapper(_ENTITYTYPE)
CS2GS_AskRegister = 2000
GS2CS_Error = 2001
CS2GS_UserInfo = 2002
CS2GS_StartMatch = 2003
CS2GS_EnterRoom = 2004
CS2GS_TransformSync = 2005
CS2GS_StateSync = 2006
CS2GS_ShootBullet = 2007
CS2GS_TakeDamage = 2008
CS2GS_EntityDestroy = 2009
Entity_Active = 1
Entity_Static = 2



_ASKREGISTER = _descriptor.Descriptor(
  name='AskRegister',
  full_name='CS_GS.AskRegister',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.AskRegister.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='CS_GS.AskRegister.state', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgList', full_name='CS_GS.AskRegister.msgList', index=2,
      number=3, type=14, cpp_type=8, label=3,
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
  serialized_start=22,
  serialized_end=129,
)


_ERRORMSG = _descriptor.Descriptor(
  name='ErrorMsg',
  full_name='CS_GS.ErrorMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.ErrorMsg.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2001,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorid', full_name='CS_GS.ErrorMsg.errorid', index=1,
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
  serialized_start=131,
  serialized_end=200,
)


_TRANSMITMSG = _descriptor.Descriptor(
  name='TransmitMsg',
  full_name='CS_GS.TransmitMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.TransmitMsg.mail', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.TransmitMsg.msgid', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='CS_GS.TransmitMsg.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=202,
  serialized_end=272,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='CS_GS.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.UserInfo.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2002,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='CS_GS.UserInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=274,
  serialized_end=343,
)


_STARTMATCH = _descriptor.Descriptor(
  name='StartMatch',
  full_name='CS_GS.StartMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.StartMatch.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2003,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.StartMatch.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='CS_GS.StartMatch.result', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=345,
  serialized_end=434,
)


_ENTERROOM = _descriptor.Descriptor(
  name='EnterRoom',
  full_name='CS_GS.EnterRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.EnterRoom.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2004,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.EnterRoom.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='CS_GS.EnterRoom.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='CS_GS.EnterRoom.roomid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapid', full_name='CS_GS.EnterRoom.mapid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapdata', full_name='CS_GS.EnterRoom.mapdata', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=437,
  serialized_end=570,
)


_TRANSFORMINFO = _descriptor.Descriptor(
  name='TransformInfo',
  full_name='CS_GS.TransformInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.TransformInfo.mail', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='CS_GS.TransformInfo.speed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='CS_GS.TransformInfo.position', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='CS_GS.TransformInfo.rotation', index=3,
      number=4, type=2, cpp_type=6, label=3,
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
  serialized_start=572,
  serialized_end=652,
)


_TRANSFORMSYNC = _descriptor.Descriptor(
  name='TransformSync',
  full_name='CS_GS.TransformSync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.TransformSync.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2005,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.TransformSync.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='CS_GS.TransformSync.roomid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transforminfo', full_name='CS_GS.TransformSync.transforminfo', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=655,
  serialized_end=795,
)


_STATESYNC = _descriptor.Descriptor(
  name='StateSync',
  full_name='CS_GS.StateSync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.StateSync.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2006,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.StateSync.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='CS_GS.StateSync.roomid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity', full_name='CS_GS.StateSync.entity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=797,
  serialized_end=915,
)


_SHOOTBULLET = _descriptor.Descriptor(
  name='ShootBullet',
  full_name='CS_GS.ShootBullet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.ShootBullet.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2007,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.ShootBullet.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='CS_GS.ShootBullet.roomid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weaponid', full_name='CS_GS.ShootBullet.weaponid', index=3,
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
  serialized_start=917,
  serialized_end=1026,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='CS_GS.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entitytype', full_name='CS_GS.Entity.entitytype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityid', full_name='CS_GS.Entity.entityid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='CS_GS.Entity.health', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='CS_GS.Entity.score', index=3,
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
  serialized_start=1028,
  serialized_end=1124,
)


_TAKEDAMAGE = _descriptor.Descriptor(
  name='TakeDamage',
  full_name='CS_GS.TakeDamage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.TakeDamage.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2008,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.TakeDamage.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roomid', full_name='CS_GS.TakeDamage.roomid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weaponid', full_name='CS_GS.TakeDamage.weaponid', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bulletid', full_name='CS_GS.TakeDamage.bulletid', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shooter', full_name='CS_GS.TakeDamage.shooter', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='CS_GS.TakeDamage.target', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='damage', full_name='CS_GS.TakeDamage.damage', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=1127,
  serialized_end=1331,
)


_ENTITYDESTROY = _descriptor.Descriptor(
  name='EntityDestroy',
  full_name='CS_GS.EntityDestroy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgid', full_name='CS_GS.EntityDestroy.msgid', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2009,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='CS_GS.EntityDestroy.mail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity', full_name='CS_GS.EntityDestroy.entity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1333,
  serialized_end=1443,
)

_ASKREGISTER.fields_by_name['msgid'].enum_type = _MSGID
_ASKREGISTER.fields_by_name['msgList'].enum_type = _MSGID
_ERRORMSG.fields_by_name['msgid'].enum_type = _MSGID
_TRANSMITMSG.fields_by_name['msgid'].enum_type = _MSGID
_USERINFO.fields_by_name['msgid'].enum_type = _MSGID
_STARTMATCH.fields_by_name['msgid'].enum_type = _MSGID
_ENTERROOM.fields_by_name['msgid'].enum_type = _MSGID
_TRANSFORMSYNC.fields_by_name['msgid'].enum_type = _MSGID
_TRANSFORMSYNC.fields_by_name['transforminfo'].message_type = _TRANSFORMINFO
_STATESYNC.fields_by_name['msgid'].enum_type = _MSGID
_STATESYNC.fields_by_name['entity'].message_type = _ENTITY
_SHOOTBULLET.fields_by_name['msgid'].enum_type = _MSGID
_ENTITY.fields_by_name['entitytype'].enum_type = _ENTITYTYPE
_TAKEDAMAGE.fields_by_name['msgid'].enum_type = _MSGID
_TAKEDAMAGE.fields_by_name['shooter'].message_type = _ENTITY
_TAKEDAMAGE.fields_by_name['target'].message_type = _ENTITY
_ENTITYDESTROY.fields_by_name['msgid'].enum_type = _MSGID
_ENTITYDESTROY.fields_by_name['entity'].message_type = _ENTITY
DESCRIPTOR.message_types_by_name['AskRegister'] = _ASKREGISTER
DESCRIPTOR.message_types_by_name['ErrorMsg'] = _ERRORMSG
DESCRIPTOR.message_types_by_name['TransmitMsg'] = _TRANSMITMSG
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['StartMatch'] = _STARTMATCH
DESCRIPTOR.message_types_by_name['EnterRoom'] = _ENTERROOM
DESCRIPTOR.message_types_by_name['TransformInfo'] = _TRANSFORMINFO
DESCRIPTOR.message_types_by_name['TransformSync'] = _TRANSFORMSYNC
DESCRIPTOR.message_types_by_name['StateSync'] = _STATESYNC
DESCRIPTOR.message_types_by_name['ShootBullet'] = _SHOOTBULLET
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['TakeDamage'] = _TAKEDAMAGE
DESCRIPTOR.message_types_by_name['EntityDestroy'] = _ENTITYDESTROY
DESCRIPTOR.enum_types_by_name['MsgID'] = _MSGID
DESCRIPTOR.enum_types_by_name['EntityType'] = _ENTITYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AskRegister = _reflection.GeneratedProtocolMessageType('AskRegister', (_message.Message,), dict(
  DESCRIPTOR = _ASKREGISTER,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.AskRegister)
  ))
_sym_db.RegisterMessage(AskRegister)

ErrorMsg = _reflection.GeneratedProtocolMessageType('ErrorMsg', (_message.Message,), dict(
  DESCRIPTOR = _ERRORMSG,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.ErrorMsg)
  ))
_sym_db.RegisterMessage(ErrorMsg)

TransmitMsg = _reflection.GeneratedProtocolMessageType('TransmitMsg', (_message.Message,), dict(
  DESCRIPTOR = _TRANSMITMSG,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.TransmitMsg)
  ))
_sym_db.RegisterMessage(TransmitMsg)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)

StartMatch = _reflection.GeneratedProtocolMessageType('StartMatch', (_message.Message,), dict(
  DESCRIPTOR = _STARTMATCH,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.StartMatch)
  ))
_sym_db.RegisterMessage(StartMatch)

EnterRoom = _reflection.GeneratedProtocolMessageType('EnterRoom', (_message.Message,), dict(
  DESCRIPTOR = _ENTERROOM,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.EnterRoom)
  ))
_sym_db.RegisterMessage(EnterRoom)

TransformInfo = _reflection.GeneratedProtocolMessageType('TransformInfo', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMINFO,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.TransformInfo)
  ))
_sym_db.RegisterMessage(TransformInfo)

TransformSync = _reflection.GeneratedProtocolMessageType('TransformSync', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMSYNC,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.TransformSync)
  ))
_sym_db.RegisterMessage(TransformSync)

StateSync = _reflection.GeneratedProtocolMessageType('StateSync', (_message.Message,), dict(
  DESCRIPTOR = _STATESYNC,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.StateSync)
  ))
_sym_db.RegisterMessage(StateSync)

ShootBullet = _reflection.GeneratedProtocolMessageType('ShootBullet', (_message.Message,), dict(
  DESCRIPTOR = _SHOOTBULLET,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.ShootBullet)
  ))
_sym_db.RegisterMessage(ShootBullet)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), dict(
  DESCRIPTOR = _ENTITY,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.Entity)
  ))
_sym_db.RegisterMessage(Entity)

TakeDamage = _reflection.GeneratedProtocolMessageType('TakeDamage', (_message.Message,), dict(
  DESCRIPTOR = _TAKEDAMAGE,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.TakeDamage)
  ))
_sym_db.RegisterMessage(TakeDamage)

EntityDestroy = _reflection.GeneratedProtocolMessageType('EntityDestroy', (_message.Message,), dict(
  DESCRIPTOR = _ENTITYDESTROY,
  __module__ = 'CS_GS_pb2'
  # @@protoc_insertion_point(class_scope:CS_GS.EntityDestroy)
  ))
_sym_db.RegisterMessage(EntityDestroy)


# @@protoc_insertion_point(module_scope)