package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class FeedConfig implements AbstractData {

  public int alg() {
    return mAlg;
  }

  public int produceTimeMs() {
    return mProduceTimeMs;
  }

  public int consumeTimeMs() {
    return mConsumeTimeMs;
  }

  public int produceSetSize() {
    return mProduceSetSize;
  }

  public int consumeSetSize() {
    return mConsumeSetSize;
  }

  public int recycle() {
    return mRecycle;
  }

  public int objConsumedTotal() {
    return mObjConsumedTotal;
  }

  public int seed() {
    return mSeed;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "alg";
  protected static final String _1 = "produce_time_ms";
  protected static final String _2 = "consume_time_ms";
  protected static final String _3 = "produce_set_size";
  protected static final String _4 = "consume_set_size";
  protected static final String _5 = "recycle";
  protected static final String _6 = "obj_consumed_total";
  protected static final String _7 = "seed";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mAlg);
    m.putUnsafe(_1, mProduceTimeMs);
    m.putUnsafe(_2, mConsumeTimeMs);
    m.putUnsafe(_3, mProduceSetSize);
    m.putUnsafe(_4, mConsumeSetSize);
    m.putUnsafe(_5, mRecycle);
    m.putUnsafe(_6, mObjConsumedTotal);
    m.putUnsafe(_7, mSeed);
    return m;
  }

  @Override
  public FeedConfig build() {
    return this;
  }

  @Override
  public FeedConfig parse(Object obj) {
    return new FeedConfig((JSMap) obj);
  }

  private FeedConfig(JSMap m) {
    mAlg = m.opt(_0, 1);
    mProduceTimeMs = m.opt(_1, 1200);
    mConsumeTimeMs = m.opt(_2, 500);
    mProduceSetSize = m.opt(_3, 3);
    mConsumeSetSize = m.opt(_4, 2);
    mRecycle = m.opt(_5, 3);
    mObjConsumedTotal = m.opt(_6, 80);
    mSeed = m.opt(_7, 1965);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof FeedConfig))
      return false;
    FeedConfig other = (FeedConfig) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mAlg == other.mAlg))
      return false;
    if (!(mProduceTimeMs == other.mProduceTimeMs))
      return false;
    if (!(mConsumeTimeMs == other.mConsumeTimeMs))
      return false;
    if (!(mProduceSetSize == other.mProduceSetSize))
      return false;
    if (!(mConsumeSetSize == other.mConsumeSetSize))
      return false;
    if (!(mRecycle == other.mRecycle))
      return false;
    if (!(mObjConsumedTotal == other.mObjConsumedTotal))
      return false;
    if (!(mSeed == other.mSeed))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mAlg;
      r = r * 37 + mProduceTimeMs;
      r = r * 37 + mConsumeTimeMs;
      r = r * 37 + mProduceSetSize;
      r = r * 37 + mConsumeSetSize;
      r = r * 37 + mRecycle;
      r = r * 37 + mObjConsumedTotal;
      r = r * 37 + mSeed;
      m__hashcode = r;
    }
    return r;
  }

  protected int mAlg;
  protected int mProduceTimeMs;
  protected int mConsumeTimeMs;
  protected int mProduceSetSize;
  protected int mConsumeSetSize;
  protected int mRecycle;
  protected int mObjConsumedTotal;
  protected int mSeed;
  protected int m__hashcode;

  public static final class Builder extends FeedConfig {

    private Builder(FeedConfig m) {
      mAlg = m.mAlg;
      mProduceTimeMs = m.mProduceTimeMs;
      mConsumeTimeMs = m.mConsumeTimeMs;
      mProduceSetSize = m.mProduceSetSize;
      mConsumeSetSize = m.mConsumeSetSize;
      mRecycle = m.mRecycle;
      mObjConsumedTotal = m.mObjConsumedTotal;
      mSeed = m.mSeed;
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
    public FeedConfig build() {
      FeedConfig r = new FeedConfig();
      r.mAlg = mAlg;
      r.mProduceTimeMs = mProduceTimeMs;
      r.mConsumeTimeMs = mConsumeTimeMs;
      r.mProduceSetSize = mProduceSetSize;
      r.mConsumeSetSize = mConsumeSetSize;
      r.mRecycle = mRecycle;
      r.mObjConsumedTotal = mObjConsumedTotal;
      r.mSeed = mSeed;
      return r;
    }

    public Builder alg(int x) {
      mAlg = x;
      return this;
    }

    public Builder produceTimeMs(int x) {
      mProduceTimeMs = x;
      return this;
    }

    public Builder consumeTimeMs(int x) {
      mConsumeTimeMs = x;
      return this;
    }

    public Builder produceSetSize(int x) {
      mProduceSetSize = x;
      return this;
    }

    public Builder consumeSetSize(int x) {
      mConsumeSetSize = x;
      return this;
    }

    public Builder recycle(int x) {
      mRecycle = x;
      return this;
    }

    public Builder objConsumedTotal(int x) {
      mObjConsumedTotal = x;
      return this;
    }

    public Builder seed(int x) {
      mSeed = x;
      return this;
    }

  }

  public static final FeedConfig DEFAULT_INSTANCE = new FeedConfig();

  private FeedConfig() {
    mAlg = 1;
    mProduceTimeMs = 1200;
    mConsumeTimeMs = 500;
    mProduceSetSize = 3;
    mConsumeSetSize = 2;
    mRecycle = 3;
    mObjConsumedTotal = 80;
    mSeed = 1965;
  }

}
