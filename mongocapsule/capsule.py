import mongoengine
from .documents import Document, DynamicDocument


class MongoCapsule(object):
  def __init__(self, db, **kwa):
    self.__include_mongoengine__()
    self.connection = mongoengine.connect(db, **kwa)
    self.Document = Document
    self.DynamicDocument = DynamicDocument

  def __include_mongoengine__(self):
    for module in mongoengine, mongoengine.fields:
      for key in module.__all__:
        if not hasattr(self, key):
          setattr(self, key, getattr(module, key))
