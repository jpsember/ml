from __future__ import annotations
from gen.layer_type import LayerType
from gen.vol import Vol
from pycore.base import AbstractData
from pycore.ipoint import IPoint


class Layer(AbstractData):

  default_instance: Layer

  _k_0 = "type"
  _k_1 = "kernel_width"
  _k_2 = "filters"
  _k_3 = "pool"
  _k_4 = "alpha"
  _k_5 = "stride"
  _k_6 = "dropout"
  _k_7 = "batch_norm"
  _k_8 = "num_weights"
  _k_9 = "input_volume"
  _k_10 = "output_volume"

  def __init__(self):
    self._h = None
    self._0 = LayerType.default_instance
    self._1 = None
    self._2 = 0
    self._3 = False
    self._4 = None
    self._5 = None
    self._6 = None
    self._7 = False
    self._8 = 0
    self._9 = Vol.default_instance
    self._10 = Vol.default_instance

  @classmethod
  def new_builder(cls) -> LayerBuilder:
    return LayerBuilder()

  def parse(self, obj: dict) -> Layer:
    inst = Layer()
    x = obj.get(Layer._k_0, LayerType.default_instance)
    inst._0 = x
    inst._1 = obj.get(Layer._k_1, None)
    inst._2 = obj.get(Layer._k_2, 0)
    inst._3 = obj.get(Layer._k_3, False)
    inst._4 = obj.get(Layer._k_4, None)
    x = obj.get(Layer._k_5)
    if x is not None:
      inst._5 = IPoint.default_instance.parse(x)
    inst._6 = obj.get(Layer._k_6, None)
    inst._7 = obj.get(Layer._k_7, False)
    inst._8 = obj.get(Layer._k_8, 0)
    x = obj.get(Layer._k_9)
    if x is not None:
      inst._9 = Vol.default_instance.parse(x)
    x = obj.get(Layer._k_10)
    if x is not None:
      inst._10 = Vol.default_instance.parse(x)
    return inst

  def _g0(self) -> LayerType:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  def _g3(self) -> bool:
    return self._3

  def _g4(self) -> float:
    return self._4

  def _g5(self) -> IPoint:
    return self._5

  def _g6(self) -> float:
    return self._6

  def _g7(self) -> bool:
    return self._7

  def _g8(self) -> int:
    return self._8

  def _g9(self) -> Vol:
    return self._9

  def _g10(self) -> Vol:
    return self._10

  type = property(_g0)
  kernel_width = property(_g1)
  filters = property(_g2)
  pool = property(_g3)
  alpha = property(_g4)
  stride = property(_g5)
  dropout = property(_g6)
  batch_norm = property(_g7)
  num_weights = property(_g8)
  input_volume = property(_g9)
  output_volume = property(_g10)

  def to_builder(self) -> LayerBuilder:
    x = LayerBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    x._4 = self._4
    x._5 = self._5
    x._6 = self._6
    x._7 = self._7
    x._8 = self._8
    x._9 = self._9
    x._10 = self._10
    return x

  def to_json(self) -> dict:
    m = {}
    m[Layer._k_0] = self._0
    if self._1 is not None:
      m[Layer._k_1] = self._1
    m[Layer._k_2] = self._2
    m[Layer._k_3] = self._3
    if self._4 is not None:
      m[Layer._k_4] = self._4
    if self._5 is not None:
      m[Layer._k_5] = self._5.to_json()
    if self._6 is not None:
      m[Layer._k_6] = self._6
    m[Layer._k_7] = self._7
    m[Layer._k_8] = self._8
    m[Layer._k_9] = self._9.to_json()
    m[Layer._k_10] = self._10.to_json()
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._3)
      r = r * 37 + hash(self._7)
      r = r * 37 + hash(self._8)
      r = r * 37 + hash(self._9)
      r = r * 37 + hash(self._10)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._4)
      r = r * 37 + hash(self._5)
      r = r * 37 + hash(self._6)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, Layer):
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


Layer.default_instance = Layer()


class LayerBuilder(Layer):

  def set_type(self, x: LayerType) -> LayerBuilder:
    self._0 = LayerType.default_instance if x is None else x
    return self

  def set_kernel_width(self, x: int) -> LayerBuilder:
    self._1 = x
    return self

  def set_filters(self, x: int) -> LayerBuilder:
    self._2 = 0 if x is None else x
    return self

  def set_pool(self, x: bool) -> LayerBuilder:
    self._3 = False if x is None else x
    return self

  def set_alpha(self, x: float) -> LayerBuilder:
    self._4 = x
    return self

  def set_stride(self, x: IPoint) -> LayerBuilder:
    if x is not None:
      x = x.build()
    self._5 = x
    return self

  def set_dropout(self, x: float) -> LayerBuilder:
    self._6 = x
    return self

  def set_batch_norm(self, x: bool) -> LayerBuilder:
    self._7 = False if x is None else x
    return self

  def set_num_weights(self, x: int) -> LayerBuilder:
    self._8 = 0 if x is None else x
    return self

  def set_input_volume(self, x: Vol) -> LayerBuilder:
    if x is None:
      x = Vol.default_instance
    self._9 = x.build()
    return self

  def set_output_volume(self, x: Vol) -> LayerBuilder:
    if x is None:
      x = Vol.default_instance
    self._10 = x.build()
    return self

  type = property(Layer._g0, set_type)
  kernel_width = property(Layer._g1, set_kernel_width)
  filters = property(Layer._g2, set_filters)
  pool = property(Layer._g3, set_pool)
  alpha = property(Layer._g4, set_alpha)
  stride = property(Layer._g5, set_stride)
  dropout = property(Layer._g6, set_dropout)
  batch_norm = property(Layer._g7, set_batch_norm)
  num_weights = property(Layer._g8, set_num_weights)
  input_volume = property(Layer._g9, set_input_volume)
  output_volume = property(Layer._g10, set_output_volume)

  def to_builder(self) -> LayerBuilder:
    return self

  def build(self) -> Layer:
    v = Layer()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    v._4 = self._4
    v._5 = self._5
    v._6 = self._6
    v._7 = self._7
    v._8 = self._8
    v._9 = self._9
    v._10 = self._10
    return v
