from __future__ import annotations
from pycore.base import AbstractData


class FeedConfig(AbstractData):

  default_instance: FeedConfig

  _k_0 = "alg"
  _k_1 = "produce_time_ms"
  _k_2 = "consume_time_ms"
  _k_3 = "produce_set_size"
  _k_4 = "consume_set_size"
  _k_5 = "recycle"
  _k_6 = "obj_consumed_total"
  _k_7 = "seed"

  def __init__(self):
    self._h = None
    self._0 = 1
    self._1 = 1200
    self._2 = 500
    self._3 = 3
    self._4 = 2
    self._5 = 3
    self._6 = 80
    self._7 = 1965

  @classmethod
  def new_builder(cls) -> FeedConfigBuilder:
    return FeedConfigBuilder()

  def parse(self, obj: dict) -> FeedConfig:
    inst = FeedConfig()
    inst._0 = obj.get(FeedConfig._k_0, 1)
    inst._1 = obj.get(FeedConfig._k_1, 1200)
    inst._2 = obj.get(FeedConfig._k_2, 500)
    inst._3 = obj.get(FeedConfig._k_3, 3)
    inst._4 = obj.get(FeedConfig._k_4, 2)
    inst._5 = obj.get(FeedConfig._k_5, 3)
    inst._6 = obj.get(FeedConfig._k_6, 80)
    inst._7 = obj.get(FeedConfig._k_7, 1965)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  def _g3(self) -> int:
    return self._3

  def _g4(self) -> int:
    return self._4

  def _g5(self) -> int:
    return self._5

  def _g6(self) -> int:
    return self._6

  def _g7(self) -> int:
    return self._7

  alg = property(_g0)
  produce_time_ms = property(_g1)
  consume_time_ms = property(_g2)
  produce_set_size = property(_g3)
  consume_set_size = property(_g4)
  recycle = property(_g5)
  obj_consumed_total = property(_g6)
  seed = property(_g7)

  def to_builder(self) -> FeedConfigBuilder:
    x = FeedConfigBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    x._4 = self._4
    x._5 = self._5
    x._6 = self._6
    x._7 = self._7
    return x

  def to_json(self) -> dict:
    m = {}
    m[FeedConfig._k_0] = self._0
    m[FeedConfig._k_1] = self._1
    m[FeedConfig._k_2] = self._2
    m[FeedConfig._k_3] = self._3
    m[FeedConfig._k_4] = self._4
    m[FeedConfig._k_5] = self._5
    m[FeedConfig._k_6] = self._6
    m[FeedConfig._k_7] = self._7
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._3)
      r = r * 37 + hash(self._4)
      r = r * 37 + hash(self._5)
      r = r * 37 + hash(self._6)
      r = r * 37 + hash(self._7)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, FeedConfig):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2\
        and self._3 == other._3\
        and self._4 == other._4\
        and self._5 == other._5\
        and self._6 == other._6\
        and self._7 == other._7
    else:
      return False


FeedConfig.default_instance = FeedConfig()


class FeedConfigBuilder(FeedConfig):

  def set_alg(self, x: int) -> FeedConfigBuilder:
    self._0 = 1 if x is None else x
    return self

  def set_produce_time_ms(self, x: int) -> FeedConfigBuilder:
    self._1 = 1200 if x is None else x
    return self

  def set_consume_time_ms(self, x: int) -> FeedConfigBuilder:
    self._2 = 500 if x is None else x
    return self

  def set_produce_set_size(self, x: int) -> FeedConfigBuilder:
    self._3 = 3 if x is None else x
    return self

  def set_consume_set_size(self, x: int) -> FeedConfigBuilder:
    self._4 = 2 if x is None else x
    return self

  def set_recycle(self, x: int) -> FeedConfigBuilder:
    self._5 = 3 if x is None else x
    return self

  def set_obj_consumed_total(self, x: int) -> FeedConfigBuilder:
    self._6 = 80 if x is None else x
    return self

  def set_seed(self, x: int) -> FeedConfigBuilder:
    self._7 = 1965 if x is None else x
    return self

  alg = property(FeedConfig._g0, set_alg)
  produce_time_ms = property(FeedConfig._g1, set_produce_time_ms)
  consume_time_ms = property(FeedConfig._g2, set_consume_time_ms)
  produce_set_size = property(FeedConfig._g3, set_produce_set_size)
  consume_set_size = property(FeedConfig._g4, set_consume_set_size)
  recycle = property(FeedConfig._g5, set_recycle)
  obj_consumed_total = property(FeedConfig._g6, set_obj_consumed_total)
  seed = property(FeedConfig._g7, set_seed)

  def to_builder(self) -> FeedConfigBuilder:
    return self

  def build(self) -> FeedConfig:
    v = FeedConfig()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    v._4 = self._4
    v._5 = self._5
    v._6 = self._6
    v._7 = self._7
    return v
