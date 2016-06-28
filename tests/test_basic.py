import nose

from mongocapsule import MongoCapsule


class TestCapsule:
  def __init__(self):
    self.db = MongoCapsule('test', host='mongomock://localhost')
    self.set_up(self.db)

  def set_up(self, db):
    class Doc(db.Document):
      val = db.StringField()

    self.Doc = Doc

  def test_basic(self):
    self.Doc.drop_collection()
    obj = self.Doc(val='test')
    obj.save()

    obj_test = self.Doc.objects.get()

    assert obj_test.val == 'test'

  def test_paginate(self):
    self.Doc.drop_collection()
    for i in range(100):
      self.Doc(val=str(i)).save()

    for i, doc in enumerate(self.Doc.objects.page()):
      assert doc.val == str(i)

    for i, doc in enumerate(self.Doc.objects.page(2)):
      assert doc.val == str(i + 10)

  @nose.tools.raises(ValueError)
  def test_exceptions(self):
    self.Doc.objects.page(0)

  def test_update_page_limit(self):
    self.Doc.drop_collection()

    for i in range(100):
      self.Doc(val=str(i)).save()

    assert self.Doc.objects.page_count == 10

    self.Doc.objects.set_page_limit(20)

    assert self.Doc.objects.page_count == 5


