from __future__ import annotations
from pycore.base import AbstractData
from pycore.datautil import DataUtil
from pycore.ipoint import IPoint
from typing import List


class Yolo(AbstractData):

  default_instance: Yolo

  _k_0 = "image_size"
  _k_1 = "image_channels"
  _k_2 = "block_size"
  _k_3 = "category_count"
  _k_4 = "anchor_boxes_pixels"
  _k_5 = "lambda_coord"
  _k_6 = "lambda_noobj"
  _k_7 = "neighbor_factor"

  def __init__(self):
    self._h = None
    self._0 = IPoint.default_instance
    self._1 = 0
    self._2 = DEF_k_2
    self._3 = 0
    self._4 = []
    self._5 = 5.0
    self._6 = 0.5
    self._7 = 0.0

  @classmethod
  def new_builder(cls) -> YoloBuilder:
    return YoloBuilder()

  def parse(self, obj: dict) -> Yolo:
    inst = Yolo()
    x = obj.get(Yolo._k_0)
    if x is not None:
      inst._0 = IPoint.default_instance.parse(x)
    inst._1 = obj.get(Yolo._k_1, 0)
    x = obj.get(Yolo._k_2)
    if x is not None:
      inst._2 = DEF_k_2.parse(x)
    inst._3 = obj.get(Yolo._k_3, 0)
    inst._4 = DataUtil.parse_list_of_objects(IPoint.default_instance, obj.get(Yolo._k_4), False)
    inst._5 = obj.get(Yolo._k_5, 5.0)
    inst._6 = obj.get(Yolo._k_6, 0.5)
    inst._7 = obj.get(Yolo._k_7, 0.0)
    return inst

  def _g0(self) -> IPoint:
    return self._0

  def _g1(self) -> int:
    return self._1

  def _g2(self) -> IPoint:
    return self._2

  def _g3(self) -> int:
    return self._3

  def _g4(self) -> List[IPoint]:
    return self._4

  def _g5(self) -> float:
    return self._5

  def _g6(self) -> float:
    return self._6

  def _g7(self) -> float:
    return self._7

  image_size = property(_g0)
  image_channels = property(_g1)
  block_size = property(_g2)
  category_count = property(_g3)
  anchor_boxes_pixels = property(_g4)
  lambda_coord = property(_g5)
  lambda_noobj = property(_g6)
  neighbor_factor = property(_g7)

  def to_builder(self) -> YoloBuilder:
    x = YoloBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    x._4 = self._4.copy()
    x._5 = self._5
    x._6 = self._6
    x._7 = self._7
    return x

  def to_json(self) -> dict:
    m = {}
    m[Yolo._k_0] = self._0.to_json()
    m[Yolo._k_1] = self._1
    m[Yolo._k_2] = self._2.to_json()
    m[Yolo._k_3] = self._3
    m[Yolo._k_4] = [x.to_json() for x in self._4]
    m[Yolo._k_5] = self._5
    m[Yolo._k_6] = self._6
    m[Yolo._k_7] = self._7
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._0)
      r = r * 37 + hash(self._1)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._3)
      for x in self._4:
        r = r * 37 + hash(x)
      r = r * 37 + hash(self._5)
      r = r * 37 + hash(self._6)
      r = r * 37 + hash(self._7)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, Yolo):
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


DEF_k_2  = IPoint.with_x_y(32, 32)


Yolo.default_instance = Yolo()


class YoloBuilder(Yolo):

  def set_image_size(self, x: IPoint) -> YoloBuilder:
    if x is None:
      x = IPoint.default_instance
    self._0 = x.build()
    return self

  def set_image_channels(self, x: int) -> YoloBuilder:
    self._1 = 0 if x is None else x
    return self

  def set_block_size(self, x: IPoint) -> YoloBuilder:
    if x is None:
      x = DEF_k_2
    self._2 = x.build()
    return self

  def set_category_count(self, x: int) -> YoloBuilder:
    self._3 = 0 if x is None else x
    return self

  def set_anchor_boxes_pixels(self, x: List[IPoint]) -> YoloBuilder:
    self._4 = [] if x is None else x.copy()
    return self

  def set_lambda_coord(self, x: float) -> YoloBuilder:
    self._5 = 5.0 if x is None else x
    return self

  def set_lambda_noobj(self, x: float) -> YoloBuilder:
    self._6 = 0.5 if x is None else x
    return self

  def set_neighbor_factor(self, x: float) -> YoloBuilder:
    self._7 = 0.0 if x is None else x
    return self

  image_size = property(Yolo._g0, set_image_size)
  image_channels = property(Yolo._g1, set_image_channels)
  block_size = property(Yolo._g2, set_block_size)
  category_count = property(Yolo._g3, set_category_count)
  anchor_boxes_pixels = property(Yolo._g4, set_anchor_boxes_pixels)
  lambda_coord = property(Yolo._g5, set_lambda_coord)
  lambda_noobj = property(Yolo._g6, set_lambda_noobj)
  neighbor_factor = property(Yolo._g7, set_neighbor_factor)

  def to_builder(self) -> YoloBuilder:
    return self

  def build(self) -> Yolo:
    v = Yolo()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    v._4 = self._4.copy()
    v._5 = self._5
    v._6 = self._6
    v._7 = self._7
    return v
