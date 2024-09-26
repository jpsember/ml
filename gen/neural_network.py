from __future__ import annotations
from gen.data_type import DataType
from gen.layer import Layer
from gen.network_options import NetworkOptions
from gen.network_project_type import NetworkProjectType
from gen.special_option import SpecialOption
from pycore.base import AbstractData
from pycore.datautil import DataUtil
from pycore.ipoint import IPoint
from typing import List


class NeuralNetwork(AbstractData):

  default_instance: NeuralNetwork

  _k_0 = "version"
  _k_1 = "project_type"
  _k_2 = "layers"
  _k_3 = "weight_count"
  _k_4 = "kernel_width"
  _k_5 = "alpha"
  _k_6 = "stride"
  _k_7 = "dropout_input"
  _k_8 = "dropout_hidden"
  _k_9 = "model_config"
  _k_10 = "monochrome_source_images"
  _k_11 = "image_data_type"
  _k_12 = "label_data_type"
  _k_13 = "special_option"
  _k_14 = "options"

  def __init__(self):
    self._h = None
    self._0 = 0
    self._1 = NetworkProjectType.default_instance
    self._2 = []
    self._3 = 0
    self._4 = 3
    self._5 = 0.01
    self._6 = DEF_k_6
    self._7 = 0.2
    self._8 = 0.5
    self._9 = {}
    self._10 = False
    self._11 = DataType.default_instance
    self._12 = DataType.default_instance
    self._13 = SpecialOption.default_instance
    self._14 = NetworkOptions.default_instance

  @classmethod
  def new_builder(cls) -> NeuralNetworkBuilder:
    return NeuralNetworkBuilder()

  def parse(self, obj: dict) -> NeuralNetwork:
    inst = NeuralNetwork()
    inst._0 = obj.get(NeuralNetwork._k_0, 0)
    x = obj.get(NeuralNetwork._k_1, NetworkProjectType.default_instance)
    inst._1 = x
    inst._2 = DataUtil.parse_list_of_objects(Layer.default_instance, obj.get(NeuralNetwork._k_2), False)
    inst._3 = obj.get(NeuralNetwork._k_3, 0)
    inst._4 = obj.get(NeuralNetwork._k_4, 3)
    inst._5 = obj.get(NeuralNetwork._k_5, 0.01)
    x = obj.get(NeuralNetwork._k_6)
    if x is not None:
      inst._6 = DEF_k_6.parse(x)
    inst._7 = obj.get(NeuralNetwork._k_7, 0.2)
    inst._8 = obj.get(NeuralNetwork._k_8, 0.5)
    inst._9 = obj.get(NeuralNetwork._k_9, {})
    inst._10 = obj.get(NeuralNetwork._k_10, False)
    x = obj.get(NeuralNetwork._k_11, DataType.default_instance)
    inst._11 = x
    x = obj.get(NeuralNetwork._k_12, DataType.default_instance)
    inst._12 = x
    x = obj.get(NeuralNetwork._k_13, SpecialOption.default_instance)
    inst._13 = x
    x = obj.get(NeuralNetwork._k_14)
    if x is not None:
      inst._14 = NetworkOptions.default_instance.parse(x)
    return inst

  def _g0(self) -> int:
    return self._0

  def _g1(self) -> NetworkProjectType:
    return self._1

  def _g2(self) -> List[Layer]:
    return self._2

  def _g3(self) -> int:
    return self._3

  def _g4(self) -> int:
    return self._4

  def _g5(self) -> float:
    return self._5

  def _g6(self) -> IPoint:
    return self._6

  def _g7(self) -> float:
    return self._7

  def _g8(self) -> float:
    return self._8

  def _g9(self) -> dict:
    return self._9

  def _g10(self) -> bool:
    return self._10

  def _g11(self) -> DataType:
    return self._11

  def _g12(self) -> DataType:
    return self._12

  def _g13(self) -> SpecialOption:
    return self._13

  def _g14(self) -> NetworkOptions:
    return self._14

  version = property(_g0)
  project_type = property(_g1)
  layers = property(_g2)
  weight_count = property(_g3)
  kernel_width = property(_g4)
  alpha = property(_g5)
  stride = property(_g6)
  dropout_input = property(_g7)
  dropout_hidden = property(_g8)
  model_config = property(_g9)
  monochrome_source_images = property(_g10)
  image_data_type = property(_g11)
  label_data_type = property(_g12)
  special_option = property(_g13)
  options = property(_g14)

  def to_builder(self) -> NeuralNetworkBuilder:
    x = NeuralNetworkBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2.copy()
    x._3 = self._3
    x._4 = self._4
    x._5 = self._5
    x._6 = self._6
    x._7 = self._7
    x._8 = self._8
    x._9 = self._9
    x._10 = self._10
    x._11 = self._11
    x._12 = self._12
    x._13 = self._13
    x._14 = self._14
    return x

  def to_json(self) -> dict:
    m = {}
    m[NeuralNetwork._k_0] = self._0
    m[NeuralNetwork._k_1] = self._1
    m[NeuralNetwork._k_2] = [x.to_json() for x in self._2]
    m[NeuralNetwork._k_3] = self._3
    m[NeuralNetwork._k_4] = self._4
    m[NeuralNetwork._k_5] = self._5
    m[NeuralNetwork._k_6] = self._6.to_json()
    m[NeuralNetwork._k_7] = self._7
    m[NeuralNetwork._k_8] = self._8
    m[NeuralNetwork._k_9] = self._9
    m[NeuralNetwork._k_10] = self._10
    m[NeuralNetwork._k_11] = self._11
    m[NeuralNetwork._k_12] = self._12
    m[NeuralNetwork._k_13] = self._13
    m[NeuralNetwork._k_14] = self._14.to_json()
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      for x in self._2:
        r = r * 37 + hash(x)
      r = r * 37 + hash(self._3)
      r = r * 37 + hash(self._4)
      r = r * 37 + hash(self._5)
      r = r * 37 + hash(self._6)
      r = r * 37 + hash(self._7)
      r = r * 37 + hash(self._8)
      r = r * 37 + hash(self._9)
      r = r * 37 + hash(self._10)
      r = r * 37 + hash(self._11)
      r = r * 37 + hash(self._12)
      r = r * 37 + hash(self._13)
      r = r * 37 + hash(self._14)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, NeuralNetwork):
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
        and self._10 == other._10\
        and self._11 == other._11\
        and self._12 == other._12\
        and self._13 == other._13\
        and self._14 == other._14
    else:
      return False


DEF_k_6  = IPoint.with_x_y(2, 2)


NeuralNetwork.default_instance = NeuralNetwork()


class NeuralNetworkBuilder(NeuralNetwork):

  def set_version(self, x: int) -> NeuralNetworkBuilder:
    self._0 = 0 if x is None else x
    return self

  def set_project_type(self, x: NetworkProjectType) -> NeuralNetworkBuilder:
    self._1 = NetworkProjectType.default_instance if x is None else x
    return self

  def set_layers(self, x: List[Layer]) -> NeuralNetworkBuilder:
    self._2 = [] if x is None else x.copy()
    return self

  def set_weight_count(self, x: int) -> NeuralNetworkBuilder:
    self._3 = 0 if x is None else x
    return self

  def set_kernel_width(self, x: int) -> NeuralNetworkBuilder:
    self._4 = 3 if x is None else x
    return self

  def set_alpha(self, x: float) -> NeuralNetworkBuilder:
    self._5 = 0.01 if x is None else x
    return self

  def set_stride(self, x: IPoint) -> NeuralNetworkBuilder:
    if x is None:
      x = DEF_k_6
    self._6 = x.build()
    return self

  def set_dropout_input(self, x: float) -> NeuralNetworkBuilder:
    self._7 = 0.2 if x is None else x
    return self

  def set_dropout_hidden(self, x: float) -> NeuralNetworkBuilder:
    self._8 = 0.5 if x is None else x
    return self

  def set_model_config(self, x: dict) -> NeuralNetworkBuilder:
    self._9 = {} if x is None else x
    return self

  def set_monochrome_source_images(self, x: bool) -> NeuralNetworkBuilder:
    self._10 = False if x is None else x
    return self

  def set_image_data_type(self, x: DataType) -> NeuralNetworkBuilder:
    self._11 = DataType.default_instance if x is None else x
    return self

  def set_label_data_type(self, x: DataType) -> NeuralNetworkBuilder:
    self._12 = DataType.default_instance if x is None else x
    return self

  def set_special_option(self, x: SpecialOption) -> NeuralNetworkBuilder:
    self._13 = SpecialOption.default_instance if x is None else x
    return self

  def set_options(self, x: NetworkOptions) -> NeuralNetworkBuilder:
    if x is None:
      x = NetworkOptions.default_instance
    self._14 = x.build()
    return self

  version = property(NeuralNetwork._g0, set_version)
  project_type = property(NeuralNetwork._g1, set_project_type)
  layers = property(NeuralNetwork._g2, set_layers)
  weight_count = property(NeuralNetwork._g3, set_weight_count)
  kernel_width = property(NeuralNetwork._g4, set_kernel_width)
  alpha = property(NeuralNetwork._g5, set_alpha)
  stride = property(NeuralNetwork._g6, set_stride)
  dropout_input = property(NeuralNetwork._g7, set_dropout_input)
  dropout_hidden = property(NeuralNetwork._g8, set_dropout_hidden)
  model_config = property(NeuralNetwork._g9, set_model_config)
  monochrome_source_images = property(NeuralNetwork._g10, set_monochrome_source_images)
  image_data_type = property(NeuralNetwork._g11, set_image_data_type)
  label_data_type = property(NeuralNetwork._g12, set_label_data_type)
  special_option = property(NeuralNetwork._g13, set_special_option)
  options = property(NeuralNetwork._g14, set_options)

  def to_builder(self) -> NeuralNetworkBuilder:
    return self

  def build(self) -> NeuralNetwork:
    v = NeuralNetwork()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2.copy()
    v._3 = self._3
    v._4 = self._4
    v._5 = self._5
    v._6 = self._6
    v._7 = self._7
    v._8 = self._8
    v._9 = self._9
    v._10 = self._10
    v._11 = self._11
    v._12 = self._12
    v._13 = self._13
    v._14 = self._14
    return v
