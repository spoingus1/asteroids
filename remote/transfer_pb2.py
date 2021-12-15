# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transfer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0etransfer.proto\"U\n\x08Outbound\x12\t\n\x01X\x18\x01 \x01(\x05\x12\t\n\x01Y\x18\x02 \x01(\x05\x12\n\n\x02\x64X\x18\x03 \x01(\x05\x12\n\n\x02\x64Y\x18\x04 \x01(\x05\x12\x0c\n\x04size\x18\x05 \x01(\x05\x12\r\n\x05\x63olor\x18\x06 \x01(\x05\"\x19\n\x07Success\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32)\n\x08Transfer\x12\x1d\n\x04Xfer\x12\t.Outbound\x1a\x08.Success\"\x00\x62\x06proto3'
)




_OUTBOUND = _descriptor.Descriptor(
  name='Outbound',
  full_name='Outbound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='Outbound.X', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Y', full_name='Outbound.Y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dX', full_name='Outbound.dX', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dY', full_name='Outbound.dY', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='Outbound.size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='Outbound.color', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=18,
  serialized_end=103,
)


_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='Success.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=105,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['Outbound'] = _OUTBOUND
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Outbound = _reflection.GeneratedProtocolMessageType('Outbound', (_message.Message,), {
  'DESCRIPTOR' : _OUTBOUND,
  '__module__' : 'transfer_pb2'
  # @@protoc_insertion_point(class_scope:Outbound)
  })
_sym_db.RegisterMessage(Outbound)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESS,
  '__module__' : 'transfer_pb2'
  # @@protoc_insertion_point(class_scope:Success)
  })
_sym_db.RegisterMessage(Success)



_TRANSFER = _descriptor.ServiceDescriptor(
  name='Transfer',
  full_name='Transfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=132,
  serialized_end=173,
  methods=[
  _descriptor.MethodDescriptor(
    name='Xfer',
    full_name='Transfer.Xfer',
    index=0,
    containing_service=None,
    input_type=_OUTBOUND,
    output_type=_SUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSFER)

DESCRIPTOR.services_by_name['Transfer'] = _TRANSFER

# @@protoc_insertion_point(module_scope)
