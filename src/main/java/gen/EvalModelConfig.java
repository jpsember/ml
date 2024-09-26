package gen;

import java.io.File;
import js.data.AbstractData;
import js.file.Files;
import js.json.JSMap;

public class EvalModelConfig implements AbstractData {

  public NeuralNetwork network() {
    return mNetwork;
  }

  public File networkPath() {
    return mNetworkPath;
  }

  public File trainTestDir() {
    return mTrainTestDir;
  }

  public File evalDir() {
    return mEvalDir;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "network";
  protected static final String _1 = "network_path";
  protected static final String _2 = "train_test_dir";
  protected static final String _3 = "eval_dir";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    if (mNetwork != null) {
      m.putUnsafe(_0, mNetwork.toJson());
    }
    m.putUnsafe(_1, mNetworkPath.toString());
    m.putUnsafe(_2, mTrainTestDir.toString());
    m.putUnsafe(_3, mEvalDir.toString());
    return m;
  }

  @Override
  public EvalModelConfig build() {
    return this;
  }

  @Override
  public EvalModelConfig parse(Object obj) {
    return new EvalModelConfig((JSMap) obj);
  }

  private EvalModelConfig(JSMap m) {
    {
      Object x = m.optUnsafe(_0);
      if (x != null) {
        mNetwork = NeuralNetwork.DEFAULT_INSTANCE.parse(x);
      }
    }
    {
      mNetworkPath = Files.DEFAULT;
      String x = m.opt(_1, (String) null);
      if (x != null) {
        mNetworkPath = new File(x);
      }
    }
    {
      mTrainTestDir = _D2;
      String x = m.opt(_2, (String) null);
      if (x != null) {
        mTrainTestDir = new File(x);
      }
    }
    {
      mEvalDir = _D3;
      String x = m.opt(_3, (String) null);
      if (x != null) {
        mEvalDir = new File(x);
      }
    }
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof EvalModelConfig))
      return false;
    EvalModelConfig other = (EvalModelConfig) object;
    if (other.hashCode() != hashCode())
      return false;
    if ((mNetwork == null) ^ (other.mNetwork == null))
      return false;
    if (mNetwork != null) {
      if (!(mNetwork.equals(other.mNetwork)))
        return false;
    }
    if (!(mNetworkPath.equals(other.mNetworkPath)))
      return false;
    if (!(mTrainTestDir.equals(other.mTrainTestDir)))
      return false;
    if (!(mEvalDir.equals(other.mEvalDir)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      if (mNetwork != null) {
        r = r * 37 + mNetwork.hashCode();
      }
      r = r * 37 + mNetworkPath.hashCode();
      r = r * 37 + mTrainTestDir.hashCode();
      r = r * 37 + mEvalDir.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected NeuralNetwork mNetwork;
  protected File mNetworkPath;
  protected File mTrainTestDir;
  protected File mEvalDir;
  protected int m__hashcode;

  public static final class Builder extends EvalModelConfig {

    private Builder(EvalModelConfig m) {
      mNetwork = m.mNetwork;
      mNetworkPath = m.mNetworkPath;
      mTrainTestDir = m.mTrainTestDir;
      mEvalDir = m.mEvalDir;
    }

    @Override
    public Builder toBuilder() {
      return this;
    }

    @Override
    public int hashCode() {
      m__hashcode = 0;
      return super.hashCode();
    }

    @Override
    public EvalModelConfig build() {
      EvalModelConfig r = new EvalModelConfig();
      r.mNetwork = mNetwork;
      r.mNetworkPath = mNetworkPath;
      r.mTrainTestDir = mTrainTestDir;
      r.mEvalDir = mEvalDir;
      return r;
    }

    public Builder network(NeuralNetwork x) {
      mNetwork = (x == null) ? null : x.build();
      return this;
    }

    public Builder networkPath(File x) {
      mNetworkPath = (x == null) ? Files.DEFAULT : x;
      return this;
    }

    public Builder trainTestDir(File x) {
      mTrainTestDir = (x == null) ? _D2 : x;
      return this;
    }

    public Builder evalDir(File x) {
      mEvalDir = (x == null) ? _D3 : x;
      return this;
    }

  }

  private static final File _D2 = new File("test_data");
  private static final File _D3 = new File("evaluation");

  public static final EvalModelConfig DEFAULT_INSTANCE = new EvalModelConfig();

  private EvalModelConfig() {
    mNetworkPath = Files.DEFAULT;
    mTrainTestDir = _D2;
    mEvalDir = _D3;
  }

}
