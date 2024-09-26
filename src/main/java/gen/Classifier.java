package gen;

import js.data.AbstractData;
import js.geometry.IPoint;
import js.json.JSMap;

public class Classifier implements AbstractData {

  public IPoint imageSize() {
    return mImageSize;
  }

  public int imageChannels() {
    return mImageChannels;
  }

  public int categoryCount() {
    return mCategoryCount;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "image_size";
  protected static final String _1 = "image_channels";
  protected static final String _2 = "category_count";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mImageSize.toJson());
    m.putUnsafe(_1, mImageChannels);
    m.putUnsafe(_2, mCategoryCount);
    return m;
  }

  @Override
  public Classifier build() {
    return this;
  }

  @Override
  public Classifier parse(Object obj) {
    return new Classifier((JSMap) obj);
  }

  private Classifier(JSMap m) {
    {
      mImageSize = IPoint.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_0);
      if (x != null) {
        mImageSize = IPoint.DEFAULT_INSTANCE.parse(x);
      }
    }
    mImageChannels = m.opt(_1, 0);
    mCategoryCount = m.opt(_2, 0);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof Classifier))
      return false;
    Classifier other = (Classifier) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mImageSize.equals(other.mImageSize)))
      return false;
    if (!(mImageChannels == other.mImageChannels))
      return false;
    if (!(mCategoryCount == other.mCategoryCount))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mImageSize.hashCode();
      r = r * 37 + mImageChannels;
      r = r * 37 + mCategoryCount;
      m__hashcode = r;
    }
    return r;
  }

  protected IPoint mImageSize;
  protected int mImageChannels;
  protected int mCategoryCount;
  protected int m__hashcode;

  public static final class Builder extends Classifier {

    private Builder(Classifier m) {
      mImageSize = m.mImageSize;
      mImageChannels = m.mImageChannels;
      mCategoryCount = m.mCategoryCount;
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
    public Classifier build() {
      Classifier r = new Classifier();
      r.mImageSize = mImageSize;
      r.mImageChannels = mImageChannels;
      r.mCategoryCount = mCategoryCount;
      return r;
    }

    public Builder imageSize(IPoint x) {
      mImageSize = (x == null) ? IPoint.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder imageChannels(int x) {
      mImageChannels = x;
      return this;
    }

    public Builder categoryCount(int x) {
      mCategoryCount = x;
      return this;
    }

  }

  public static final Classifier DEFAULT_INSTANCE = new Classifier();

  private Classifier() {
    mImageSize = IPoint.DEFAULT_INSTANCE;
  }

}
