from __future__ import annotations
from pycore.base import AbstractData
from pycore.ipoint import IPoint


class Classifier(AbstractData):

  default_instance: Classifier

  _k_0 = "image_size"
  _k_1 = "image_channels"
  _k_2 = "category_count"

  def __init__(self):
    self._h = None
    self._0 = IPoint.default_instance
    self._1 = 0
    self._2 = 0

  @classmethod
  def new_builder(cls) -> ClassifierBuilder:
    return ClassifierBuilder()

  def parse(self, obj: dict) -> Classifier:
    inst = Classifier()
    x = obj.get(Classifier._k_0)
    if x is not None:
      inst._0 = IPoint.default_instance.parse(x)
    inst._1 = obj.get(Classifier._k_1, 0)
    inst._2 = obj.get(Classifier._k_2, 0)
    return inst

  def _g0(self) -> IPoint:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  image_size = property(_g0)
  image_channels = property(_g1)
  category_count = property(_g2)

  def to_builder(self) -> ClassifierBuilder:
    x = ClassifierBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    return x

  def to_json(self) -> dict:
    m = {}
    m[Classifier._k_0] = self._0.to_json()
    m[Classifier._k_1] = self._1
    m[Classifier._k_2] = self._2
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, Classifier):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2
    else:
      return False


Classifier.default_instance = Classifier()


class ClassifierBuilder(Classifier):

  def set_image_size(self, x: IPoint) -> ClassifierBuilder:
    if x is None:
      x = IPoint.default_instance
    self._0 = x.build()
    return self

  def set_image_channels(self, x: int) -> ClassifierBuilder:
    self._1 = 0 if x is None else x
    return self

  def set_category_count(self, x: int) -> ClassifierBuilder:
    self._2 = 0 if x is None else x
    return self

  image_size = property(Classifier._g0, set_image_size)
  image_channels = property(Classifier._g1, set_image_channels)
  category_count = property(Classifier._g2, set_category_count)

  def to_builder(self) -> ClassifierBuilder:
    return self

  def build(self) -> Classifier:
    v = Classifier()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    return v
