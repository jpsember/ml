package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class ImageSetInfo implements AbstractData {

  public int imageCount() {
    return mImageCount;
  }

  public int imageLengthBytes() {
    return mImageLengthBytes;
  }

  public int labelLengthBytes() {
    return mLabelLengthBytes;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "image_count";
  protected static final String _1 = "image_length_bytes";
  protected static final String _2 = "label_length_bytes";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mImageCount);
    m.putUnsafe(_1, mImageLengthBytes);
    m.putUnsafe(_2, mLabelLengthBytes);
    return m;
  }

  @Override
  public ImageSetInfo build() {
    return this;
  }

  @Override
  public ImageSetInfo parse(Object obj) {
    return new ImageSetInfo((JSMap) obj);
  }

  private ImageSetInfo(JSMap m) {
    mImageCount = m.opt(_0, 0);
    mImageLengthBytes = m.opt(_1, 0);
    mLabelLengthBytes = m.opt(_2, 0);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof ImageSetInfo))
      return false;
    ImageSetInfo other = (ImageSetInfo) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mImageCount == other.mImageCount))
      return false;
    if (!(mImageLengthBytes == other.mImageLengthBytes))
      return false;
    if (!(mLabelLengthBytes == other.mLabelLengthBytes))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mImageCount;
      r = r * 37 + mImageLengthBytes;
      r = r * 37 + mLabelLengthBytes;
      m__hashcode = r;
    }
    return r;
  }

  protected int mImageCount;
  protected int mImageLengthBytes;
  protected int mLabelLengthBytes;
  protected int m__hashcode;

  public static final class Builder extends ImageSetInfo {

    private Builder(ImageSetInfo m) {
      mImageCount = m.mImageCount;
      mImageLengthBytes = m.mImageLengthBytes;
      mLabelLengthBytes = m.mLabelLengthBytes;
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
    public ImageSetInfo build() {
      ImageSetInfo r = new ImageSetInfo();
      r.mImageCount = mImageCount;
      r.mImageLengthBytes = mImageLengthBytes;
      r.mLabelLengthBytes = mLabelLengthBytes;
      return r;
    }

    public Builder imageCount(int x) {
      mImageCount = x;
      return this;
    }

    public Builder imageLengthBytes(int x) {
      mImageLengthBytes = x;
      return this;
    }

    public Builder labelLengthBytes(int x) {
      mLabelLengthBytes = x;
      return this;
    }

  }

  public static final ImageSetInfo DEFAULT_INSTANCE = new ImageSetInfo();

  private ImageSetInfo() {
  }

}
