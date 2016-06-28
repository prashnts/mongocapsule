import mongoengine
from .queryset import QuerySet


class Document(mongoengine.Document):
  meta = {
    'abstract': True,
    'queryset_class': QuerySet
  }


class DynamicDocument(mongoengine.DynamicDocument):
  meta = {
    'abstract': True,
    'queryset_class': QuerySet
  }
