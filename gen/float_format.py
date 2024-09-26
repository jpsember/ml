from __future__ import annotations
from pycore.base import AbstractData


class FloatFormat(AbstractData):

  default_instance: FloatFormat

  _k_0 = "format_str"
  _k_1 = "max_value"
  _k_2 = "min_value"
  _k_3 = "zero_str"

  def __init__(self):
    self._h = None
    self._0 = ""
    self._1 = 0.0
    self._2 = 0.0
    self._3 = ""

  @classmethod
  def new_builder(cls) -> FloatFormatBuilder:
    return FloatFormatBuilder()

  def parse(self, obj: dict) -> FloatFormat:
    inst = FloatFormat()
    inst._0 = obj.get(FloatFormat._k_0, "")
    inst._1 = obj.get(FloatFormat._k_1, 0.0)
    inst._2 = obj.get(FloatFormat._k_2, 0.0)
    inst._3 = obj.get(FloatFormat._k_3, "")
    return inst

  def _g0(self) -> str:
    return self._0

  def _g1(self) -> float:
    return self._1

  def _g2(self) -> float:
    return self._2

  def _g3(self) -> str:
    return self._3

  format_str = property(_g0)
  max_value = property(_g1)
  min_value = property(_g2)
  zero_str = property(_g3)

  def to_builder(self) -> FloatFormatBuilder:
    x = FloatFormatBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    return x

  def to_json(self) -> dict:
    m = {}
    m[FloatFormat._k_0] = self._0
    m[FloatFormat._k_1] = self._1
    m[FloatFormat._k_2] = self._2
    m[FloatFormat._k_3] = self._3
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._3)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, FloatFormat):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2\
        and self._3 == other._3
    else:
      return False


FloatFormat.default_instance = FloatFormat()


class FloatFormatBuilder(FloatFormat):

  def set_format_str(self, x: str) -> FloatFormatBuilder:
    self._0 = "" if x is None else x
    return self

  def set_max_value(self, x: float) -> FloatFormatBuilder:
    self._1 = 0.0 if x is None else x
    return self

  def set_min_value(self, x: float) -> FloatFormatBuilder:
    self._2 = 0.0 if x is None else x
    return self

  def set_zero_str(self, x: str) -> FloatFormatBuilder:
    self._3 = "" if x is None else x
    return self

  format_str = property(FloatFormat._g0, set_format_str)
  max_value = property(FloatFormat._g1, set_max_value)
  min_value = property(FloatFormat._g2, set_min_value)
  zero_str = property(FloatFormat._g3, set_zero_str)

  def to_builder(self) -> FloatFormatBuilder:
    return self

  def build(self) -> FloatFormat:
    v = FloatFormat()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    return v
