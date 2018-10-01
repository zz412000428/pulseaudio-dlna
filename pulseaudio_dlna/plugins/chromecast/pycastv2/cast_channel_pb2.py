# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cast_channel.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cast_channel.proto',
  package='extensions.api.cast_channel',
  serialized_pb='\n\x12\x63\x61st_channel.proto\x12\x1b\x65xtensions.api.cast_channel\"\xe3\x02\n\x0b\x43\x61stMessage\x12R\n\x10protocol_version\x18\x01 \x02(\x0e\x32\x38.extensions.api.cast_channel.CastMessage.ProtocolVersion\x12\x11\n\tsource_id\x18\x02 \x02(\t\x12\x16\n\x0e\x64\x65stination_id\x18\x03 \x02(\t\x12\x11\n\tnamespace\x18\x04 \x02(\t\x12J\n\x0cpayload_type\x18\x05 \x02(\x0e\x32\x34.extensions.api.cast_channel.CastMessage.PayloadType\x12\x14\n\x0cpayload_utf8\x18\x06 \x01(\t\x12\x16\n\x0epayload_binary\x18\x07 \x01(\x0c\"!\n\x0fProtocolVersion\x12\x0e\n\nCASTV2_1_0\x10\x00\"%\n\x0bPayloadType\x12\n\n\x06STRING\x10\x00\x12\n\n\x06\x42INARY\x10\x01\"\x0f\n\rAuthChallenge\"B\n\x0c\x41uthResponse\x12\x11\n\tsignature\x18\x01 \x02(\x0c\x12\x1f\n\x17\x63lient_auth_certificate\x18\x02 \x02(\x0c\"~\n\tAuthError\x12\x44\n\nerror_type\x18\x01 \x02(\x0e\x32\x30.extensions.api.cast_channel.AuthError.ErrorType\"+\n\tErrorType\x12\x12\n\x0eINTERNAL_ERROR\x10\x00\x12\n\n\x06NO_TLS\x10\x01\"\xc6\x01\n\x11\x44\x65viceAuthMessage\x12=\n\tchallenge\x18\x01 \x01(\x0b\x32*.extensions.api.cast_channel.AuthChallenge\x12;\n\x08response\x18\x02 \x01(\x0b\x32).extensions.api.cast_channel.AuthResponse\x12\x35\n\x05\x65rror\x18\x03 \x01(\x0b\x32&.extensions.api.cast_channel.AuthErrorB\x02H\x03')



_CASTMESSAGE_PROTOCOLVERSION = _descriptor.EnumDescriptor(
  name='ProtocolVersion',
  full_name='extensions.api.cast_channel.CastMessage.ProtocolVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CASTV2_1_0', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=335,
  serialized_end=368,
)

_CASTMESSAGE_PAYLOADTYPE = _descriptor.EnumDescriptor(
  name='PayloadType',
  full_name='extensions.api.cast_channel.CastMessage.PayloadType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=370,
  serialized_end=407,
)

_AUTHERROR_ERRORTYPE = _descriptor.EnumDescriptor(
  name='ErrorType',
  full_name='extensions.api.cast_channel.AuthError.ErrorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_TLS', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=577,
  serialized_end=620,
)


_CASTMESSAGE = _descriptor.Descriptor(
  name='CastMessage',
  full_name='extensions.api.cast_channel.CastMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='extensions.api.cast_channel.CastMessage.protocol_version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_id', full_name='extensions.api.cast_channel.CastMessage.source_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=bytes("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination_id', full_name='extensions.api.cast_channel.CastMessage.destination_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=bytes("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='extensions.api.cast_channel.CastMessage.namespace', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=bytes("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='extensions.api.cast_channel.CastMessage.payload_type', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_utf8', full_name='extensions.api.cast_channel.CastMessage.payload_utf8', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=bytes("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_binary', full_name='extensions.api.cast_channel.CastMessage.payload_binary', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CASTMESSAGE_PROTOCOLVERSION,
    _CASTMESSAGE_PAYLOADTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=52,
  serialized_end=407,
)


_AUTHCHALLENGE = _descriptor.Descriptor(
  name='AuthChallenge',
  full_name='extensions.api.cast_channel.AuthChallenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=409,
  serialized_end=424,
)


_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='extensions.api.cast_channel.AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='extensions.api.cast_channel.AuthResponse.signature', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_auth_certificate', full_name='extensions.api.cast_channel.AuthResponse.client_auth_certificate', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=426,
  serialized_end=492,
)


_AUTHERROR = _descriptor.Descriptor(
  name='AuthError',
  full_name='extensions.api.cast_channel.AuthError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_type', full_name='extensions.api.cast_channel.AuthError.error_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUTHERROR_ERRORTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=494,
  serialized_end=620,
)


_DEVICEAUTHMESSAGE = _descriptor.Descriptor(
  name='DeviceAuthMessage',
  full_name='extensions.api.cast_channel.DeviceAuthMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge', full_name='extensions.api.cast_channel.DeviceAuthMessage.challenge', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='extensions.api.cast_channel.DeviceAuthMessage.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='extensions.api.cast_channel.DeviceAuthMessage.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=623,
  serialized_end=821,
)

_CASTMESSAGE.fields_by_name['protocol_version'].enum_type = _CASTMESSAGE_PROTOCOLVERSION
_CASTMESSAGE.fields_by_name['payload_type'].enum_type = _CASTMESSAGE_PAYLOADTYPE
_CASTMESSAGE_PROTOCOLVERSION.containing_type = _CASTMESSAGE;
_CASTMESSAGE_PAYLOADTYPE.containing_type = _CASTMESSAGE;
_AUTHERROR.fields_by_name['error_type'].enum_type = _AUTHERROR_ERRORTYPE
_AUTHERROR_ERRORTYPE.containing_type = _AUTHERROR;
_DEVICEAUTHMESSAGE.fields_by_name['challenge'].message_type = _AUTHCHALLENGE
_DEVICEAUTHMESSAGE.fields_by_name['response'].message_type = _AUTHRESPONSE
_DEVICEAUTHMESSAGE.fields_by_name['error'].message_type = _AUTHERROR
DESCRIPTOR.message_types_by_name['CastMessage'] = _CASTMESSAGE
DESCRIPTOR.message_types_by_name['AuthChallenge'] = _AUTHCHALLENGE
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
DESCRIPTOR.message_types_by_name['AuthError'] = _AUTHERROR
DESCRIPTOR.message_types_by_name['DeviceAuthMessage'] = _DEVICEAUTHMESSAGE

class CastMessage(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
  DESCRIPTOR = _CASTMESSAGE

  # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.CastMessage)

class AuthChallenge(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
  DESCRIPTOR = _AUTHCHALLENGE

  # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.AuthChallenge)

class AuthResponse(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
  DESCRIPTOR = _AUTHRESPONSE

  # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.AuthResponse)

class AuthError(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
  DESCRIPTOR = _AUTHERROR

  # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.AuthError)

class DeviceAuthMessage(_message.Message, metaclass=_reflection.GeneratedProtocolMessageType):
  DESCRIPTOR = _DEVICEAUTHMESSAGE

  # @@protoc_insertion_point(class_scope:extensions.api.cast_channel.DeviceAuthMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)
