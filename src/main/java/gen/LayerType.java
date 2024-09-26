package gen;

public enum LayerType {

  CONV, FC, LEAKY_RELU, MAXPOOL, OUTPUT, YOLO, CLASSIFIER;

  public static final LayerType DEFAULT_INSTANCE = CONV;

}
