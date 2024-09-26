package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class Vol implements AbstractData {

  public int width() {
    return mWidth;
  }

  public int height() {
    return mHeight;
  }

  public int depth() {
    return mDepth;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "width";
  protected static final String _1 = "height";
  protected static final String _2 = "depth";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mWidth);
    m.putUnsafe(_1, mHeight);
    m.putUnsafe(_2, mDepth);
    return m;
  }

  @Override
  public Vol build() {
    return this;
  }

  @Override
  public Vol parse(Object obj) {
    return new Vol((JSMap) obj);
  }

  private Vol(JSMap m) {
    mWidth = m.opt(_0, 0);
    mHeight = m.opt(_1, 0);
    mDepth = m.opt(_2, 0);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof Vol))
      return false;
    Vol other = (Vol) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mWidth == other.mWidth))
      return false;
    if (!(mHeight == other.mHeight))
      return false;
    if (!(mDepth == other.mDepth))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mWidth;
      r = r * 37 + mHeight;
      r = r * 37 + mDepth;
      m__hashcode = r;
    }
    return r;
  }

  protected int mWidth;
  protected int mHeight;
  protected int mDepth;
  protected int m__hashcode;

  public static final class Builder extends Vol {

    private Builder(Vol m) {
      mWidth = m.mWidth;
      mHeight = m.mHeight;
      mDepth = m.mDepth;
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
    public Vol build() {
      Vol r = new Vol();
      r.mWidth = mWidth;
      r.mHeight = mHeight;
      r.mDepth = mDepth;
      return r;
    }

    public Builder width(int x) {
      mWidth = x;
      return this;
    }

    public Builder height(int x) {
      mHeight = x;
      return this;
    }

    public Builder depth(int x) {
      mDepth = x;
      return this;
    }

  }

  public static final Vol DEFAULT_INSTANCE = new Vol();

  private Vol() {
  }

}
