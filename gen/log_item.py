from __future__ import annotations
from gen.special_handling import SpecialHandling
from pycore.base import AbstractData
from typing import List


class LogItem(AbstractData):

  default_instance: LogItem

  _k_0 = "id"
  _k_1 = "family_size"
  _k_2 = "family_slot"
  _k_3 = "family_id"
  _k_4 = "message"
  _k_5 = "shape"
  _k_6 = "tensor_bytes"
  _k_7 = "tensor_floats"
  _k_8 = "stats"
  _k_9 = "special_handling"
  _k_10 = "illegal_values_found"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = 0
    self._2 = 0
    self._3 = 0
    self._4 = ""
    self._5 = []
    self._6 = None
    self._7 = None
    self._8 = None
    self._9 = SpecialHandling.default_instance
    self._10 = False

  @classmethod
  def new_builder(cls) -> LogItemBuilder:
    return LogItemBuilder()

  def parse(self, obj: dict) -> LogItem:
    inst = LogItem()
    inst._0 = obj.get(LogItem._k_0, 0)
    inst._1 = obj.get(LogItem._k_1, 0)
    inst._2 = obj.get(LogItem._k_2, 0)
    inst._3 = obj.get(LogItem._k_3, 0)
    inst._4 = obj.get(LogItem._k_4, "")
    inst._5 = obj.get(LogItem._k_5, []).copy()
    x = obj.get(LogItem._k_6, None)
    if x is not None:
      inst._6 = x.copy()
    x = obj.get(LogItem._k_7, None)
    if x is not None:
      inst._7 = x.copy()
    inst._8 = obj.get(LogItem._k_8, None)
    x = obj.get(LogItem._k_9, SpecialHandling.default_instance)
    inst._9 = x
    inst._10 = obj.get(LogItem._k_10, False)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  def _g3(self) -> int:
    return self._3

  def _g4(self) -> str:
    return self._4

  def _g5(self) -> List[int]:
    return self._5

  def _g6(self) -> List[int]:
    return self._6

  def _g7(self) -> List[float]:
    return self._7

  def _g8(self) -> dict:
    return self._8

  def _g9(self) -> SpecialHandling:
    return self._9

  def _g10(self) -> bool:
    return self._10

  id = property(_g0)
  family_size = property(_g1)
  family_slot = property(_g2)
  family_id = property(_g3)
  message = property(_g4)
  shape = property(_g5)
  tensor_bytes = property(_g6)
  tensor_floats = property(_g7)
  stats = property(_g8)
  special_handling = property(_g9)
  illegal_values_found = property(_g10)

  def to_builder(self) -> LogItemBuilder:
    x = LogItemBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    x._4 = self._4
    x._5 = self._5.copy()
    if self._6 is not None:
      x._6 = self._6.copy()
    if self._7 is not None:
      x._7 = self._7.copy()
    x._8 = self._8
    x._9 = self._9
    x._10 = self._10
    return x

  def to_json(self) -> dict:
    m = {}
    m[LogItem._k_0] = self._0
    m[LogItem._k_1] = self._1
    m[LogItem._k_2] = self._2
    m[LogItem._k_3] = self._3
    m[LogItem._k_4] = self._4
    m[LogItem._k_5] = self._5.copy()
    if self._6 is not None:
      m[LogItem._k_6] = self._6.copy()
    if self._7 is not None:
      m[LogItem._k_7] = self._7.copy()
    if self._8 is not None:
      m[LogItem._k_8] = self._8
    m[LogItem._k_9] = self._9
    m[LogItem._k_10] = self._10
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._3)
      r = r * 37 + hash(self._4)
      for x in self._5:
        r = r * 37 + hash(x)
      r = r * 37 + hash(self._9)
      r = r * 37 + hash(self._10)
      if self._6 is not None:
        for x in self._6:
          r = r * 37 + hash(x)
      if self._7 is not None:
        for x in self._7:
          r = r * 37 + hash(x)
      r = r * 37 + hash(self._8)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, LogItem):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2\
        and self._3 == other._3\
        and self._4 == other._4\
        and self._5 == other._5\
        and self._6 == other._6\
        and self._7 == other._7\
        and self._8 == other._8\
        and self._9 == other._9\
        and self._10 == other._10
    else:
      return False


LogItem.default_instance = LogItem()


class LogItemBuilder(LogItem):

  def set_id(self, x: int) -> LogItemBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_family_size(self, x: int) -> LogItemBuilder:
    self._1 = 0 if x is None else x
    return self

  def set_family_slot(self, x: int) -> LogItemBuilder:
    self._2 = 0 if x is None else x
    return self

  def set_family_id(self, x: int) -> LogItemBuilder:
    self._3 = 0 if x is None else x
    return self

  def set_message(self, x: str) -> LogItemBuilder:
    self._4 = "" if x is None else x
    return self

  def set_shape(self, x: List[int]) -> LogItemBuilder:
    self._5 = [] if x is None else x.copy()
    return self

  def set_tensor_bytes(self, x: List[int]) -> LogItemBuilder:
    self._6 = x if x is None else x.copy()
    return self

  def set_tensor_floats(self, x: List[float]) -> LogItemBuilder:
    self._7 = x if x is None else x.copy()
    return self

  def set_stats(self, x: dict) -> LogItemBuilder:
    self._8 = x
    return self

  def set_special_handling(self, x: SpecialHandling) -> LogItemBuilder:
    self._9 = SpecialHandling.default_instance if x is None else x
    return self

  def set_illegal_values_found(self, x: bool) -> LogItemBuilder:
    self._10 = False if x is None else x
    return self

  id = property(LogItem._g0, set_id)
  family_size = property(LogItem._g1, set_family_size)
  family_slot = property(LogItem._g2, set_family_slot)
  family_id = property(LogItem._g3, set_family_id)
  message = property(LogItem._g4, set_message)
  shape = property(LogItem._g5, set_shape)
  tensor_bytes = property(LogItem._g6, set_tensor_bytes)
  tensor_floats = property(LogItem._g7, set_tensor_floats)
  stats = property(LogItem._g8, set_stats)
  special_handling = property(LogItem._g9, set_special_handling)
  illegal_values_found = property(LogItem._g10, set_illegal_values_found)

  def to_builder(self) -> LogItemBuilder:
    return self

  def build(self) -> LogItem:
    v = LogItem()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    v._4 = self._4
    v._5 = self._5.copy()
    x = self._6
    v._6 = x if x is None else x.copy()
    x = self._7
    v._7 = x if x is None else x.copy()
    v._8 = self._8
    v._9 = self._9
    v._10 = self._10
    return v
