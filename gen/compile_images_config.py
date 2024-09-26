from __future__ import annotations
from gen.augmentation_config import AugmentationConfig
from gen.compile_oper import CompileOper
from gen.neural_network import NeuralNetwork
from gen.train_param import TrainParam
from pycore.base import AbstractData


class CompileImagesConfig(AbstractData):

  default_instance: CompileImagesConfig

  _k_0 = "oper"
  _k_1 = "network"
  _k_2 = "network_path"
  _k_3 = "source_dir"
  _k_4 = "augmentation_config"
  _k_5 = "seed"
  _k_6 = "target_dir_model"
  _k_7 = "inspection_dir"
  _k_8 = "train_param"
  _k_9 = "snapshot_dir"
  _k_10 = "progress_file"
  _k_11 = "inference_dir"
  _k_12 = "max_image_count"
  _k_13 = "inactivity_timeout_seconds"

  def __init__(self):
    self._h = None
    self._0 = CompileOper.default_instance
    self._1 = None
    self._2 = ""
    self._3 = ""
    self._4 = AugmentationConfig.default_instance
    self._5 = 0
    self._6 = "train_info"
    self._7 = ""
    self._8 = TrainParam.default_instance
    self._9 = ""
    self._10 = "progress.txt"
    self._11 = "inference"
    self._12 = 32
    self._13 = 900

  @classmethod
  def new_builder(cls) -> CompileImagesConfigBuilder:
    return CompileImagesConfigBuilder()

  def parse(self, obj: dict) -> CompileImagesConfig:
    inst = CompileImagesConfig()
    x = obj.get(CompileImagesConfig._k_0, CompileOper.default_instance)
    inst._0 = x
    x = obj.get(CompileImagesConfig._k_1)
    if x is not None:
      inst._1 = NeuralNetwork.default_instance.parse(x)
    inst._2 = obj.get(CompileImagesConfig._k_2, "")
    inst._3 = obj.get(CompileImagesConfig._k_3, "")
    x = obj.get(CompileImagesConfig._k_4)
    if x is not None:
      inst._4 = AugmentationConfig.default_instance.parse(x)
    inst._5 = obj.get(CompileImagesConfig._k_5, 0)
    inst._6 = obj.get(CompileImagesConfig._k_6, "train_info")
    inst._7 = obj.get(CompileImagesConfig._k_7, "")
    x = obj.get(CompileImagesConfig._k_8)
    if x is not None:
      inst._8 = TrainParam.default_instance.parse(x)
    inst._9 = obj.get(CompileImagesConfig._k_9, "")
    inst._10 = obj.get(CompileImagesConfig._k_10, "progress.txt")
    inst._11 = obj.get(CompileImagesConfig._k_11, "inference")
    inst._12 = obj.get(CompileImagesConfig._k_12, 32)
    inst._13 = obj.get(CompileImagesConfig._k_13, 900)
    return inst

  def _g0(self) -> CompileOper:
    return self._0

  def _g1(self) -> NeuralNetwork:
    return self._1

  def _g2(self) -> str:
    return self._2

  def _g3(self) -> str:
    return self._3

  def _g4(self) -> AugmentationConfig:
    return self._4

  def _g5(self) -> int:
    return self._5

  def _g6(self) -> str:
    return self._6

  def _g7(self) -> str:
    return self._7

  def _g8(self) -> TrainParam:
    return self._8

  def _g9(self) -> str:
    return self._9

  def _g10(self) -> str:
    return self._10

  def _g11(self) -> str:
    return self._11

  def _g12(self) -> int:
    return self._12

  def _g13(self) -> int:
    return self._13

  oper = property(_g0)
  network = property(_g1)
  network_path = property(_g2)
  source_dir = property(_g3)
  augmentation_config = property(_g4)
  seed = property(_g5)
  target_dir_model = property(_g6)
  inspection_dir = property(_g7)
  train_param = property(_g8)
  snapshot_dir = property(_g9)
  progress_file = property(_g10)
  inference_dir = property(_g11)
  max_image_count = property(_g12)
  inactivity_timeout_seconds = property(_g13)

  def to_builder(self) -> CompileImagesConfigBuilder:
    x = CompileImagesConfigBuilder()
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
    x._11 = self._11
    x._12 = self._12
    x._13 = self._13
    return x

  def to_json(self) -> dict:
    m = {}
    m[CompileImagesConfig._k_0] = self._0
    if self._1 is not None:
      m[CompileImagesConfig._k_1] = self._1.to_json()
    m[CompileImagesConfig._k_2] = self._2
    m[CompileImagesConfig._k_3] = self._3
    m[CompileImagesConfig._k_4] = self._4.to_json()
    m[CompileImagesConfig._k_5] = self._5
    m[CompileImagesConfig._k_6] = self._6
    m[CompileImagesConfig._k_7] = self._7
    m[CompileImagesConfig._k_8] = self._8.to_json()
    m[CompileImagesConfig._k_9] = self._9
    m[CompileImagesConfig._k_10] = self._10
    m[CompileImagesConfig._k_11] = self._11
    m[CompileImagesConfig._k_12] = self._12
    m[CompileImagesConfig._k_13] = self._13
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._2)
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
      r = r * 37 + hash(self._1)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, CompileImagesConfig):
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
        and self._13 == other._13
    else:
      return False


CompileImagesConfig.default_instance = CompileImagesConfig()


class CompileImagesConfigBuilder(CompileImagesConfig):

  def set_oper(self, x: CompileOper) -> CompileImagesConfigBuilder:
    self._0 = CompileOper.default_instance if x is None else x
    return self

  def set_network(self, x: NeuralNetwork) -> CompileImagesConfigBuilder:
    if x is not None:
      x = x.build()
    self._1 = x
    return self

  def set_network_path(self, x: str) -> CompileImagesConfigBuilder:
    self._2 = "" if x is None else x
    return self

  def set_source_dir(self, x: str) -> CompileImagesConfigBuilder:
    self._3 = "" if x is None else x
    return self

  def set_augmentation_config(self, x: AugmentationConfig) -> CompileImagesConfigBuilder:
    if x is None:
      x = AugmentationConfig.default_instance
    self._4 = x.build()
    return self

  def set_seed(self, x: int) -> CompileImagesConfigBuilder:
    self._5 = 0 if x is None else x
    return self

  def set_target_dir_model(self, x: str) -> CompileImagesConfigBuilder:
    self._6 = "train_info" if x is None else x
    return self

  def set_inspection_dir(self, x: str) -> CompileImagesConfigBuilder:
    self._7 = "" if x is None else x
    return self

  def set_train_param(self, x: TrainParam) -> CompileImagesConfigBuilder:
    if x is None:
      x = TrainParam.default_instance
    self._8 = x.build()
    return self

  def set_snapshot_dir(self, x: str) -> CompileImagesConfigBuilder:
    self._9 = "" if x is None else x
    return self

  def set_progress_file(self, x: str) -> CompileImagesConfigBuilder:
    self._10 = "progress.txt" if x is None else x
    return self

  def set_inference_dir(self, x: str) -> CompileImagesConfigBuilder:
    self._11 = "inference" if x is None else x
    return self

  def set_max_image_count(self, x: int) -> CompileImagesConfigBuilder:
    self._12 = 32 if x is None else x
    return self

  def set_inactivity_timeout_seconds(self, x: int) -> CompileImagesConfigBuilder:
    self._13 = 900 if x is None else x
    return self

  oper = property(CompileImagesConfig._g0, set_oper)
  network = property(CompileImagesConfig._g1, set_network)
  network_path = property(CompileImagesConfig._g2, set_network_path)
  source_dir = property(CompileImagesConfig._g3, set_source_dir)
  augmentation_config = property(CompileImagesConfig._g4, set_augmentation_config)
  seed = property(CompileImagesConfig._g5, set_seed)
  target_dir_model = property(CompileImagesConfig._g6, set_target_dir_model)
  inspection_dir = property(CompileImagesConfig._g7, set_inspection_dir)
  train_param = property(CompileImagesConfig._g8, set_train_param)
  snapshot_dir = property(CompileImagesConfig._g9, set_snapshot_dir)
  progress_file = property(CompileImagesConfig._g10, set_progress_file)
  inference_dir = property(CompileImagesConfig._g11, set_inference_dir)
  max_image_count = property(CompileImagesConfig._g12, set_max_image_count)
  inactivity_timeout_seconds = property(CompileImagesConfig._g13, set_inactivity_timeout_seconds)

  def to_builder(self) -> CompileImagesConfigBuilder:
    return self

  def build(self) -> CompileImagesConfig:
    v = CompileImagesConfig()
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
    v._11 = self._11
    v._12 = self._12
    v._13 = self._13
    return v
