import math
import mongoengine


class QuerySet(mongoengine.QuerySet):
  LIMIT = 10

  def set_page_limit(self, value):
    QuerySet.LIMIT = value

  def page(self, page=1):
    if not page >= 1:
      raise ValueError('Page number should be a Natural number.')
    skip = (page - 1) * self.LIMIT
    return self.skip(skip).limit(self.LIMIT)

  @property
  def page_count(self):
    return math.ceil(self.count() / self.LIMIT)
