from __future__ import annotations
from pycore.base import AbstractData


class DescribeNetworkConfig(AbstractData):

  default_instance: DescribeNetworkConfig

  _k_0 = "path"
  _k_1 = "max_size_mb"

  def __init__(self):
    self._h = None
    self._0 = "network.json"
    self._1 = 300

  @classmethod
  def new_builder(cls) -> DescribeNetworkConfigBuilder:
    return DescribeNetworkConfigBuilder()

  def parse(self, obj: dict) -> DescribeNetworkConfig:
    inst = DescribeNetworkConfig()
    inst._0 = obj.get(DescribeNetworkConfig._k_0, "network.json")
    inst._1 = obj.get(DescribeNetworkConfig._k_1, 300)
    return inst

  def _g0(self) -> str:
    return self._0

  def _g1(self) -> int:
    return self._1

  path = property(_g0)
  max_size_mb = property(_g1)

  def to_builder(self) -> DescribeNetworkConfigBuilder:
    x = DescribeNetworkConfigBuilder()
    x._0 = self._0
    x._1 = self._1
    return x

  def to_json(self) -> dict:
    m = {}
    m[DescribeNetworkConfig._k_0] = self._0
    m[DescribeNetworkConfig._k_1] = self._1
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, DescribeNetworkConfig):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1
    else:
      return False


DescribeNetworkConfig.default_instance = DescribeNetworkConfig()


class DescribeNetworkConfigBuilder(DescribeNetworkConfig):

  def set_path(self, x: str) -> DescribeNetworkConfigBuilder:
    self._0 = "network.json" if x is None else x
    return self

  def set_max_size_mb(self, x: int) -> DescribeNetworkConfigBuilder:
    self._1 = 300 if x is None else x
    return self

  path = property(DescribeNetworkConfig._g0, set_path)
  max_size_mb = property(DescribeNetworkConfig._g1, set_max_size_mb)

  def to_builder(self) -> DescribeNetworkConfigBuilder:
    return self

  def build(self) -> DescribeNetworkConfig:
    v = DescribeNetworkConfig()
    v._0 = self._0
    v._1 = self._1
    return v
