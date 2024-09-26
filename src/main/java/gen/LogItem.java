package gen;

import java.util.Arrays;
import js.data.AbstractData;
import js.data.DataUtil;
import js.json.JSMap;

public class LogItem implements AbstractData {

  public int id() {
    return mId;
  }

  public int familySize() {
    return mFamilySize;
  }

  public int familySlot() {
    return mFamilySlot;
  }

  public int familyId() {
    return mFamilyId;
  }

  public String message() {
    return mMessage;
  }

  public int[] shape() {
    return mShape;
  }

  public byte[] tensorBytes() {
    return mTensorBytes;
  }

  public float[] tensorFloats() {
    return mTensorFloats;
  }

  public JSMap stats() {
    return mStats;
  }

  public SpecialHandling specialHandling() {
    return mSpecialHandling;
  }

  public boolean illegalValuesFound() {
    return mIllegalValuesFound;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "id";
  protected static final String _1 = "family_size";
  protected static final String _2 = "family_slot";
  protected static final String _3 = "family_id";
  protected static final String _4 = "message";
  protected static final String _5 = "shape";
  protected static final String _6 = "tensor_bytes";
  protected static final String _7 = "tensor_floats";
  protected static final String _8 = "stats";
  protected static final String _9 = "special_handling";
  protected static final String _10 = "illegal_values_found";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mId);
    m.putUnsafe(_1, mFamilySize);
    m.putUnsafe(_2, mFamilySlot);
    m.putUnsafe(_3, mFamilyId);
    m.putUnsafe(_4, mMessage);
    m.putUnsafe(_5, DataUtil.encodeBase64Maybe(mShape));
    if (mTensorBytes != null) {
      m.putUnsafe(_6, DataUtil.encodeBase64Maybe(mTensorBytes));
    }
    if (mTensorFloats != null) {
      m.putUnsafe(_7, DataUtil.encodeBase64Maybe(mTensorFloats));
    }
    if (mStats != null) {
      m.putUnsafe(_8, mStats);
    }
    m.putUnsafe(_9, mSpecialHandling.toString().toLowerCase());
    m.putUnsafe(_10, mIllegalValuesFound);
    return m;
  }

  @Override
  public LogItem build() {
    return this;
  }

  @Override
  public LogItem parse(Object obj) {
    return new LogItem((JSMap) obj);
  }

  private LogItem(JSMap m) {
    mId = m.opt(_0, 0);
    mFamilySize = m.opt(_1, 0);
    mFamilySlot = m.opt(_2, 0);
    mFamilyId = m.opt(_3, 0);
    mMessage = m.opt(_4, "");
    {
      mShape = DataUtil.EMPTY_INT_ARRAY;
      Object x = m.optUnsafe(_5);
      if (x != null) {
        mShape = DataUtil.parseIntsFromArrayOrBase64(x);
      }
    }
    {
      Object x = m.optUnsafe(_6);
      if (x != null) {
        mTensorBytes = DataUtil.parseBytesFromArrayOrBase64(x);
      }
    }
    {
      Object x = m.optUnsafe(_7);
      if (x != null) {
        mTensorFloats = DataUtil.parseFloatsFromArrayOrBase64(x);
      }
    }
    {
      JSMap x = m.optJSMap(_8);
      if (x != null) {
        mStats = x.lock();
      }
    }
    {
      String x = m.opt(_9, "");
      mSpecialHandling = x.isEmpty() ? SpecialHandling.DEFAULT_INSTANCE : SpecialHandling.valueOf(x.toUpperCase());
    }
    mIllegalValuesFound = m.opt(_10, false);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof LogItem))
      return false;
    LogItem other = (LogItem) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mId == other.mId))
      return false;
    if (!(mFamilySize == other.mFamilySize))
      return false;
    if (!(mFamilySlot == other.mFamilySlot))
      return false;
    if (!(mFamilyId == other.mFamilyId))
      return false;
    if (!(mMessage.equals(other.mMessage)))
      return false;
    if (!(Arrays.equals(mShape, other.mShape)))
      return false;
    if ((mTensorBytes == null) ^ (other.mTensorBytes == null))
      return false;
    if (mTensorBytes != null) {
      if (!(Arrays.equals(mTensorBytes, other.mTensorBytes)))
        return false;
    }
    if ((mTensorFloats == null) ^ (other.mTensorFloats == null))
      return false;
    if (mTensorFloats != null) {
      if (!(Arrays.equals(mTensorFloats, other.mTensorFloats)))
        return false;
    }
    if ((mStats == null) ^ (other.mStats == null))
      return false;
    if (mStats != null) {
      if (!(mStats.equals(other.mStats)))
        return false;
    }
    if (!(mSpecialHandling.equals(other.mSpecialHandling)))
      return false;
    if (!(mIllegalValuesFound == other.mIllegalValuesFound))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mId;
      r = r * 37 + mFamilySize;
      r = r * 37 + mFamilySlot;
      r = r * 37 + mFamilyId;
      r = r * 37 + mMessage.hashCode();
      r = r * 37 + Arrays.hashCode(mShape);
      if (mTensorBytes != null) {
        r = r * 37 + Arrays.hashCode(mTensorBytes);
      }
      if (mTensorFloats != null) {
        r = r * 37 + Arrays.hashCode(mTensorFloats);
      }
      if (mStats != null) {
        r = r * 37 + mStats.hashCode();
      }
      r = r * 37 + mSpecialHandling.ordinal();
      r = r * 37 + (mIllegalValuesFound ? 1 : 0);
      m__hashcode = r;
    }
    return r;
  }

  protected int mId;
  protected int mFamilySize;
  protected int mFamilySlot;
  protected int mFamilyId;
  protected String mMessage;
  protected int[] mShape;
  protected byte[] mTensorBytes;
  protected float[] mTensorFloats;
  protected JSMap mStats;
  protected SpecialHandling mSpecialHandling;
  protected boolean mIllegalValuesFound;
  protected int m__hashcode;

  public static final class Builder extends LogItem {

    private Builder(LogItem m) {
      mId = m.mId;
      mFamilySize = m.mFamilySize;
      mFamilySlot = m.mFamilySlot;
      mFamilyId = m.mFamilyId;
      mMessage = m.mMessage;
      mShape = m.mShape;
      mTensorBytes = m.mTensorBytes;
      mTensorFloats = m.mTensorFloats;
      mStats = m.mStats;
      mSpecialHandling = m.mSpecialHandling;
      mIllegalValuesFound = m.mIllegalValuesFound;
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
    public LogItem build() {
      LogItem r = new LogItem();
      r.mId = mId;
      r.mFamilySize = mFamilySize;
      r.mFamilySlot = mFamilySlot;
      r.mFamilyId = mFamilyId;
      r.mMessage = mMessage;
      r.mShape = mShape;
      r.mTensorBytes = mTensorBytes;
      r.mTensorFloats = mTensorFloats;
      r.mStats = mStats;
      r.mSpecialHandling = mSpecialHandling;
      r.mIllegalValuesFound = mIllegalValuesFound;
      return r;
    }

    public Builder id(int x) {
      mId = x;
      return this;
    }

    public Builder familySize(int x) {
      mFamilySize = x;
      return this;
    }

    public Builder familySlot(int x) {
      mFamilySlot = x;
      return this;
    }

    public Builder familyId(int x) {
      mFamilyId = x;
      return this;
    }

    public Builder message(String x) {
      mMessage = (x == null) ? "" : x;
      return this;
    }

    public Builder shape(int[] x) {
      mShape = (x == null) ? DataUtil.EMPTY_INT_ARRAY : x;
      return this;
    }

    public Builder tensorBytes(byte[] x) {
      mTensorBytes = (x == null) ? null : x;
      return this;
    }

    public Builder tensorFloats(float[] x) {
      mTensorFloats = x;
      return this;
    }

    public Builder stats(JSMap x) {
      mStats = x;
      return this;
    }

    public Builder specialHandling(SpecialHandling x) {
      mSpecialHandling = (x == null) ? SpecialHandling.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder illegalValuesFound(boolean x) {
      mIllegalValuesFound = x;
      return this;
    }

  }

  public static final LogItem DEFAULT_INSTANCE = new LogItem();

  private LogItem() {
    mMessage = "";
    mShape = DataUtil.EMPTY_INT_ARRAY;
    mSpecialHandling = SpecialHandling.DEFAULT_INSTANCE;
  }

}
