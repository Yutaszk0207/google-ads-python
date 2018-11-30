# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/campaign_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import campaign_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/campaign_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/services/campaign_service.proto\x12 google.ads.googleads.v0.services\x1a\x36google/ads/googleads_v0/proto/resources/campaign.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"+\n\x12GetCampaignRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"v\n\x16MutateCampaignsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12G\n\noperations\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v0.services.CampaignOperation\"\xe1\x01\n\x11\x43\x61mpaignOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12=\n\x06\x63reate\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v0.resources.CampaignH\x00\x12=\n\x06update\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v0.resources.CampaignH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"b\n\x17MutateCampaignsResponse\x12G\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v0.services.MutateCampaignResult\"-\n\x14MutateCampaignResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xfd\x02\n\x0f\x43\x61mpaignService\x12\xa5\x01\n\x0bGetCampaign\x12\x34.google.ads.googleads.v0.services.GetCampaignRequest\x1a+.google.ads.googleads.v0.resources.Campaign\"3\x82\xd3\xe4\x93\x02-\x12+/v0/{resource_name=customers/*/campaigns/*}\x12\xc1\x01\n\x0fMutateCampaigns\x12\x38.google.ads.googleads.v0.services.MutateCampaignsRequest\x1a\x39.google.ads.googleads.v0.services.MutateCampaignsResponse\"9\x82\xd3\xe4\x93\x02\x33\"./v0/customers/{customer_id=*}/campaigns:mutate:\x01*B\xd4\x01\n$com.google.ads.googleads.v0.servicesB\x14\x43\x61mpaignServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETCAMPAIGNREQUEST = _descriptor.Descriptor(
  name='GetCampaignRequest',
  full_name='google.ads.googleads.v0.services.GetCampaignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetCampaignRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=262,
)


_MUTATECAMPAIGNSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignsRequest',
  full_name='google.ads.googleads.v0.services.MutateCampaignsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateCampaignsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateCampaignsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=382,
)


_CAMPAIGNOPERATION = _descriptor.Descriptor(
  name='CampaignOperation',
  full_name='google.ads.googleads.v0.services.CampaignOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.CampaignOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.CampaignOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.CampaignOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.CampaignOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.CampaignOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=385,
  serialized_end=610,
)


_MUTATECAMPAIGNSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignsResponse',
  full_name='google.ads.googleads.v0.services.MutateCampaignsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateCampaignsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=612,
  serialized_end=710,
)


_MUTATECAMPAIGNRESULT = _descriptor.Descriptor(
  name='MutateCampaignResult',
  full_name='google.ads.googleads.v0.services.MutateCampaignResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateCampaignResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=757,
)

_MUTATECAMPAIGNSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNOPERATION
_CAMPAIGNOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN
_CAMPAIGNOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['create'])
_CAMPAIGNOPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['update'])
_CAMPAIGNOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_CAMPAIGNOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNOPERATION.fields_by_name['remove'])
_CAMPAIGNOPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNRESULT
DESCRIPTOR.message_types_by_name['GetCampaignRequest'] = _GETCAMPAIGNREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignsRequest'] = _MUTATECAMPAIGNSREQUEST
DESCRIPTOR.message_types_by_name['CampaignOperation'] = _CAMPAIGNOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignsResponse'] = _MUTATECAMPAIGNSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignResult'] = _MUTATECAMPAIGNRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignRequest = _reflection.GeneratedProtocolMessageType('GetCampaignRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCAMPAIGNREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.campaign_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignService.GetCampaign][google.ads.googleads.v0.services.CampaignService.GetCampaign].
  
  
  Attributes:
      resource_name:
          The resource name of the campaign to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetCampaignRequest)
  ))
_sym_db.RegisterMessage(GetCampaignRequest)

MutateCampaignsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNSREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.campaign_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignService.MutateCampaigns][google.ads.googleads.v0.services.CampaignService.MutateCampaigns].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose campaigns are being modified.
      operations:
          The list of operations to perform on individual campaigns.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCampaignsRequest)
  ))
_sym_db.RegisterMessage(MutateCampaignsRequest)

CampaignOperation = _reflection.GeneratedProtocolMessageType('CampaignOperation', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNOPERATION,
  __module__ = 'google.ads.google_ads.v0.proto.services.campaign_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a campaign.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          campaign.
      update:
          Update operation: The campaign is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the removed campaign is
          expected, in this format:
          ``customers/{customer_id}/campaigns/{campaign_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.CampaignOperation)
  ))
_sym_db.RegisterMessage(CampaignOperation)

MutateCampaignsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNSRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.campaign_service_pb2'
  ,
  __doc__ = """Response message for campaign mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCampaignsResponse)
  ))
_sym_db.RegisterMessage(MutateCampaignsResponse)

MutateCampaignResult = _reflection.GeneratedProtocolMessageType('MutateCampaignResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNRESULT,
  __module__ = 'google.ads.google_ads.v0.proto.services.campaign_service_pb2'
  ,
  __doc__ = """The result for the campaign mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCampaignResult)
  ))
_sym_db.RegisterMessage(MutateCampaignResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\024CampaignServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_CAMPAIGNSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignService',
  full_name='google.ads.googleads.v0.services.CampaignService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=760,
  serialized_end=1141,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaign',
    full_name='google.ads.googleads.v0.services.CampaignService.GetCampaign',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002-\022+/v0/{resource_name=customers/*/campaigns/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaigns',
    full_name='google.ads.googleads.v0.services.CampaignService.MutateCampaigns',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNSREQUEST,
    output_type=_MUTATECAMPAIGNSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0023\"./v0/customers/{customer_id=*}/campaigns:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNSERVICE)

DESCRIPTOR.services_by_name['CampaignService'] = _CAMPAIGNSERVICE

# @@protoc_insertion_point(module_scope)
