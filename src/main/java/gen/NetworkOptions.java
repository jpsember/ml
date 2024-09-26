package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class NetworkOptions implements AbstractData {

  public float confidencePct() {
    return mConfidencePct;
  }

  public float maxIOverU() {
    return mMaxIOverU;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "confidence_pct";
  protected static final String _1 = "max_i_over_u";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mConfidencePct);
    m.putUnsafe(_1, mMaxIOverU);
    return m;
  }

  @Override
  public NetworkOptions build() {
    return this;
  }

  @Override
  public NetworkOptions parse(Object obj) {
    return new NetworkOptions((JSMap) obj);
  }

  private NetworkOptions(JSMap m) {
    mConfidencePct = m.opt(_0, 65.0f);
    mMaxIOverU = m.opt(_1, 0.4f);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof NetworkOptions))
      return false;
    NetworkOptions other = (NetworkOptions) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mConfidencePct == other.mConfidencePct))
      return false;
    if (!(mMaxIOverU == other.mMaxIOverU))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + (int)mConfidencePct;
      r = r * 37 + (int)mMaxIOverU;
      m__hashcode = r;
    }
    return r;
  }

  protected float mConfidencePct;
  protected float mMaxIOverU;
  protected int m__hashcode;

  public static final class Builder extends NetworkOptions {

    private Builder(NetworkOptions m) {
      mConfidencePct = m.mConfidencePct;
      mMaxIOverU = m.mMaxIOverU;
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
    public NetworkOptions build() {
      NetworkOptions r = new NetworkOptions();
      r.mConfidencePct = mConfidencePct;
      r.mMaxIOverU = mMaxIOverU;
      return r;
    }

    public Builder confidencePct(float x) {
      mConfidencePct = x;
      return this;
    }

    public Builder maxIOverU(float x) {
      mMaxIOverU = x;
      return this;
    }

  }

  public static final NetworkOptions DEFAULT_INSTANCE = new NetworkOptions();

  private NetworkOptions() {
    mConfidencePct = 65.0f;
    mMaxIOverU = 0.4f;
  }

}
