# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NetspeakService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NetspeakService.proto',
  package='netspeak.service',
  syntax='proto3',
  serialized_options=b'\n\024org.netspeak.serviceH\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15NetspeakService.proto\x12\x10netspeak.service\"\x84\x01\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0e\n\x06\x63orpus\x18\x02 \x01(\t\x12\x13\n\x0bmax_phrases\x18\x03 \x01(\r\x12?\n\x12phrase_constraints\x18\x04 \x01(\x0b\x32#.netspeak.service.PhraseConstraints\"P\n\x11PhraseConstraints\x12\x15\n\rfrequency_max\x18\x01 \x01(\x04\x12\x11\n\twords_min\x18\x02 \x01(\r\x12\x11\n\twords_max\x18\x03 \x01(\r\"\xbe\x02\n\x06Phrase\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tfrequency\x18\x02 \x01(\x04\x12,\n\x05words\x18\x03 \x03(\x0b\x32\x1d.netspeak.service.Phrase.Word\x1a\xe6\x01\n\x04Word\x12.\n\x03tag\x18\x01 \x01(\x0e\x32!.netspeak.service.Phrase.Word.Tag\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x9f\x01\n\x03Tag\x12\x08\n\x04WORD\x10\x00\x12\x12\n\x0eWORD_FOR_QMARK\x10\x01\x12\x11\n\rWORD_FOR_STAR\x10\x02\x12\x13\n\x0fWORD_IN_DICTSET\x10\x03\x12\x14\n\x10WORD_IN_ORDERSET\x10\x04\x12\x15\n\x11WORD_IN_OPTIONSET\x10\x05\x12\x11\n\rWORD_FOR_PLUS\x10\x06\x12\x12\n\x0eWORD_FOR_REGEX\x10\x07\"\x99\x03\n\x0eSearchResponse\x12\x39\n\x06result\x18\x01 \x01(\x0b\x32\'.netspeak.service.SearchResponse.ResultH\x00\x12\x37\n\x05\x65rror\x18\x02 \x01(\x0b\x32&.netspeak.service.SearchResponse.ErrorH\x00\x1aJ\n\x06Result\x12)\n\x07phrases\x18\x01 \x03(\x0b\x32\x18.netspeak.service.Phrase\x12\x15\n\runknown_words\x18\x02 \x03(\t\x1a\xba\x01\n\x05\x45rror\x12\x39\n\x04kind\x18\x01 \x01(\x0e\x32+.netspeak.service.SearchResponse.Error.Kind\x12\x0f\n\x07message\x18\x02 \x01(\t\"e\n\x04Kind\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x15\n\x11INVALID_PARAMETER\x10\x64\x12\x11\n\rINVALID_QUERY\x10n\x12\x12\n\x0eINVALID_CORPUS\x10oB\n\n\x08response\"\x10\n\x0e\x43orporaRequest\"5\n\x06\x43orpus\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"<\n\x0f\x43orporaResponse\x12)\n\x07\x63orpora\x18\x01 \x03(\x0b\x32\x18.netspeak.service.Corpus2\xb1\x01\n\x0fNetspeakService\x12K\n\x06Search\x12\x1f.netspeak.service.SearchRequest\x1a .netspeak.service.SearchResponse\x12Q\n\nGetCorpora\x12 .netspeak.service.CorporaRequest\x1a!.netspeak.service.CorporaResponseB\x18\n\x14org.netspeak.serviceH\x01\x62\x06proto3'
)



_PHRASE_WORD_TAG = _descriptor.EnumDescriptor(
  name='Tag',
  full_name='netspeak.service.Phrase.Word.Tag',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_FOR_QMARK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_FOR_STAR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_IN_DICTSET', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_IN_ORDERSET', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_IN_OPTIONSET', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_FOR_PLUS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORD_FOR_REGEX', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=420,
  serialized_end=579,
)
_sym_db.RegisterEnumDescriptor(_PHRASE_WORD_TAG)

_SEARCHRESPONSE_ERROR_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='netspeak.service.SearchResponse.Error.Kind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARAMETER', index=2, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_QUERY', index=3, number=110,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CORPUS', index=4, number=111,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=878,
  serialized_end=979,
)
_sym_db.RegisterEnumDescriptor(_SEARCHRESPONSE_ERROR_KIND)


_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='netspeak.service.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='netspeak.service.SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='corpus', full_name='netspeak.service.SearchRequest.corpus', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_phrases', full_name='netspeak.service.SearchRequest.max_phrases', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phrase_constraints', full_name='netspeak.service.SearchRequest.phrase_constraints', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=44,
  serialized_end=176,
)


_PHRASECONSTRAINTS = _descriptor.Descriptor(
  name='PhraseConstraints',
  full_name='netspeak.service.PhraseConstraints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequency_max', full_name='netspeak.service.PhraseConstraints.frequency_max', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words_min', full_name='netspeak.service.PhraseConstraints.words_min', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words_max', full_name='netspeak.service.PhraseConstraints.words_max', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=178,
  serialized_end=258,
)


_PHRASE_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='netspeak.service.Phrase.Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='netspeak.service.Phrase.Word.tag', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='netspeak.service.Phrase.Word.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PHRASE_WORD_TAG,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=579,
)

_PHRASE = _descriptor.Descriptor(
  name='Phrase',
  full_name='netspeak.service.Phrase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='netspeak.service.Phrase.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='netspeak.service.Phrase.frequency', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words', full_name='netspeak.service.Phrase.words', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PHRASE_WORD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=579,
)


_SEARCHRESPONSE_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='netspeak.service.SearchResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phrases', full_name='netspeak.service.SearchResponse.Result.phrases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unknown_words', full_name='netspeak.service.SearchResponse.Result.unknown_words', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=716,
  serialized_end=790,
)

_SEARCHRESPONSE_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='netspeak.service.SearchResponse.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='netspeak.service.SearchResponse.Error.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='netspeak.service.SearchResponse.Error.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEARCHRESPONSE_ERROR_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=793,
  serialized_end=979,
)

_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='netspeak.service.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='netspeak.service.SearchResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='netspeak.service.SearchResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_RESULT, _SEARCHRESPONSE_ERROR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='netspeak.service.SearchResponse.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=582,
  serialized_end=991,
)


_CORPORAREQUEST = _descriptor.Descriptor(
  name='CorporaRequest',
  full_name='netspeak.service.CorporaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=993,
  serialized_end=1009,
)


_CORPUS = _descriptor.Descriptor(
  name='Corpus',
  full_name='netspeak.service.Corpus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='netspeak.service.Corpus.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='netspeak.service.Corpus.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='netspeak.service.Corpus.language', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1011,
  serialized_end=1064,
)


_CORPORARESPONSE = _descriptor.Descriptor(
  name='CorporaResponse',
  full_name='netspeak.service.CorporaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='corpora', full_name='netspeak.service.CorporaResponse.corpora', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1066,
  serialized_end=1126,
)

_SEARCHREQUEST.fields_by_name['phrase_constraints'].message_type = _PHRASECONSTRAINTS
_PHRASE_WORD.fields_by_name['tag'].enum_type = _PHRASE_WORD_TAG
_PHRASE_WORD.containing_type = _PHRASE
_PHRASE_WORD_TAG.containing_type = _PHRASE_WORD
_PHRASE.fields_by_name['words'].message_type = _PHRASE_WORD
_SEARCHRESPONSE_RESULT.fields_by_name['phrases'].message_type = _PHRASE
_SEARCHRESPONSE_RESULT.containing_type = _SEARCHRESPONSE
_SEARCHRESPONSE_ERROR.fields_by_name['kind'].enum_type = _SEARCHRESPONSE_ERROR_KIND
_SEARCHRESPONSE_ERROR.containing_type = _SEARCHRESPONSE
_SEARCHRESPONSE_ERROR_KIND.containing_type = _SEARCHRESPONSE_ERROR
_SEARCHRESPONSE.fields_by_name['result'].message_type = _SEARCHRESPONSE_RESULT
_SEARCHRESPONSE.fields_by_name['error'].message_type = _SEARCHRESPONSE_ERROR
_SEARCHRESPONSE.oneofs_by_name['response'].fields.append(
  _SEARCHRESPONSE.fields_by_name['result'])
_SEARCHRESPONSE.fields_by_name['result'].containing_oneof = _SEARCHRESPONSE.oneofs_by_name['response']
_SEARCHRESPONSE.oneofs_by_name['response'].fields.append(
  _SEARCHRESPONSE.fields_by_name['error'])
_SEARCHRESPONSE.fields_by_name['error'].containing_oneof = _SEARCHRESPONSE.oneofs_by_name['response']
_CORPORARESPONSE.fields_by_name['corpora'].message_type = _CORPUS
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['PhraseConstraints'] = _PHRASECONSTRAINTS
DESCRIPTOR.message_types_by_name['Phrase'] = _PHRASE
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['CorporaRequest'] = _CORPORAREQUEST
DESCRIPTOR.message_types_by_name['Corpus'] = _CORPUS
DESCRIPTOR.message_types_by_name['CorporaResponse'] = _CORPORARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

PhraseConstraints = _reflection.GeneratedProtocolMessageType('PhraseConstraints', (_message.Message,), {
  'DESCRIPTOR' : _PHRASECONSTRAINTS,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.PhraseConstraints)
  })
_sym_db.RegisterMessage(PhraseConstraints)

Phrase = _reflection.GeneratedProtocolMessageType('Phrase', (_message.Message,), {

  'Word' : _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
    'DESCRIPTOR' : _PHRASE_WORD,
    '__module__' : 'NetspeakService_pb2'
    # @@protoc_insertion_point(class_scope:netspeak.service.Phrase.Word)
    })
  ,
  'DESCRIPTOR' : _PHRASE,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.Phrase)
  })
_sym_db.RegisterMessage(Phrase)
_sym_db.RegisterMessage(Phrase.Word)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _SEARCHRESPONSE_RESULT,
    '__module__' : 'NetspeakService_pb2'
    # @@protoc_insertion_point(class_scope:netspeak.service.SearchResponse.Result)
    })
  ,

  'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
    'DESCRIPTOR' : _SEARCHRESPONSE_ERROR,
    '__module__' : 'NetspeakService_pb2'
    # @@protoc_insertion_point(class_scope:netspeak.service.SearchResponse.Error)
    })
  ,
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)
_sym_db.RegisterMessage(SearchResponse.Result)
_sym_db.RegisterMessage(SearchResponse.Error)

CorporaRequest = _reflection.GeneratedProtocolMessageType('CorporaRequest', (_message.Message,), {
  'DESCRIPTOR' : _CORPORAREQUEST,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.CorporaRequest)
  })
_sym_db.RegisterMessage(CorporaRequest)

Corpus = _reflection.GeneratedProtocolMessageType('Corpus', (_message.Message,), {
  'DESCRIPTOR' : _CORPUS,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.Corpus)
  })
_sym_db.RegisterMessage(Corpus)

CorporaResponse = _reflection.GeneratedProtocolMessageType('CorporaResponse', (_message.Message,), {
  'DESCRIPTOR' : _CORPORARESPONSE,
  '__module__' : 'NetspeakService_pb2'
  # @@protoc_insertion_point(class_scope:netspeak.service.CorporaResponse)
  })
_sym_db.RegisterMessage(CorporaResponse)


DESCRIPTOR._options = None

_NETSPEAKSERVICE = _descriptor.ServiceDescriptor(
  name='NetspeakService',
  full_name='netspeak.service.NetspeakService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1129,
  serialized_end=1306,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='netspeak.service.NetspeakService.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCorpora',
    full_name='netspeak.service.NetspeakService.GetCorpora',
    index=1,
    containing_service=None,
    input_type=_CORPORAREQUEST,
    output_type=_CORPORARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETSPEAKSERVICE)

DESCRIPTOR.services_by_name['NetspeakService'] = _NETSPEAKSERVICE

# @@protoc_insertion_point(module_scope)
