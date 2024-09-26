from __future__ import annotations
from pycore.base import AbstractData


class Vol(AbstractData):

  default_instance: Vol

  _k_0 = "width"
  _k_1 = "height"
  _k_2 = "depth"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = 0
    self._2 = 0

  @classmethod
  def new_builder(cls) -> VolBuilder:
    return VolBuilder()

  def parse(self, obj: dict) -> Vol:
    inst = Vol()
    inst._0 = obj.get(Vol._k_0, 0)
    inst._1 = obj.get(Vol._k_1, 0)
    inst._2 = obj.get(Vol._k_2, 0)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  width = property(_g0)
  height = property(_g1)
  depth = property(_g2)

  def to_builder(self) -> VolBuilder:
    x = VolBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    return x

  def to_json(self) -> dict:
    m = {}
    m[Vol._k_0] = self._0
    m[Vol._k_1] = self._1
    m[Vol._k_2] = self._2
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, Vol):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2
    else:
      return False


Vol.default_instance = Vol()


class VolBuilder(Vol):

  def set_width(self, x: int) -> VolBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_height(self, x: int) -> VolBuilder:
    self._1 = 0 if x is None else x
    return self

  def set_depth(self, x: int) -> VolBuilder:
    self._2 = 0 if x is None else x
    return self

  width = property(Vol._g0, set_width)
  height = property(Vol._g1, set_height)
  depth = property(Vol._g2, set_depth)

  def to_builder(self) -> VolBuilder:
    return self

  def build(self) -> Vol:
    v = Vol()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    return v
