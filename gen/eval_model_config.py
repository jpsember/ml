from __future__ import annotations
from gen.neural_network import NeuralNetwork
from pycore.base import AbstractData


class EvalModelConfig(AbstractData):

  default_instance: EvalModelConfig

  _k_0 = "network"
  _k_1 = "network_path"
  _k_2 = "train_test_dir"
  _k_3 = "eval_dir"

  def __init__(self):
    self._h = None
    self._0 = None
    self._1 = ""
    self._2 = "test_data"
    self._3 = "evaluation"

  @classmethod
  def new_builder(cls) -> EvalModelConfigBuilder:
    return EvalModelConfigBuilder()

  def parse(self, obj: dict) -> EvalModelConfig:
    inst = EvalModelConfig()
    x = obj.get(EvalModelConfig._k_0)
    if x is not None:
      inst._0 = NeuralNetwork.default_instance.parse(x)
    inst._1 = obj.get(EvalModelConfig._k_1, "")
    inst._2 = obj.get(EvalModelConfig._k_2, "test_data")
    inst._3 = obj.get(EvalModelConfig._k_3, "evaluation")
    return inst

  def _g0(self) -> NeuralNetwork:
    return self._0

  def _g1(self) -> str:
    return self._1

  def _g2(self) -> str:
    return self._2

  def _g3(self) -> str:
    return self._3

  network = property(_g0)
  network_path = property(_g1)
  train_test_dir = property(_g2)
  eval_dir = property(_g3)

  def to_builder(self) -> EvalModelConfigBuilder:
    x = EvalModelConfigBuilder()
    x._0 = self._0
    x._1 = self._1
    x._2 = self._2
    x._3 = self._3
    return x

  def to_json(self) -> dict:
    m = {}
    if self._0 is not None:
      m[EvalModelConfig._k_0] = self._0.to_json()
    m[EvalModelConfig._k_1] = self._1
    m[EvalModelConfig._k_2] = self._2
    m[EvalModelConfig._k_3] = self._3
    return m

  def __hash__(self) -> int:
    if self._h is None:
      r = hash(self._1)
      r = r * 37 + hash(self._2)
      r = r * 37 + hash(self._3)
      r = r * 37 + hash(self._0)
      self._h = r
    return self._h

  def __eq__(self, other) -> bool:
    if isinstance(other, EvalModelConfig):
      return hash(self) == hash(other)\
        and self._0 == other._0\
        and self._1 == other._1\
        and self._2 == other._2\
        and self._3 == other._3
    else:
      return False


EvalModelConfig.default_instance = EvalModelConfig()


class EvalModelConfigBuilder(EvalModelConfig):

  def set_network(self, x: NeuralNetwork) -> EvalModelConfigBuilder:
    if x is not None:
      x = x.build()
    self._0 = x
    return self

  def set_network_path(self, x: str) -> EvalModelConfigBuilder:
    self._1 = "" if x is None else x
    return self

  def set_train_test_dir(self, x: str) -> EvalModelConfigBuilder:
    self._2 = "test_data" if x is None else x
    return self

  def set_eval_dir(self, x: str) -> EvalModelConfigBuilder:
    self._3 = "evaluation" if x is None else x
    return self

  network = property(EvalModelConfig._g0, set_network)
  network_path = property(EvalModelConfig._g1, set_network_path)
  train_test_dir = property(EvalModelConfig._g2, set_train_test_dir)
  eval_dir = property(EvalModelConfig._g3, set_eval_dir)

  def to_builder(self) -> EvalModelConfigBuilder:
    return self

  def build(self) -> EvalModelConfig:
    v = EvalModelConfig()
    v._0 = self._0
    v._1 = self._1
    v._2 = self._2
    v._3 = self._3
    return v
