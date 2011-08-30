# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='status.proto',
  package='server.status',
  serialized_pb='\n\x0cstatus.proto\x12\rserver.status\"E\n\nTCPRequest\x12\x11\n\tclient_ip\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x11\n\tuser_pass\x18\x03 \x01(\t\"\x88\x01\n\x0bTCPResponse\x12\x15\n\rrequest_total\x18\x01 \x02(\x04\x12\x14\n\x0cread_timeout\x18\x02 \x02(\x04\x12\x18\n\x10max_request_time\x18\x03 \x02(\x02\x12\x18\n\x10min_request_time\x18\x04 \x02(\x02\x12\x18\n\x10\x61vg_request_time\x18\x05 \x02(\x02\"\xe9\x03\n\x0bRPCResponse\x12\x15\n\rrequest_total\x18\x01 \x02(\x04\x12\x13\n\x0b\x62\x61\x64_request\x18\x02 \x02(\x04\x12\x45\n\x11service_not_found\x18\x03 \x03(\x0b\x32*.server.status.RPCResponse.ServiceNotFound\x12\x43\n\x10method_not_found\x18\x04 \x03(\x0b\x32).server.status.RPCResponse.MethodNotFound\x12@\n\x0eservice_status\x18\x05 \x03(\x0b\x32(.server.status.RPCResponse.ServiceStatus\x1a\x36\n\x0fServiceNotFound\x12\x14\n\x0cservice_name\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x02(\x04\x1a\x34\n\x0eMethodNotFound\x12\x13\n\x0bmethod_name\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x02(\x04\x1ar\n\rServiceStatus\x12\x14\n\x0cservice_name\x18\x01 \x02(\t\x12\x10\n\x08min_time\x18\x02 \x02(\x02\x12\x10\n\x08max_time\x18\x03 \x02(\x02\x12\x10\n\x08\x61vg_time\x18\x04 \x02(\x02\x12\x15\n\rrequest_total\x18\x05 \x02(\x02\"E\n\nRPCRequest\x12\x11\n\tclient_ip\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x11\n\tuser_pass\x18\x03 \x01(\t2\x97\x01\n\rStatusService\x12\x42\n\tTCPStatus\x12\x19.server.status.TCPRequest\x1a\x1a.server.status.TCPResponse\x12\x42\n\tRPCStatus\x12\x19.server.status.RPCRequest\x1a\x1a.server.status.RPCResponseB\x03\x90\x01\x01')




_TCPREQUEST = descriptor.Descriptor(
  name='TCPRequest',
  full_name='server.status.TCPRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_ip', full_name='server.status.TCPRequest.client_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_name', full_name='server.status.TCPRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_pass', full_name='server.status.TCPRequest.user_pass', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=100,
)


_TCPRESPONSE = descriptor.Descriptor(
  name='TCPResponse',
  full_name='server.status.TCPResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request_total', full_name='server.status.TCPResponse.request_total', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='read_timeout', full_name='server.status.TCPResponse.read_timeout', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_request_time', full_name='server.status.TCPResponse.max_request_time', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_request_time', full_name='server.status.TCPResponse.min_request_time', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avg_request_time', full_name='server.status.TCPResponse.avg_request_time', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=103,
  serialized_end=239,
)


_RPCRESPONSE_SERVICENOTFOUND = descriptor.Descriptor(
  name='ServiceNotFound',
  full_name='server.status.RPCResponse.ServiceNotFound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_name', full_name='server.status.RPCResponse.ServiceNotFound.service_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='server.status.RPCResponse.ServiceNotFound.count', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=507,
  serialized_end=561,
)

_RPCRESPONSE_METHODNOTFOUND = descriptor.Descriptor(
  name='MethodNotFound',
  full_name='server.status.RPCResponse.MethodNotFound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='method_name', full_name='server.status.RPCResponse.MethodNotFound.method_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='server.status.RPCResponse.MethodNotFound.count', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=563,
  serialized_end=615,
)

_RPCRESPONSE_SERVICESTATUS = descriptor.Descriptor(
  name='ServiceStatus',
  full_name='server.status.RPCResponse.ServiceStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_name', full_name='server.status.RPCResponse.ServiceStatus.service_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_time', full_name='server.status.RPCResponse.ServiceStatus.min_time', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_time', full_name='server.status.RPCResponse.ServiceStatus.max_time', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avg_time', full_name='server.status.RPCResponse.ServiceStatus.avg_time', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='request_total', full_name='server.status.RPCResponse.ServiceStatus.request_total', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=617,
  serialized_end=731,
)

_RPCRESPONSE = descriptor.Descriptor(
  name='RPCResponse',
  full_name='server.status.RPCResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request_total', full_name='server.status.RPCResponse.request_total', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bad_request', full_name='server.status.RPCResponse.bad_request', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service_not_found', full_name='server.status.RPCResponse.service_not_found', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method_not_found', full_name='server.status.RPCResponse.method_not_found', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service_status', full_name='server.status.RPCResponse.service_status', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RPCRESPONSE_SERVICENOTFOUND, _RPCRESPONSE_METHODNOTFOUND, _RPCRESPONSE_SERVICESTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=242,
  serialized_end=731,
)


_RPCREQUEST = descriptor.Descriptor(
  name='RPCRequest',
  full_name='server.status.RPCRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_ip', full_name='server.status.RPCRequest.client_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_name', full_name='server.status.RPCRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_pass', full_name='server.status.RPCRequest.user_pass', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=733,
  serialized_end=802,
)

_RPCRESPONSE_SERVICENOTFOUND.containing_type = _RPCRESPONSE;
_RPCRESPONSE_METHODNOTFOUND.containing_type = _RPCRESPONSE;
_RPCRESPONSE_SERVICESTATUS.containing_type = _RPCRESPONSE;
_RPCRESPONSE.fields_by_name['service_not_found'].message_type = _RPCRESPONSE_SERVICENOTFOUND
_RPCRESPONSE.fields_by_name['method_not_found'].message_type = _RPCRESPONSE_METHODNOTFOUND
_RPCRESPONSE.fields_by_name['service_status'].message_type = _RPCRESPONSE_SERVICESTATUS
DESCRIPTOR.message_types_by_name['TCPRequest'] = _TCPREQUEST
DESCRIPTOR.message_types_by_name['TCPResponse'] = _TCPRESPONSE
DESCRIPTOR.message_types_by_name['RPCResponse'] = _RPCRESPONSE
DESCRIPTOR.message_types_by_name['RPCRequest'] = _RPCREQUEST

class TCPRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCPREQUEST
  
  # @@protoc_insertion_point(class_scope:server.status.TCPRequest)

class TCPResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCPRESPONSE
  
  # @@protoc_insertion_point(class_scope:server.status.TCPResponse)

class RPCResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class ServiceNotFound(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RPCRESPONSE_SERVICENOTFOUND
    
    # @@protoc_insertion_point(class_scope:server.status.RPCResponse.ServiceNotFound)
  
  class MethodNotFound(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RPCRESPONSE_METHODNOTFOUND
    
    # @@protoc_insertion_point(class_scope:server.status.RPCResponse.MethodNotFound)
  
  class ServiceStatus(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RPCRESPONSE_SERVICESTATUS
    
    # @@protoc_insertion_point(class_scope:server.status.RPCResponse.ServiceStatus)
  DESCRIPTOR = _RPCRESPONSE
  
  # @@protoc_insertion_point(class_scope:server.status.RPCResponse)

class RPCRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPCREQUEST
  
  # @@protoc_insertion_point(class_scope:server.status.RPCRequest)


_STATUSSERVICE = descriptor.ServiceDescriptor(
  name='StatusService',
  full_name='server.status.StatusService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=805,
  serialized_end=956,
  methods=[
  descriptor.MethodDescriptor(
    name='TCPStatus',
    full_name='server.status.StatusService.TCPStatus',
    index=0,
    containing_service=None,
    input_type=_TCPREQUEST,
    output_type=_TCPRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='RPCStatus',
    full_name='server.status.StatusService.RPCStatus',
    index=1,
    containing_service=None,
    input_type=_RPCREQUEST,
    output_type=_RPCRESPONSE,
    options=None,
  ),
])

class StatusService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _STATUSSERVICE
class StatusService_Stub(StatusService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _STATUSSERVICE

# @@protoc_insertion_point(module_scope)
