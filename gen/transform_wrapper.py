from __future__ import annotations
from pycore.base import AbstractData
from pycore.matrix import Matrix


class TransformWrapper(AbstractData):

  default_instance: TransformWrapper

  _k_0 = "matrix"
  _k_1 = "inverse"
  _k_2 = "rotation_degrees"

  def __init__(self):
    self._h = None
    self._0 = Matrix.default_instance
    self._1 = Matrix.default_instance
    self._2 = 0

  @classmethod
  def new_builder(cls) -> TransformWrapperBuilder:
    return TransformWrapperBuilder()

  def parse(self, obj: dict) -> TransformWrapper:
    inst = TransformWrapper()
    x = obj.get(TransformWrapper._k_0)
    if x is not None:
      inst._0 = Matrix.default_instance.parse(x)
    x = obj.get(TransformWrapper._k_1)
    if x is not None:
      inst._1 = Matrix.default_instance.parse(x)
    inst._2 = obj.get(TransformWrapper._k_2, 0)
    return inst

  def _g0(self) -> Matrix:
    return self._0

  def _g1(self) -> Matrix:
    return self._1

  def _g2(self) -> int:
    return self._2

  matrix = property(_g0)
  inverse = property(_g1)
  rotation_degrees = property(_g2)

  def to_builder(self) -> TransformWrapperBuilder:
    x = TransformWrapperBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    return x

  def to_json(self) -> dict:
    m = {}
    m[TransformWrapper._k_0] = self._0.to_json()
    m[TransformWrapper._k_1] = self._1.to_json()
    m[TransformWrapper._k_2] = self._2
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, TransformWrapper):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2
    else:
      return False


TransformWrapper.default_instance = TransformWrapper()


class TransformWrapperBuilder(TransformWrapper):

  def set_matrix(self, x: Matrix) -> TransformWrapperBuilder:
    if x is None:
      x = Matrix.default_instance
    self._0 = x.build()
    return self

  def set_inverse(self, x: Matrix) -> TransformWrapperBuilder:
    if x is None:
      x = Matrix.default_instance
    self._1 = x.build()
    return self

  def set_rotation_degrees(self, x: int) -> TransformWrapperBuilder:
    self._2 = 0 if x is None else x
    return self

  matrix = property(TransformWrapper._g0, set_matrix)
  inverse = property(TransformWrapper._g1, set_inverse)
  rotation_degrees = property(TransformWrapper._g2, set_rotation_degrees)

  def to_builder(self) -> TransformWrapperBuilder:
    return self

  def build(self) -> TransformWrapper:
    v = TransformWrapper()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    return v
