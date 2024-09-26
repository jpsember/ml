from __future__ import annotations
from pycore.base import AbstractData


class TrainParam(AbstractData):

  default_instance: TrainParam

  _k_0 = "target_dir_train"
  _k_1 = "target_dir_checkpoint"
  _k_2 = "max_train_sets"
  _k_3 = "recycle"
  _k_4 = "max_checkpoints"
  _k_5 = "target_accuracy"
  _k_6 = "target_loss"
  _k_7 = "target_epoch"
  _k_8 = "batch_size"
  _k_9 = "detect_anomalies"
  _k_10 = "max_log_count"
  _k_11 = "with_gradient_norm"
  _k_12 = "disable_batch_norm"
  _k_13 = "generate_snapshots"

  def __init__(self):
    self._h = None
    self._0 = "train_data"
    self._1 = "checkpoints"
    self._2 = 3
    self._3 = 3
    self._4 = 3
    self._5 = 95
    self._6 = 0.0
    self._7 = 0
    self._8 = 32
    self._9 = False
    self._10 = 20
    self._11 = False
    self._12 = False
    self._13 = False

  @classmethod
  def new_builder(cls) -> TrainParamBuilder:
    return TrainParamBuilder()

  def parse(self, obj: dict) -> TrainParam:
    inst = TrainParam()
    inst._0 = obj.get(TrainParam._k_0, "train_data")
    inst._1 = obj.get(TrainParam._k_1, "checkpoints")
    inst._2 = obj.get(TrainParam._k_2, 3)
    inst._3 = obj.get(TrainParam._k_3, 3)
    inst._4 = obj.get(TrainParam._k_4, 3)
    inst._5 = obj.get(TrainParam._k_5, 95)
    inst._6 = obj.get(TrainParam._k_6, 0.0)
    inst._7 = obj.get(TrainParam._k_7, 0)
    inst._8 = obj.get(TrainParam._k_8, 32)
    inst._9 = obj.get(TrainParam._k_9, False)
    inst._10 = obj.get(TrainParam._k_10, 20)
    inst._11 = obj.get(TrainParam._k_11, False)
    inst._12 = obj.get(TrainParam._k_12, False)
    inst._13 = obj.get(TrainParam._k_13, False)
    return inst

  def _g0(self) -> str:
    return self._0

  def _g1(self) -> str:
    return self._1

  def _g2(self) -> int:
    return self._2

  def _g3(self) -> int:
    return self._3

  def _g4(self) -> int:
    return self._4

  def _g5(self) -> int:
    return self._5

  def _g6(self) -> float:
    return self._6

  def _g7(self) -> int:
    return self._7

  def _g8(self) -> int:
    return self._8

  def _g9(self) -> bool:
    return self._9

  def _g10(self) -> int:
    return self._10

  def _g11(self) -> bool:
    return self._11

  def _g12(self) -> bool:
    return self._12

  def _g13(self) -> bool:
    return self._13

  target_dir_train = property(_g0)
  target_dir_checkpoint = property(_g1)
  max_train_sets = property(_g2)
  recycle = property(_g3)
  max_checkpoints = property(_g4)
  target_accuracy = property(_g5)
  target_loss = property(_g6)
  target_epoch = property(_g7)
  batch_size = property(_g8)
  detect_anomalies = property(_g9)
  max_log_count = property(_g10)
  with_gradient_norm = property(_g11)
  disable_batch_norm = property(_g12)
  generate_snapshots = property(_g13)

  def to_builder(self) -> TrainParamBuilder:
    x = TrainParamBuilder()
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
    m[TrainParam._k_0] = self._0
    m[TrainParam._k_1] = self._1
    m[TrainParam._k_2] = self._2
    m[TrainParam._k_3] = self._3
    m[TrainParam._k_4] = self._4
    m[TrainParam._k_5] = self._5
    m[TrainParam._k_6] = self._6
    m[TrainParam._k_7] = self._7
    m[TrainParam._k_8] = self._8
    m[TrainParam._k_9] = self._9
    m[TrainParam._k_10] = self._10
    m[TrainParam._k_11] = self._11
    m[TrainParam._k_12] = self._12
    m[TrainParam._k_13] = self._13
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
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, TrainParam):
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


TrainParam.default_instance = TrainParam()


class TrainParamBuilder(TrainParam):

  def set_target_dir_train(self, x: str) -> TrainParamBuilder:
    self._0 = "train_data" if x is None else x
    return self

  def set_target_dir_checkpoint(self, x: str) -> TrainParamBuilder:
    self._1 = "checkpoints" if x is None else x
    return self

  def set_max_train_sets(self, x: int) -> TrainParamBuilder:
    self._2 = 3 if x is None else x
    return self

  def set_recycle(self, x: int) -> TrainParamBuilder:
    self._3 = 3 if x is None else x
    return self

  def set_max_checkpoints(self, x: int) -> TrainParamBuilder:
    self._4 = 3 if x is None else x
    return self

  def set_target_accuracy(self, x: int) -> TrainParamBuilder:
    self._5 = 95 if x is None else x
    return self

  def set_target_loss(self, x: float) -> TrainParamBuilder:
    self._6 = 0.0 if x is None else x
    return self

  def set_target_epoch(self, x: int) -> TrainParamBuilder:
    self._7 = 0 if x is None else x
    return self

  def set_batch_size(self, x: int) -> TrainParamBuilder:
    self._8 = 32 if x is None else x
    return self

  def set_detect_anomalies(self, x: bool) -> TrainParamBuilder:
    self._9 = False if x is None else x
    return self

  def set_max_log_count(self, x: int) -> TrainParamBuilder:
    self._10 = 20 if x is None else x
    return self

  def set_with_gradient_norm(self, x: bool) -> TrainParamBuilder:
    self._11 = False if x is None else x
    return self

  def set_disable_batch_norm(self, x: bool) -> TrainParamBuilder:
    self._12 = False if x is None else x
    return self

  def set_generate_snapshots(self, x: bool) -> TrainParamBuilder:
    self._13 = False if x is None else x
    return self

  target_dir_train = property(TrainParam._g0, set_target_dir_train)
  target_dir_checkpoint = property(TrainParam._g1, set_target_dir_checkpoint)
  max_train_sets = property(TrainParam._g2, set_max_train_sets)
  recycle = property(TrainParam._g3, set_recycle)
  max_checkpoints = property(TrainParam._g4, set_max_checkpoints)
  target_accuracy = property(TrainParam._g5, set_target_accuracy)
  target_loss = property(TrainParam._g6, set_target_loss)
  target_epoch = property(TrainParam._g7, set_target_epoch)
  batch_size = property(TrainParam._g8, set_batch_size)
  detect_anomalies = property(TrainParam._g9, set_detect_anomalies)
  max_log_count = property(TrainParam._g10, set_max_log_count)
  with_gradient_norm = property(TrainParam._g11, set_with_gradient_norm)
  disable_batch_norm = property(TrainParam._g12, set_disable_batch_norm)
  generate_snapshots = property(TrainParam._g13, set_generate_snapshots)

  def to_builder(self) -> TrainParamBuilder:
    return self

  def build(self) -> TrainParam:
    v = TrainParam()
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
