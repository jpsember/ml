package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class Stats implements AbstractData {

  public int trainCount() {
    return mTrainCount;
  }

  public int testCount() {
    return mTestCount;
  }

  public float mean() {
    return mMean;
  }

  public float standardDeviation() {
    return mStandardDeviation;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "train_count";
  protected static final String _1 = "test_count";
  protected static final String _2 = "mean";
  protected static final String _3 = "standard_deviation";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mTrainCount);
    m.putUnsafe(_1, mTestCount);
    m.putUnsafe(_2, mMean);
    m.putUnsafe(_3, mStandardDeviation);
    return m;
  }

  @Override
  public Stats build() {
    return this;
  }

  @Override
  public Stats parse(Object obj) {
    return new Stats((JSMap) obj);
  }

  private Stats(JSMap m) {
    mTrainCount = m.opt(_0, 0);
    mTestCount = m.opt(_1, 0);
    mMean = m.opt(_2, 0f);
    mStandardDeviation = m.opt(_3, 0f);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof Stats))
      return false;
    Stats other = (Stats) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mTrainCount == other.mTrainCount))
      return false;
    if (!(mTestCount == other.mTestCount))
      return false;
    if (!(mMean == other.mMean))
      return false;
    if (!(mStandardDeviation == other.mStandardDeviation))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mTrainCount;
      r = r * 37 + mTestCount;
      r = r * 37 + (int)mMean;
      r = r * 37 + (int)mStandardDeviation;
      m__hashcode = r;
    }
    return r;
  }

  protected int mTrainCount;
  protected int mTestCount;
  protected float mMean;
  protected float mStandardDeviation;
  protected int m__hashcode;

  public static final class Builder extends Stats {

    private Builder(Stats m) {
      mTrainCount = m.mTrainCount;
      mTestCount = m.mTestCount;
      mMean = m.mMean;
      mStandardDeviation = m.mStandardDeviation;
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
    public Stats build() {
      Stats r = new Stats();
      r.mTrainCount = mTrainCount;
      r.mTestCount = mTestCount;
      r.mMean = mMean;
      r.mStandardDeviation = mStandardDeviation;
      return r;
    }

    public Builder trainCount(int x) {
      mTrainCount = x;
      return this;
    }

    public Builder testCount(int x) {
      mTestCount = x;
      return this;
    }

    public Builder mean(float x) {
      mMean = x;
      return this;
    }

    public Builder standardDeviation(float x) {
      mStandardDeviation = x;
      return this;
    }

  }

  public static final Stats DEFAULT_INSTANCE = new Stats();

  private Stats() {
  }

}
