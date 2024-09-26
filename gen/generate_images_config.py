from __future__ import annotations
from gen.augmentation_config import AugmentationConfig
from gen.neural_network import NeuralNetwork
from pycore.base import AbstractData


class GenerateImagesConfig(AbstractData):

  default_instance: GenerateImagesConfig

  _k_0 = "target_dir"
  _k_1 = "image_total"
  _k_2 = "seed"
  _k_3 = "network"
  _k_4 = "network_path"
  _k_5 = "categories"
  _k_6 = "max_objects"
  _k_7 = "augmentation_config"
  _k_8 = "noise_factor"
  _k_9 = "font_limit"
  _k_10 = "color_limit"
  _k_11 = "bgnd_image"

  def __init__(self):
    self._h = None
    self._0 = "generated_images"
    self._1 = 20
    self._2 = 0
    self._3 = None
    self._4 = ""
    self._5 = ""
    self._6 = 4
    self._7 = AugmentationConfig.default_instance
    self._8 = 30
    self._9 = 0
    self._10 = 0
    self._11 = ""

  @classmethod
  def new_builder(cls) -> GenerateImagesConfigBuilder:
    return GenerateImagesConfigBuilder()

  def parse(self, obj: dict) -> GenerateImagesConfig:
    inst = GenerateImagesConfig()
    inst._0 = obj.get(GenerateImagesConfig._k_0, "generated_images")
    inst._1 = obj.get(GenerateImagesConfig._k_1, 20)
    inst._2 = obj.get(GenerateImagesConfig._k_2, 0)
    x = obj.get(GenerateImagesConfig._k_3)
    if x is not None:
      inst._3 = NeuralNetwork.default_instance.parse(x)
    inst._4 = obj.get(GenerateImagesConfig._k_4, "")
    inst._5 = obj.get(GenerateImagesConfig._k_5, "")
    inst._6 = obj.get(GenerateImagesConfig._k_6, 4)
    x = obj.get(GenerateImagesConfig._k_7)
    if x is not None:
      inst._7 = AugmentationConfig.default_instance.parse(x)
    inst._8 = obj.get(GenerateImagesConfig._k_8, 30)
    inst._9 = obj.get(GenerateImagesConfig._k_9, 0)
    inst._10 = obj.get(GenerateImagesConfig._k_10, 0)
    inst._11 = obj.get(GenerateImagesConfig._k_11, "")
    return inst

  def _g0(self) -> str:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> int:
    return self._2

  def _g3(self) -> NeuralNetwork:
    return self._3

  def _g4(self) -> str:
    return self._4

  def _g5(self) -> str:
    return self._5

  def _g6(self) -> int:
    return self._6

  def _g7(self) -> AugmentationConfig:
    return self._7

  def _g8(self) -> int:
    return self._8

  def _g9(self) -> int:
    return self._9

  def _g10(self) -> int:
    return self._10

  def _g11(self) -> str:
    return self._11

  target_dir = property(_g0)
  image_total = property(_g1)
  seed = property(_g2)
  network = property(_g3)
  network_path = property(_g4)
  categories = property(_g5)
  max_objects = property(_g6)
  augmentation_config = property(_g7)
  noise_factor = property(_g8)
  font_limit = property(_g9)
  color_limit = property(_g10)
  bgnd_image = property(_g11)

  def to_builder(self) -> GenerateImagesConfigBuilder:
    x = GenerateImagesConfigBuilder()
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
    return x

  def to_json(self) -> dict:
    m = {}
    m[GenerateImagesConfig._k_0] = self._0
    m[GenerateImagesConfig._k_1] = self._1
    m[GenerateImagesConfig._k_2] = self._2
    if self._3 is not None:
      m[GenerateImagesConfig._k_3] = self._3.to_json()
    m[GenerateImagesConfig._k_4] = self._4
    m[GenerateImagesConfig._k_5] = self._5
    m[GenerateImagesConfig._k_6] = self._6
    m[GenerateImagesConfig._k_7] = self._7.to_json()
    m[GenerateImagesConfig._k_8] = self._8
    m[GenerateImagesConfig._k_9] = self._9
    m[GenerateImagesConfig._k_10] = self._10
    m[GenerateImagesConfig._k_11] = self._11
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._4)
      r = r * 37 + hash(self._5)
      r = r * 37 + hash(self._6)
      r = r * 37 + hash(self._7)
      r = r * 37 + hash(self._8)
      r = r * 37 + hash(self._9)
      r = r * 37 + hash(self._10)
      r = r * 37 + hash(self._11)
      r = r * 37 + hash(self._3)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, GenerateImagesConfig):
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
        and self._11 == other._11
    else:
      return False


GenerateImagesConfig.default_instance = GenerateImagesConfig()


class GenerateImagesConfigBuilder(GenerateImagesConfig):

  def set_target_dir(self, x: str) -> GenerateImagesConfigBuilder:
    self._0 = "generated_images" if x is None else x
    return self

  def set_image_total(self, x: int) -> GenerateImagesConfigBuilder:
    self._1 = 20 if x is None else x
    return self

  def set_seed(self, x: int) -> GenerateImagesConfigBuilder:
    self._2 = 0 if x is None else x
    return self

  def set_network(self, x: NeuralNetwork) -> GenerateImagesConfigBuilder:
    if x is not None:
      x = x.build()
    self._3 = x
    return self

  def set_network_path(self, x: str) -> GenerateImagesConfigBuilder:
    self._4 = "" if x is None else x
    return self

  def set_categories(self, x: str) -> GenerateImagesConfigBuilder:
    self._5 = "" if x is None else x
    return self

  def set_max_objects(self, x: int) -> GenerateImagesConfigBuilder:
    self._6 = 4 if x is None else x
    return self

  def set_augmentation_config(self, x: AugmentationConfig) -> GenerateImagesConfigBuilder:
    if x is None:
      x = AugmentationConfig.default_instance
    self._7 = x.build()
    return self

  def set_noise_factor(self, x: int) -> GenerateImagesConfigBuilder:
    self._8 = 30 if x is None else x
    return self

  def set_font_limit(self, x: int) -> GenerateImagesConfigBuilder:
    self._9 = 0 if x is None else x
    return self

  def set_color_limit(self, x: int) -> GenerateImagesConfigBuilder:
    self._10 = 0 if x is None else x
    return self

  def set_bgnd_image(self, x: str) -> GenerateImagesConfigBuilder:
    self._11 = "" if x is None else x
    return self

  target_dir = property(GenerateImagesConfig._g0, set_target_dir)
  image_total = property(GenerateImagesConfig._g1, set_image_total)
  seed = property(GenerateImagesConfig._g2, set_seed)
  network = property(GenerateImagesConfig._g3, set_network)
  network_path = property(GenerateImagesConfig._g4, set_network_path)
  categories = property(GenerateImagesConfig._g5, set_categories)
  max_objects = property(GenerateImagesConfig._g6, set_max_objects)
  augmentation_config = property(GenerateImagesConfig._g7, set_augmentation_config)
  noise_factor = property(GenerateImagesConfig._g8, set_noise_factor)
  font_limit = property(GenerateImagesConfig._g9, set_font_limit)
  color_limit = property(GenerateImagesConfig._g10, set_color_limit)
  bgnd_image = property(GenerateImagesConfig._g11, set_bgnd_image)

  def to_builder(self) -> GenerateImagesConfigBuilder:
    return self

  def build(self) -> GenerateImagesConfig:
    v = GenerateImagesConfig()
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
    return v
