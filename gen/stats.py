from __future__ import annotations
from pycore.base import AbstractData


class Stats(AbstractData):

  default_instance: Stats

  _k_0 = "train_count"
  _k_1 = "test_count"
  _k_2 = "mean"
  _k_3 = "standard_deviation"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = 0
    self._2 = 0.0
    self._3 = 0.0

  @classmethod
  def new_builder(cls) -> StatsBuilder:
    return StatsBuilder()

  def parse(self, obj: dict) -> Stats:
    inst = Stats()
    inst._0 = obj.get(Stats._k_0, 0)
    inst._1 = obj.get(Stats._k_1, 0)
    inst._2 = obj.get(Stats._k_2, 0.0)
    inst._3 = obj.get(Stats._k_3, 0.0)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> float:
    return self._2

  def _g3(self) -> float:
    return self._3

  train_count = property(_g0)
  test_count = property(_g1)
  mean = property(_g2)
  standard_deviation = property(_g3)

  def to_builder(self) -> StatsBuilder:
    x = StatsBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    return x

  def to_json(self) -> dict:
    m = {}
    m[Stats._k_0] = self._0
    m[Stats._k_1] = self._1
    m[Stats._k_2] = self._2
    m[Stats._k_3] = self._3
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
    if isinstance(other, Stats):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2\
        and self._3 == other._3
    else:
      return False


Stats.default_instance = Stats()


class StatsBuilder(Stats):

  def set_train_count(self, x: int) -> StatsBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_test_count(self, x: int) -> StatsBuilder:
    self._1 = 0 if x is None else x
    return self

  def set_mean(self, x: float) -> StatsBuilder:
    self._2 = 0.0 if x is None else x
    return self

  def set_standard_deviation(self, x: float) -> StatsBuilder:
    self._3 = 0.0 if x is None else x
    return self

  train_count = property(Stats._g0, set_train_count)
  test_count = property(Stats._g1, set_test_count)
  mean = property(Stats._g2, set_mean)
  standard_deviation = property(Stats._g3, set_standard_deviation)

  def to_builder(self) -> StatsBuilder:
    return self

  def build(self) -> Stats:
    v = Stats()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    return v
