package gen;

import java.util.List;
import js.data.AbstractData;
import js.data.DataUtil;
import js.geometry.IPoint;
import js.json.JSList;
import js.json.JSMap;

public class Yolo implements AbstractData {

  public IPoint imageSize() {
    return mImageSize;
  }

  public int imageChannels() {
    return mImageChannels;
  }

  public IPoint blockSize() {
    return mBlockSize;
  }

  public int categoryCount() {
    return mCategoryCount;
  }

  public List<IPoint> anchorBoxesPixels() {
    return mAnchorBoxesPixels;
  }

  public float lambdaCoord() {
    return mLambdaCoord;
  }

  public float lambdaNoobj() {
    return mLambdaNoobj;
  }

  public float neighborFactor() {
    return mNeighborFactor;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "image_size";
  protected static final String _1 = "image_channels";
  protected static final String _2 = "block_size";
  protected static final String _3 = "category_count";
  protected static final String _4 = "anchor_boxes_pixels";
  protected static final String _5 = "lambda_coord";
  protected static final String _6 = "lambda_noobj";
  protected static final String _7 = "neighbor_factor";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mImageSize.toJson());
    m.putUnsafe(_1, mImageChannels);
    m.putUnsafe(_2, mBlockSize.toJson());
    m.putUnsafe(_3, mCategoryCount);
    {
      JSList j = new JSList();
      for (IPoint x : mAnchorBoxesPixels)
        j.add(x.toJson());
      m.put(_4, j);
    }
    m.putUnsafe(_5, mLambdaCoord);
    m.putUnsafe(_6, mLambdaNoobj);
    m.putUnsafe(_7, mNeighborFactor);
    return m;
  }

  @Override
  public Yolo build() {
    return this;
  }

  @Override
  public Yolo parse(Object obj) {
    return new Yolo((JSMap) obj);
  }

  private Yolo(JSMap m) {
    {
      mImageSize = IPoint.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_0);
      if (x != null) {
        mImageSize = IPoint.DEFAULT_INSTANCE.parse(x);
      }
    }
    mImageChannels = m.opt(_1, 0);
    {
      mBlockSize = _D2;
      Object x = m.optUnsafe(_2);
      if (x != null) {
        mBlockSize = IPoint.DEFAULT_INSTANCE.parse(x);
      }
    }
    mCategoryCount = m.opt(_3, 0);
    mAnchorBoxesPixels = DataUtil.parseListOfObjects(IPoint.DEFAULT_INSTANCE, m.optJSList(_4), false);
    mLambdaCoord = m.opt(_5, 5.0f);
    mLambdaNoobj = m.opt(_6, 0.5f);
    mNeighborFactor = m.opt(_7, 0f);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof Yolo))
      return false;
    Yolo other = (Yolo) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mImageSize.equals(other.mImageSize)))
      return false;
    if (!(mImageChannels == other.mImageChannels))
      return false;
    if (!(mBlockSize.equals(other.mBlockSize)))
      return false;
    if (!(mCategoryCount == other.mCategoryCount))
      return false;
    if (!(mAnchorBoxesPixels.equals(other.mAnchorBoxesPixels)))
      return false;
    if (!(mLambdaCoord == other.mLambdaCoord))
      return false;
    if (!(mLambdaNoobj == other.mLambdaNoobj))
      return false;
    if (!(mNeighborFactor == other.mNeighborFactor))
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
      r = r * 37 + mBlockSize.hashCode();
      r = r * 37 + mCategoryCount;
      for (IPoint x : mAnchorBoxesPixels)
        if (x != null)
          r = r * 37 + x.hashCode();
      r = r * 37 + (int)mLambdaCoord;
      r = r * 37 + (int)mLambdaNoobj;
      r = r * 37 + (int)mNeighborFactor;
      m__hashcode = r;
    }
    return r;
  }

  protected IPoint mImageSize;
  protected int mImageChannels;
  protected IPoint mBlockSize;
  protected int mCategoryCount;
  protected List<IPoint> mAnchorBoxesPixels;
  protected float mLambdaCoord;
  protected float mLambdaNoobj;
  protected float mNeighborFactor;
  protected int m__hashcode;

  public static final class Builder extends Yolo {

    private Builder(Yolo m) {
      mImageSize = m.mImageSize;
      mImageChannels = m.mImageChannels;
      mBlockSize = m.mBlockSize;
      mCategoryCount = m.mCategoryCount;
      mAnchorBoxesPixels = DataUtil.mutableCopyOf(m.mAnchorBoxesPixels);
      mLambdaCoord = m.mLambdaCoord;
      mLambdaNoobj = m.mLambdaNoobj;
      mNeighborFactor = m.mNeighborFactor;
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
    public Yolo build() {
      Yolo r = new Yolo();
      r.mImageSize = mImageSize;
      r.mImageChannels = mImageChannels;
      r.mBlockSize = mBlockSize;
      r.mCategoryCount = mCategoryCount;
      r.mAnchorBoxesPixels = DataUtil.immutableCopyOf(mAnchorBoxesPixels);
      r.mLambdaCoord = mLambdaCoord;
      r.mLambdaNoobj = mLambdaNoobj;
      r.mNeighborFactor = mNeighborFactor;
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

    public Builder blockSize(IPoint x) {
      mBlockSize = (x == null) ? _D2 : x.build();
      return this;
    }

    public Builder categoryCount(int x) {
      mCategoryCount = x;
      return this;
    }

    public Builder anchorBoxesPixels(List<IPoint> x) {
      mAnchorBoxesPixels = DataUtil.mutableCopyOf((x == null) ? DataUtil.emptyList() : x);
      return this;
    }

    public Builder lambdaCoord(float x) {
      mLambdaCoord = x;
      return this;
    }

    public Builder lambdaNoobj(float x) {
      mLambdaNoobj = x;
      return this;
    }

    public Builder neighborFactor(float x) {
      mNeighborFactor = x;
      return this;
    }

  }

  private static final IPoint _D2  = new IPoint(32, 32);

  public static final Yolo DEFAULT_INSTANCE = new Yolo();

  private Yolo() {
    mImageSize = IPoint.DEFAULT_INSTANCE;
    mBlockSize = _D2;
    mAnchorBoxesPixels = DataUtil.emptyList();
    mLambdaCoord = 5.0f;
    mLambdaNoobj = 0.5f;
  }

}
