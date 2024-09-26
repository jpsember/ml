from __future__ import annotations
from pycore.base import AbstractData
from typing import List


class CmdItem(AbstractData):

  default_instance: CmdItem

  _k_0 = "id"
  _k_1 = "args"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = []

  @classmethod
  def new_builder(cls) -> CmdItemBuilder:
    return CmdItemBuilder()

  def parse(self, obj: dict) -> CmdItem:
    inst = CmdItem()
    inst._0 = obj.get(CmdItem._k_0, 0)
    x = obj.get(CmdItem._k_1, [])
    inst._1 = x.copy()
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> List[str]:
    return self._1

  id = property(_g0)
  args = property(_g1)

  def to_builder(self) -> CmdItemBuilder:
    x = CmdItemBuilder()
    x._0 = self._0
    x._1 = self._1.copy()
    return x

  def to_json(self) -> dict:
    m = {}
    m[CmdItem._k_0] = self._0
    m[CmdItem._k_1] = self._1.copy()
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      for x in self._1:
        r = r * 37 + hash(x)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, CmdItem):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1
    else:
      return False


CmdItem.default_instance = CmdItem()


class CmdItemBuilder(CmdItem):

  def set_id(self, x: int) -> CmdItemBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_args(self, x: List[str]) -> CmdItemBuilder:
    self._1 = [] if x is None else x.copy()
    return self

  id = property(CmdItem._g0, set_id)
  args = property(CmdItem._g1, set_args)

  def to_builder(self) -> CmdItemBuilder:
    return self

  def build(self) -> CmdItem:
    v = CmdItem()
    v._0 = self._0
    v._1 = self._1.copy()
    return v
