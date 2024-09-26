package gen;

import js.data.AbstractData;
import js.geometry.IPoint;
import js.json.JSMap;

public class Layer implements AbstractData {

  public LayerType type() {
    return mType;
  }

  public Integer kernelWidth() {
    return mKernelWidth;
  }

  public int filters() {
    return mFilters;
  }

  public boolean pool() {
    return mPool;
  }

  public Float alpha() {
    return mAlpha;
  }

  public IPoint stride() {
    return mStride;
  }

  public Float dropout() {
    return mDropout;
  }

  public boolean batchNorm() {
    return mBatchNorm;
  }

  public int numWeights() {
    return mNumWeights;
  }

  public Vol inputVolume() {
    return mInputVolume;
  }

  public Vol outputVolume() {
    return mOutputVolume;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "type";
  protected static final String _1 = "kernel_width";
  protected static final String _2 = "filters";
  protected static final String _3 = "pool";
  protected static final String _4 = "alpha";
  protected static final String _5 = "stride";
  protected static final String _6 = "dropout";
  protected static final String _7 = "batch_norm";
  protected static final String _8 = "num_weights";
  protected static final String _9 = "input_volume";
  protected static final String _10 = "output_volume";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mType.toString().toLowerCase());
    if (mKernelWidth != null) {
      m.putUnsafe(_1, mKernelWidth);
    }
    m.putUnsafe(_2, mFilters);
    m.putUnsafe(_3, mPool);
    if (mAlpha != null) {
      m.putUnsafe(_4, mAlpha);
    }
    if (mStride != null) {
      m.putUnsafe(_5, mStride.toJson());
    }
    if (mDropout != null) {
      m.putUnsafe(_6, mDropout);
    }
    m.putUnsafe(_7, mBatchNorm);
    m.putUnsafe(_8, mNumWeights);
    m.putUnsafe(_9, mInputVolume.toJson());
    m.putUnsafe(_10, mOutputVolume.toJson());
    return m;
  }

  @Override
  public Layer build() {
    return this;
  }

  @Override
  public Layer parse(Object obj) {
    return new Layer((JSMap) obj);
  }

  private Layer(JSMap m) {
    {
      String x = m.opt(_0, "");
      mType = x.isEmpty() ? LayerType.DEFAULT_INSTANCE : LayerType.valueOf(x.toUpperCase());
    }
    mKernelWidth = m.optInt(_1);
    mFilters = m.opt(_2, 0);
    mPool = m.opt(_3, false);
    mAlpha = m.optFloat(_4);
    {
      Object x = m.optUnsafe(_5);
      if (x != null) {
        mStride = IPoint.DEFAULT_INSTANCE.parse(x);
      }
    }
    mDropout = m.optFloat(_6);
    mBatchNorm = m.opt(_7, false);
    mNumWeights = m.opt(_8, 0);
    {
      mInputVolume = Vol.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_9);
      if (x != null) {
        mInputVolume = Vol.DEFAULT_INSTANCE.parse(x);
      }
    }
    {
      mOutputVolume = Vol.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_10);
      if (x != null) {
        mOutputVolume = Vol.DEFAULT_INSTANCE.parse(x);
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
    if (object == null || !(object instanceof Layer))
      return false;
    Layer other = (Layer) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mType.equals(other.mType)))
      return false;
    if ((mKernelWidth == null) ^ (other.mKernelWidth == null))
      return false;
    if (mKernelWidth != null) {
      if (!(mKernelWidth.equals(other.mKernelWidth)))
        return false;
    }
    if (!(mFilters == other.mFilters))
      return false;
    if (!(mPool == other.mPool))
      return false;
    if ((mAlpha == null) ^ (other.mAlpha == null))
      return false;
    if (mAlpha != null) {
      if (!(mAlpha.equals(other.mAlpha)))
        return false;
    }
    if ((mStride == null) ^ (other.mStride == null))
      return false;
    if (mStride != null) {
      if (!(mStride.equals(other.mStride)))
        return false;
    }
    if ((mDropout == null) ^ (other.mDropout == null))
      return false;
    if (mDropout != null) {
      if (!(mDropout.equals(other.mDropout)))
        return false;
    }
    if (!(mBatchNorm == other.mBatchNorm))
      return false;
    if (!(mNumWeights == other.mNumWeights))
      return false;
    if (!(mInputVolume.equals(other.mInputVolume)))
      return false;
    if (!(mOutputVolume.equals(other.mOutputVolume)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mType.ordinal();
      if (mKernelWidth != null) {
        r = r * 37 + mKernelWidth;
      }
      r = r * 37 + mFilters;
      r = r * 37 + (mPool ? 1 : 0);
      if (mAlpha != null) {
        r = r * 37 + mAlpha.hashCode();
      }
      if (mStride != null) {
        r = r * 37 + mStride.hashCode();
      }
      if (mDropout != null) {
        r = r * 37 + mDropout.hashCode();
      }
      r = r * 37 + (mBatchNorm ? 1 : 0);
      r = r * 37 + mNumWeights;
      r = r * 37 + mInputVolume.hashCode();
      r = r * 37 + mOutputVolume.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected LayerType mType;
  protected Integer mKernelWidth;
  protected int mFilters;
  protected boolean mPool;
  protected Float mAlpha;
  protected IPoint mStride;
  protected Float mDropout;
  protected boolean mBatchNorm;
  protected int mNumWeights;
  protected Vol mInputVolume;
  protected Vol mOutputVolume;
  protected int m__hashcode;

  public static final class Builder extends Layer {

    private Builder(Layer m) {
      mType = m.mType;
      mKernelWidth = m.mKernelWidth;
      mFilters = m.mFilters;
      mPool = m.mPool;
      mAlpha = m.mAlpha;
      mStride = m.mStride;
      mDropout = m.mDropout;
      mBatchNorm = m.mBatchNorm;
      mNumWeights = m.mNumWeights;
      mInputVolume = m.mInputVolume;
      mOutputVolume = m.mOutputVolume;
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
    public Layer build() {
      Layer r = new Layer();
      r.mType = mType;
      r.mKernelWidth = mKernelWidth;
      r.mFilters = mFilters;
      r.mPool = mPool;
      r.mAlpha = mAlpha;
      r.mStride = mStride;
      r.mDropout = mDropout;
      r.mBatchNorm = mBatchNorm;
      r.mNumWeights = mNumWeights;
      r.mInputVolume = mInputVolume;
      r.mOutputVolume = mOutputVolume;
      return r;
    }

    public Builder type(LayerType x) {
      mType = (x == null) ? LayerType.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder kernelWidth(Integer x) {
      mKernelWidth = x;
      return this;
    }

    public Builder filters(int x) {
      mFilters = x;
      return this;
    }

    public Builder pool(boolean x) {
      mPool = x;
      return this;
    }

    public Builder alpha(Float x) {
      mAlpha = x;
      return this;
    }

    public Builder stride(IPoint x) {
      mStride = (x == null) ? null : x.build();
      return this;
    }

    public Builder dropout(Float x) {
      mDropout = x;
      return this;
    }

    public Builder batchNorm(boolean x) {
      mBatchNorm = x;
      return this;
    }

    public Builder numWeights(int x) {
      mNumWeights = x;
      return this;
    }

    public Builder inputVolume(Vol x) {
      mInputVolume = (x == null) ? Vol.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder outputVolume(Vol x) {
      mOutputVolume = (x == null) ? Vol.DEFAULT_INSTANCE : x.build();
      return this;
    }

  }

  public static final Layer DEFAULT_INSTANCE = new Layer();

  private Layer() {
    mType = LayerType.DEFAULT_INSTANCE;
    mInputVolume = Vol.DEFAULT_INSTANCE;
    mOutputVolume = Vol.DEFAULT_INSTANCE;
  }

}
