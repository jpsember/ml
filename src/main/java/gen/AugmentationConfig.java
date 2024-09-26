package gen;

import js.data.AbstractData;
import js.json.JSMap;

public class AugmentationConfig implements AbstractData {

  public boolean horizontalFlip() {
    return mHorizontalFlip;
  }

  public boolean adjustBrightness() {
    return mAdjustBrightness;
  }

  public float brightShiftMin() {
    return mBrightShiftMin;
  }

  public float brightShiftMax() {
    return mBrightShiftMax;
  }

  public boolean shearDisable() {
    return mShearDisable;
  }

  public float shearMax() {
    return mShearMax;
  }

  public boolean scaleDisable() {
    return mScaleDisable;
  }

  public float scaleMin() {
    return mScaleMin;
  }

  public float scaleMax() {
    return mScaleMax;
  }

  public boolean rotateDisable() {
    return mRotateDisable;
  }

  public float rotateDegreesMax() {
    return mRotateDegreesMax;
  }

  public boolean translateDisable() {
    return mTranslateDisable;
  }

  public float translateRatioMax() {
    return mTranslateRatioMax;
  }

  public int blurFactor() {
    return mBlurFactor;
  }

  public String obviousModeLabels() {
    return mObviousModeLabels;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "horizontal_flip";
  protected static final String _1 = "adjust_brightness";
  protected static final String _2 = "bright_shift_min";
  protected static final String _3 = "bright_shift_max";
  protected static final String _4 = "shear_disable";
  protected static final String _5 = "shear_max";
  protected static final String _6 = "scale_disable";
  protected static final String _7 = "scale_min";
  protected static final String _8 = "scale_max";
  protected static final String _9 = "rotate_disable";
  protected static final String _10 = "rotate_degrees_max";
  protected static final String _11 = "translate_disable";
  protected static final String _12 = "translate_ratio_max";
  protected static final String _13 = "blur_factor";
  protected static final String _14 = "obvious_mode_labels";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mHorizontalFlip);
    m.putUnsafe(_1, mAdjustBrightness);
    m.putUnsafe(_2, mBrightShiftMin);
    m.putUnsafe(_3, mBrightShiftMax);
    m.putUnsafe(_4, mShearDisable);
    m.putUnsafe(_5, mShearMax);
    m.putUnsafe(_6, mScaleDisable);
    m.putUnsafe(_7, mScaleMin);
    m.putUnsafe(_8, mScaleMax);
    m.putUnsafe(_9, mRotateDisable);
    m.putUnsafe(_10, mRotateDegreesMax);
    m.putUnsafe(_11, mTranslateDisable);
    m.putUnsafe(_12, mTranslateRatioMax);
    m.putUnsafe(_13, mBlurFactor);
    m.putUnsafe(_14, mObviousModeLabels);
    return m;
  }

  @Override
  public AugmentationConfig build() {
    return this;
  }

  @Override
  public AugmentationConfig parse(Object obj) {
    return new AugmentationConfig((JSMap) obj);
  }

  private AugmentationConfig(JSMap m) {
    mHorizontalFlip = m.opt(_0, true);
    mAdjustBrightness = m.opt(_1, false);
    mBrightShiftMin = m.opt(_2, -0.1f);
    mBrightShiftMax = m.opt(_3, 0.1f);
    mShearDisable = m.opt(_4, false);
    mShearMax = m.opt(_5, 0.25f);
    mScaleDisable = m.opt(_6, false);
    mScaleMin = m.opt(_7, 0f);
    mScaleMax = m.opt(_8, 1.2f);
    mRotateDisable = m.opt(_9, false);
    mRotateDegreesMax = m.opt(_10, 8.0f);
    mTranslateDisable = m.opt(_11, false);
    mTranslateRatioMax = m.opt(_12, 0.2f);
    mBlurFactor = m.opt(_13, 0);
    mObviousModeLabels = m.opt(_14, "");
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof AugmentationConfig))
      return false;
    AugmentationConfig other = (AugmentationConfig) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mHorizontalFlip == other.mHorizontalFlip))
      return false;
    if (!(mAdjustBrightness == other.mAdjustBrightness))
      return false;
    if (!(mBrightShiftMin == other.mBrightShiftMin))
      return false;
    if (!(mBrightShiftMax == other.mBrightShiftMax))
      return false;
    if (!(mShearDisable == other.mShearDisable))
      return false;
    if (!(mShearMax == other.mShearMax))
      return false;
    if (!(mScaleDisable == other.mScaleDisable))
      return false;
    if (!(mScaleMin == other.mScaleMin))
      return false;
    if (!(mScaleMax == other.mScaleMax))
      return false;
    if (!(mRotateDisable == other.mRotateDisable))
      return false;
    if (!(mRotateDegreesMax == other.mRotateDegreesMax))
      return false;
    if (!(mTranslateDisable == other.mTranslateDisable))
      return false;
    if (!(mTranslateRatioMax == other.mTranslateRatioMax))
      return false;
    if (!(mBlurFactor == other.mBlurFactor))
      return false;
    if (!(mObviousModeLabels.equals(other.mObviousModeLabels)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + (mHorizontalFlip ? 1 : 0);
      r = r * 37 + (mAdjustBrightness ? 1 : 0);
      r = r * 37 + (int)mBrightShiftMin;
      r = r * 37 + (int)mBrightShiftMax;
      r = r * 37 + (mShearDisable ? 1 : 0);
      r = r * 37 + (int)mShearMax;
      r = r * 37 + (mScaleDisable ? 1 : 0);
      r = r * 37 + (int)mScaleMin;
      r = r * 37 + (int)mScaleMax;
      r = r * 37 + (mRotateDisable ? 1 : 0);
      r = r * 37 + (int)mRotateDegreesMax;
      r = r * 37 + (mTranslateDisable ? 1 : 0);
      r = r * 37 + (int)mTranslateRatioMax;
      r = r * 37 + mBlurFactor;
      r = r * 37 + mObviousModeLabels.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected boolean mHorizontalFlip;
  protected boolean mAdjustBrightness;
  protected float mBrightShiftMin;
  protected float mBrightShiftMax;
  protected boolean mShearDisable;
  protected float mShearMax;
  protected boolean mScaleDisable;
  protected float mScaleMin;
  protected float mScaleMax;
  protected boolean mRotateDisable;
  protected float mRotateDegreesMax;
  protected boolean mTranslateDisable;
  protected float mTranslateRatioMax;
  protected int mBlurFactor;
  protected String mObviousModeLabels;
  protected int m__hashcode;

  public static final class Builder extends AugmentationConfig {

    private Builder(AugmentationConfig m) {
      mHorizontalFlip = m.mHorizontalFlip;
      mAdjustBrightness = m.mAdjustBrightness;
      mBrightShiftMin = m.mBrightShiftMin;
      mBrightShiftMax = m.mBrightShiftMax;
      mShearDisable = m.mShearDisable;
      mShearMax = m.mShearMax;
      mScaleDisable = m.mScaleDisable;
      mScaleMin = m.mScaleMin;
      mScaleMax = m.mScaleMax;
      mRotateDisable = m.mRotateDisable;
      mRotateDegreesMax = m.mRotateDegreesMax;
      mTranslateDisable = m.mTranslateDisable;
      mTranslateRatioMax = m.mTranslateRatioMax;
      mBlurFactor = m.mBlurFactor;
      mObviousModeLabels = m.mObviousModeLabels;
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
    public AugmentationConfig build() {
      AugmentationConfig r = new AugmentationConfig();
      r.mHorizontalFlip = mHorizontalFlip;
      r.mAdjustBrightness = mAdjustBrightness;
      r.mBrightShiftMin = mBrightShiftMin;
      r.mBrightShiftMax = mBrightShiftMax;
      r.mShearDisable = mShearDisable;
      r.mShearMax = mShearMax;
      r.mScaleDisable = mScaleDisable;
      r.mScaleMin = mScaleMin;
      r.mScaleMax = mScaleMax;
      r.mRotateDisable = mRotateDisable;
      r.mRotateDegreesMax = mRotateDegreesMax;
      r.mTranslateDisable = mTranslateDisable;
      r.mTranslateRatioMax = mTranslateRatioMax;
      r.mBlurFactor = mBlurFactor;
      r.mObviousModeLabels = mObviousModeLabels;
      return r;
    }

    public Builder horizontalFlip(boolean x) {
      mHorizontalFlip = x;
      return this;
    }

    public Builder adjustBrightness(boolean x) {
      mAdjustBrightness = x;
      return this;
    }

    public Builder brightShiftMin(float x) {
      mBrightShiftMin = x;
      return this;
    }

    public Builder brightShiftMax(float x) {
      mBrightShiftMax = x;
      return this;
    }

    public Builder shearDisable(boolean x) {
      mShearDisable = x;
      return this;
    }

    public Builder shearMax(float x) {
      mShearMax = x;
      return this;
    }

    public Builder scaleDisable(boolean x) {
      mScaleDisable = x;
      return this;
    }

    public Builder scaleMin(float x) {
      mScaleMin = x;
      return this;
    }

    public Builder scaleMax(float x) {
      mScaleMax = x;
      return this;
    }

    public Builder rotateDisable(boolean x) {
      mRotateDisable = x;
      return this;
    }

    public Builder rotateDegreesMax(float x) {
      mRotateDegreesMax = x;
      return this;
    }

    public Builder translateDisable(boolean x) {
      mTranslateDisable = x;
      return this;
    }

    public Builder translateRatioMax(float x) {
      mTranslateRatioMax = x;
      return this;
    }

    public Builder blurFactor(int x) {
      mBlurFactor = x;
      return this;
    }

    public Builder obviousModeLabels(String x) {
      mObviousModeLabels = (x == null) ? "" : x;
      return this;
    }

  }

  public static final AugmentationConfig DEFAULT_INSTANCE = new AugmentationConfig();

  private AugmentationConfig() {
    mHorizontalFlip = true;
    mBrightShiftMin = -0.1f;
    mBrightShiftMax = 0.1f;
    mShearMax = 0.25f;
    mScaleMax = 1.2f;
    mRotateDegreesMax = 8.0f;
    mTranslateRatioMax = 0.2f;
    mObviousModeLabels = "";
  }

}
