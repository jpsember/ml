from __future__ import annotations
from pycore.base import AbstractData


class AugmentationConfig(AbstractData):

  default_instance: AugmentationConfig

  _k_0 = "horizontal_flip"
  _k_1 = "adjust_brightness"
  _k_2 = "bright_shift_min"
  _k_3 = "bright_shift_max"
  _k_4 = "shear_disable"
  _k_5 = "shear_max"
  _k_6 = "scale_disable"
  _k_7 = "scale_min"
  _k_8 = "scale_max"
  _k_9 = "rotate_disable"
  _k_10 = "rotate_degrees_max"
  _k_11 = "translate_disable"
  _k_12 = "translate_ratio_max"
  _k_13 = "blur_factor"
  _k_14 = "obvious_mode_labels"

  def __init__(self):
    self._h = None
    self._0 = True
    self._1 = False
    self._2 = -0.1
    self._3 = 0.1
    self._4 = False
    self._5 = 0.25
    self._6 = False
    self._7 = 0.0
    self._8 = 1.2
    self._9 = False
    self._10 = 8.0
    self._11 = False
    self._12 = 0.2
    self._13 = 0
    self._14 = ""

  @classmethod
  def new_builder(cls) -> AugmentationConfigBuilder:
    return AugmentationConfigBuilder()

  def parse(self, obj: dict) -> AugmentationConfig:
    inst = AugmentationConfig()
    inst._0 = obj.get(AugmentationConfig._k_0, True)
    inst._1 = obj.get(AugmentationConfig._k_1, False)
    inst._2 = obj.get(AugmentationConfig._k_2, -0.1)
    inst._3 = obj.get(AugmentationConfig._k_3, 0.1)
    inst._4 = obj.get(AugmentationConfig._k_4, False)
    inst._5 = obj.get(AugmentationConfig._k_5, 0.25)
    inst._6 = obj.get(AugmentationConfig._k_6, False)
    inst._7 = obj.get(AugmentationConfig._k_7, 0.0)
    inst._8 = obj.get(AugmentationConfig._k_8, 1.2)
    inst._9 = obj.get(AugmentationConfig._k_9, False)
    inst._10 = obj.get(AugmentationConfig._k_10, 8.0)
    inst._11 = obj.get(AugmentationConfig._k_11, False)
    inst._12 = obj.get(AugmentationConfig._k_12, 0.2)
    inst._13 = obj.get(AugmentationConfig._k_13, 0)
    inst._14 = obj.get(AugmentationConfig._k_14, "")
    return inst

  def _g0(self) -> bool:
    return self._0

  def _g1(self) -> bool:
    return self._1

  def _g2(self) -> float:
    return self._2

  def _g3(self) -> float:
    return self._3

  def _g4(self) -> bool:
    return self._4

  def _g5(self) -> float:
    return self._5

  def _g6(self) -> bool:
    return self._6

  def _g7(self) -> float:
    return self._7

  def _g8(self) -> float:
    return self._8

  def _g9(self) -> bool:
    return self._9

  def _g10(self) -> float:
    return self._10

  def _g11(self) -> bool:
    return self._11

  def _g12(self) -> float:
    return self._12

  def _g13(self) -> int:
    return self._13

  def _g14(self) -> str:
    return self._14

  horizontal_flip = property(_g0)
  adjust_brightness = property(_g1)
  bright_shift_min = property(_g2)
  bright_shift_max = property(_g3)
  shear_disable = property(_g4)
  shear_max = property(_g5)
  scale_disable = property(_g6)
  scale_min = property(_g7)
  scale_max = property(_g8)
  rotate_disable = property(_g9)
  rotate_degrees_max = property(_g10)
  translate_disable = property(_g11)
  translate_ratio_max = property(_g12)
  blur_factor = property(_g13)
  obvious_mode_labels = property(_g14)

  def to_builder(self) -> AugmentationConfigBuilder:
    x = AugmentationConfigBuilder()
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
    x._14 = self._14
    return x

  def to_json(self) -> dict:
    m = {}
    m[AugmentationConfig._k_0] = self._0
    m[AugmentationConfig._k_1] = self._1
    m[AugmentationConfig._k_2] = self._2
    m[AugmentationConfig._k_3] = self._3
    m[AugmentationConfig._k_4] = self._4
    m[AugmentationConfig._k_5] = self._5
    m[AugmentationConfig._k_6] = self._6
    m[AugmentationConfig._k_7] = self._7
    m[AugmentationConfig._k_8] = self._8
    m[AugmentationConfig._k_9] = self._9
    m[AugmentationConfig._k_10] = self._10
    m[AugmentationConfig._k_11] = self._11
    m[AugmentationConfig._k_12] = self._12
    m[AugmentationConfig._k_13] = self._13
    m[AugmentationConfig._k_14] = self._14
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
    if isinstance(other, AugmentationConfig):
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


AugmentationConfig.default_instance = AugmentationConfig()


class AugmentationConfigBuilder(AugmentationConfig):

  def set_horizontal_flip(self, x: bool) -> AugmentationConfigBuilder:
    self._0 = True if x is None else x
    return self

  def set_adjust_brightness(self, x: bool) -> AugmentationConfigBuilder:
    self._1 = False if x is None else x
    return self

  def set_bright_shift_min(self, x: float) -> AugmentationConfigBuilder:
    self._2 = -0.1 if x is None else x
    return self

  def set_bright_shift_max(self, x: float) -> AugmentationConfigBuilder:
    self._3 = 0.1 if x is None else x
    return self

  def set_shear_disable(self, x: bool) -> AugmentationConfigBuilder:
    self._4 = False if x is None else x
    return self

  def set_shear_max(self, x: float) -> AugmentationConfigBuilder:
    self._5 = 0.25 if x is None else x
    return self

  def set_scale_disable(self, x: bool) -> AugmentationConfigBuilder:
    self._6 = False if x is None else x
    return self

  def set_scale_min(self, x: float) -> AugmentationConfigBuilder:
    self._7 = 0.0 if x is None else x
    return self

  def set_scale_max(self, x: float) -> AugmentationConfigBuilder:
    self._8 = 1.2 if x is None else x
    return self

  def set_rotate_disable(self, x: bool) -> AugmentationConfigBuilder:
    self._9 = False if x is None else x
    return self

  def set_rotate_degrees_max(self, x: float) -> AugmentationConfigBuilder:
    self._10 = 8.0 if x is None else x
    return self

  def set_translate_disable(self, x: bool) -> AugmentationConfigBuilder:
    self._11 = False if x is None else x
    return self

  def set_translate_ratio_max(self, x: float) -> AugmentationConfigBuilder:
    self._12 = 0.2 if x is None else x
    return self

  def set_blur_factor(self, x: int) -> AugmentationConfigBuilder:
    self._13 = 0 if x is None else x
    return self

  def set_obvious_mode_labels(self, x: str) -> AugmentationConfigBuilder:
    self._14 = "" if x is None else x
    return self

  horizontal_flip = property(AugmentationConfig._g0, set_horizontal_flip)
  adjust_brightness = property(AugmentationConfig._g1, set_adjust_brightness)
  bright_shift_min = property(AugmentationConfig._g2, set_bright_shift_min)
  bright_shift_max = property(AugmentationConfig._g3, set_bright_shift_max)
  shear_disable = property(AugmentationConfig._g4, set_shear_disable)
  shear_max = property(AugmentationConfig._g5, set_shear_max)
  scale_disable = property(AugmentationConfig._g6, set_scale_disable)
  scale_min = property(AugmentationConfig._g7, set_scale_min)
  scale_max = property(AugmentationConfig._g8, set_scale_max)
  rotate_disable = property(AugmentationConfig._g9, set_rotate_disable)
  rotate_degrees_max = property(AugmentationConfig._g10, set_rotate_degrees_max)
  translate_disable = property(AugmentationConfig._g11, set_translate_disable)
  translate_ratio_max = property(AugmentationConfig._g12, set_translate_ratio_max)
  blur_factor = property(AugmentationConfig._g13, set_blur_factor)
  obvious_mode_labels = property(AugmentationConfig._g14, set_obvious_mode_labels)

  def to_builder(self) -> AugmentationConfigBuilder:
    return self

  def build(self) -> AugmentationConfig:
    v = AugmentationConfig()
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
    v._14 = self._14
    return v
