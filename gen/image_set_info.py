from __future__ import annotations
from pycore.base import AbstractData


class ImageSetInfo(AbstractData):

  default_instance: ImageSetInfo

  _k_0 = "image_count"
  _k_1 = "image_length_bytes"
  _k_2 = "label_length_bytes"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = 0
    self._2 = 0

  @classmethod
  def new_builder(cls) -> ImageSetInfoBuilder:
    return ImageSetInfoBuilder()

  def parse(self, obj: dict) -> ImageSetInfo:
    inst = ImageSetInfo()
    inst._0 = obj.get(ImageSetInfo._k_0, 0)
    inst._1 = obj.get(ImageSetInfo._k_1, 0)
    inst._2 = obj.get(ImageSetInfo._k_2, 0)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  image_count = property(_g0)
  image_length_bytes = property(_g1)
  label_length_bytes = property(_g2)

  def to_builder(self) -> ImageSetInfoBuilder:
    x = ImageSetInfoBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    return x

  def to_json(self) -> dict:
    m = {}
    m[ImageSetInfo._k_0] = self._0
    m[ImageSetInfo._k_1] = self._1
    m[ImageSetInfo._k_2] = self._2
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, ImageSetInfo):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2
    else:
      return False


ImageSetInfo.default_instance = ImageSetInfo()


class ImageSetInfoBuilder(ImageSetInfo):

  def set_image_count(self, x: int) -> ImageSetInfoBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_image_length_bytes(self, x: int) -> ImageSetInfoBuilder:
    self._1 = 0 if x is None else x
    return self

  def set_label_length_bytes(self, x: int) -> ImageSetInfoBuilder:
    self._2 = 0 if x is None else x
    return self

  image_count = property(ImageSetInfo._g0, set_image_count)
  image_length_bytes = property(ImageSetInfo._g1, set_image_length_bytes)
  label_length_bytes = property(ImageSetInfo._g2, set_label_length_bytes)

  def to_builder(self) -> ImageSetInfoBuilder:
    return self

  def build(self) -> ImageSetInfo:
    v = ImageSetInfo()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    return v
