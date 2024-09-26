package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class FloatFormat implements AbstractData {

  public String formatStr() {
    return mFormatStr;
  }

  public float maxValue() {
    return mMaxValue;
  }

  public float minValue() {
    return mMinValue;
  }

  public String zeroStr() {
    return mZeroStr;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "format_str";
  protected static final String _1 = "max_value";
  protected static final String _2 = "min_value";
  protected static final String _3 = "zero_str";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mFormatStr);
    m.putUnsafe(_1, mMaxValue);
    m.putUnsafe(_2, mMinValue);
    m.putUnsafe(_3, mZeroStr);
    return m;
  }

  @Override
  public FloatFormat build() {
    return this;
  }

  @Override
  public FloatFormat parse(Object obj) {
    return new FloatFormat((JSMap) obj);
  }

  private FloatFormat(JSMap m) {
    mFormatStr = m.opt(_0, "");
    mMaxValue = m.opt(_1, 0f);
    mMinValue = m.opt(_2, 0f);
    mZeroStr = m.opt(_3, "");
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof FloatFormat))
      return false;
    FloatFormat other = (FloatFormat) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mFormatStr.equals(other.mFormatStr)))
      return false;
    if (!(mMaxValue == other.mMaxValue))
      return false;
    if (!(mMinValue == other.mMinValue))
      return false;
    if (!(mZeroStr.equals(other.mZeroStr)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mFormatStr.hashCode();
      r = r * 37 + (int)mMaxValue;
      r = r * 37 + (int)mMinValue;
      r = r * 37 + mZeroStr.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected String mFormatStr;
  protected float mMaxValue;
  protected float mMinValue;
  protected String mZeroStr;
  protected int m__hashcode;

  public static final class Builder extends FloatFormat {

    private Builder(FloatFormat m) {
      mFormatStr = m.mFormatStr;
      mMaxValue = m.mMaxValue;
      mMinValue = m.mMinValue;
      mZeroStr = m.mZeroStr;
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
    public FloatFormat build() {
      FloatFormat r = new FloatFormat();
      r.mFormatStr = mFormatStr;
      r.mMaxValue = mMaxValue;
      r.mMinValue = mMinValue;
      r.mZeroStr = mZeroStr;
      return r;
    }

    public Builder formatStr(String x) {
      mFormatStr = (x == null) ? "" : x;
      return this;
    }

    public Builder maxValue(float x) {
      mMaxValue = x;
      return this;
    }

    public Builder minValue(float x) {
      mMinValue = x;
      return this;
    }

    public Builder zeroStr(String x) {
      mZeroStr = (x == null) ? "" : x;
      return this;
    }

  }

  public static final FloatFormat DEFAULT_INSTANCE = new FloatFormat();

  private FloatFormat() {
    mFormatStr = "";
    mZeroStr = "";
  }

}
