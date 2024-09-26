from __future__ import annotations
from pycore.base import AbstractData


class TensorStats(AbstractData):

  default_instance: TensorStats

  _k_0 = "population"
  _k_1 = "min"
  _k_2 = "max"
  _k_3 = "mean"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = 0.0
    self._2 = 0.0
    self._3 = 0.0

  @classmethod
  def new_builder(cls) -> TensorStatsBuilder:
    return TensorStatsBuilder()

  def parse(self, obj: dict) -> TensorStats:
    inst = TensorStats()
    inst._0 = obj.get(TensorStats._k_0, 0)
    inst._1 = obj.get(TensorStats._k_1, 0.0)
    inst._2 = obj.get(TensorStats._k_2, 0.0)
    inst._3 = obj.get(TensorStats._k_3, 0.0)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> float:
    return self._1

  def _g2(self) -> float:
    return self._2

  def _g3(self) -> float:
    return self._3

  population = property(_g0)
  min = property(_g1)
  max = property(_g2)
  mean = property(_g3)

  def to_builder(self) -> TensorStatsBuilder:
    x = TensorStatsBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    return x

  def to_json(self) -> dict:
    m = {}
    m[TensorStats._k_0] = self._0
    m[TensorStats._k_1] = self._1
    m[TensorStats._k_2] = self._2
    m[TensorStats._k_3] = self._3
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
    if isinstance(other, TensorStats):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2\
        and self._3 == other._3
    else:
      return False


TensorStats.default_instance = TensorStats()


class TensorStatsBuilder(TensorStats):

  def set_population(self, x: int) -> TensorStatsBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_min(self, x: float) -> TensorStatsBuilder:
    self._1 = 0.0 if x is None else x
    return self

  def set_max(self, x: float) -> TensorStatsBuilder:
    self._2 = 0.0 if x is None else x
    return self

  def set_mean(self, x: float) -> TensorStatsBuilder:
    self._3 = 0.0 if x is None else x
    return self

  population = property(TensorStats._g0, set_population)
  min = property(TensorStats._g1, set_min)
  max = property(TensorStats._g2, set_max)
  mean = property(TensorStats._g3, set_mean)

  def to_builder(self) -> TensorStatsBuilder:
    return self

  def build(self) -> TensorStats:
    v = TensorStats()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    return v
