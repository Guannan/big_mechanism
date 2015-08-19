# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: table.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='table.proto',
  package='table',
  serialized_pb='\n\x0btable.proto\x12\x05table\"\x14\n\x04\x43\x65ll\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\t\"@\n\x06\x43olumn\x12\x1b\n\x06header\x18\x01 \x02(\x0b\x32\x0b.table.Cell\x12\x19\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x0b.table.Cell\"`\n\x06Source\x12\x12\n\npaperTitle\x18\x01 \x02(\t\x12\r\n\x05pmcId\x18\x02 \x02(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x02(\t\x12\x12\n\nsourceFile\x18\x04 \x01(\t\x12\x0f\n\x07sheetNo\x18\x05 \x01(\t\"V\n\x05Table\x12\x1d\n\x06\x63olumn\x18\x01 \x03(\x0b\x32\r.table.Column\x12\x0f\n\x07\x63\x61ption\x18\x02 \x03(\t\x12\x1d\n\x06source\x18\x03 \x02(\x0b\x32\r.table.SourceB\x1a\n\x0e\x65xtract.bufferB\x08TableBuf')




_CELL = _descriptor.Descriptor(
  name='Cell',
  full_name='table.Cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='table.Cell.data', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=22,
  serialized_end=42,
)


_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='table.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='table.Column.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='table.Column.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=44,
  serialized_end=108,
)


_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='table.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paperTitle', full_name='table.Source.paperTitle', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pmcId', full_name='table.Source.pmcId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='table.Source.author', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sourceFile', full_name='table.Source.sourceFile', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sheetNo', full_name='table.Source.sheetNo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=110,
  serialized_end=206,
)


_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='table.Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='table.Table.column', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='table.Table.caption', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='table.Table.source', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=208,
  serialized_end=294,
)

_COLUMN.fields_by_name['header'].message_type = _CELL
_COLUMN.fields_by_name['data'].message_type = _CELL
_TABLE.fields_by_name['column'].message_type = _COLUMN
_TABLE.fields_by_name['source'].message_type = _SOURCE
DESCRIPTOR.message_types_by_name['Cell'] = _CELL
DESCRIPTOR.message_types_by_name['Column'] = _COLUMN
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
DESCRIPTOR.message_types_by_name['Table'] = _TABLE

class Cell(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CELL

  # @@protoc_insertion_point(class_scope:table.Cell)

class Column(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COLUMN

  # @@protoc_insertion_point(class_scope:table.Column)

class Source(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOURCE

  # @@protoc_insertion_point(class_scope:table.Source)

class Table(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TABLE

  # @@protoc_insertion_point(class_scope:table.Table)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\016extract.bufferB\010TableBuf')
# @@protoc_insertion_point(module_scope)
