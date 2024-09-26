from __future__ import annotations
from pycore.base import AbstractData


class NetworkOptions(AbstractData):

  default_instance: NetworkOptions

  _k_0 = "confidence_pct"
  _k_1 = "max_i_over_u"

  def __init__(self):
    self._h = None
    self._0 = 65.0
    self._1 = 0.4

  @classmethod
  def new_builder(cls) -> NetworkOptionsBuilder:
    return NetworkOptionsBuilder()

  def parse(self, obj: dict) -> NetworkOptions:
    inst = NetworkOptions()
    inst._0 = obj.get(NetworkOptions._k_0, 65.0)
    inst._1 = obj.get(NetworkOptions._k_1, 0.4)
    return inst

  def _g0(self) -> float:
    return self._0

  def _g1(self) -> float:
    return self._1

  confidence_pct = property(_g0)
  max_i_over_u = property(_g1)

  def to_builder(self) -> NetworkOptionsBuilder:
    x = NetworkOptionsBuilder()
    x._0 = self._0
    x._1 = self._1
    return x

  def to_json(self) -> dict:
    m = {}
    m[NetworkOptions._k_0] = self._0
    m[NetworkOptions._k_1] = self._1
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, NetworkOptions):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1
    else:
      return False


NetworkOptions.default_instance = NetworkOptions()


class NetworkOptionsBuilder(NetworkOptions):

  def set_confidence_pct(self, x: float) -> NetworkOptionsBuilder:
    self._0 = 65.0 if x is None else x
    return self

  def set_max_i_over_u(self, x: float) -> NetworkOptionsBuilder:
    self._1 = 0.4 if x is None else x
    return self

  confidence_pct = property(NetworkOptions._g0, set_confidence_pct)
  max_i_over_u = property(NetworkOptions._g1, set_max_i_over_u)

  def to_builder(self) -> NetworkOptionsBuilder:
    return self

  def build(self) -> NetworkOptions:
    v = NetworkOptions()
    v._0 = self._0
    v._1 = self._1
    return v
