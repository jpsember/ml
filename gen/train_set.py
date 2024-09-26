from __future__ import annotations
from pycore.base import AbstractData


class TrainSet(AbstractData):

  default_instance: TrainSet

  _k_0 = "used"
  _k_1 = "directory"
  _k_2 = "id"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = ""
    self._2 = 0

  @classmethod
  def new_builder(cls) -> TrainSetBuilder:
    return TrainSetBuilder()

  def parse(self, obj: dict) -> TrainSet:
    inst = TrainSet()
    inst._0 = obj.get(TrainSet._k_0, 0)
    inst._1 = obj.get(TrainSet._k_1, "")
    inst._2 = obj.get(TrainSet._k_2, 0)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> str:
    return self._1

  def _g2(self) -> int:
    return self._2

  used = property(_g0)
  directory = property(_g1)
  id = property(_g2)

  def to_builder(self) -> TrainSetBuilder:
    x = TrainSetBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    return x

  def to_json(self) -> dict:
    m = {}
    m[TrainSet._k_0] = self._0
    m[TrainSet._k_1] = self._1
    m[TrainSet._k_2] = self._2
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, TrainSet):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2
    else:
      return False


TrainSet.default_instance = TrainSet()


class TrainSetBuilder(TrainSet):

  def set_used(self, x: int) -> TrainSetBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_directory(self, x: str) -> TrainSetBuilder:
    self._1 = "" if x is None else x
    return self

  def set_id(self, x: int) -> TrainSetBuilder:
    self._2 = 0 if x is None else x
    return self

  used = property(TrainSet._g0, set_used)
  directory = property(TrainSet._g1, set_directory)
  id = property(TrainSet._g2, set_id)

  def to_builder(self) -> TrainSetBuilder:
    return self

  def build(self) -> TrainSet:
    v = TrainSet()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    return v
