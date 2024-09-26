package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class TensorStats implements AbstractData {

  public int population() {
    return mPopulation;
  }

  public float min() {
    return mMin;
  }

  public float max() {
    return mMax;
  }

  public float mean() {
    return mMean;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "population";
  protected static final String _1 = "min";
  protected static final String _2 = "max";
  protected static final String _3 = "mean";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mPopulation);
    m.putUnsafe(_1, mMin);
    m.putUnsafe(_2, mMax);
    m.putUnsafe(_3, mMean);
    return m;
  }

  @Override
  public TensorStats build() {
    return this;
  }

  @Override
  public TensorStats parse(Object obj) {
    return new TensorStats((JSMap) obj);
  }

  private TensorStats(JSMap m) {
    mPopulation = m.opt(_0, 0);
    mMin = m.opt(_1, 0f);
    mMax = m.opt(_2, 0f);
    mMean = m.opt(_3, 0f);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof TensorStats))
      return false;
    TensorStats other = (TensorStats) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mPopulation == other.mPopulation))
      return false;
    if (!(mMin == other.mMin))
      return false;
    if (!(mMax == other.mMax))
      return false;
    if (!(mMean == other.mMean))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mPopulation;
      r = r * 37 + (int)mMin;
      r = r * 37 + (int)mMax;
      r = r * 37 + (int)mMean;
      m__hashcode = r;
    }
    return r;
  }

  protected int mPopulation;
  protected float mMin;
  protected float mMax;
  protected float mMean;
  protected int m__hashcode;

  public static final class Builder extends TensorStats {

    private Builder(TensorStats m) {
      mPopulation = m.mPopulation;
      mMin = m.mMin;
      mMax = m.mMax;
      mMean = m.mMean;
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
    public TensorStats build() {
      TensorStats r = new TensorStats();
      r.mPopulation = mPopulation;
      r.mMin = mMin;
      r.mMax = mMax;
      r.mMean = mMean;
      return r;
    }

    public Builder population(int x) {
      mPopulation = x;
      return this;
    }

    public Builder min(float x) {
      mMin = x;
      return this;
    }

    public Builder max(float x) {
      mMax = x;
      return this;
    }

    public Builder mean(float x) {
      mMean = x;
      return this;
    }

  }

  public static final TensorStats DEFAULT_INSTANCE = new TensorStats();

  private TensorStats() {
  }

}
