package gen;

import java.util.List;
import js.data.AbstractData;
import js.data.DataUtil;
import js.geometry.IPoint;
import js.json.JSList;
import js.json.JSMap;

public class NeuralNetwork implements AbstractData {

  public int version() {
    return mVersion;
  }

  public NetworkProjectType projectType() {
    return mProjectType;
  }

  public List<Layer> layers() {
    return mLayers;
  }

  public long weightCount() {
    return mWeightCount;
  }

  public int kernelWidth() {
    return mKernelWidth;
  }

  public float alpha() {
    return mAlpha;
  }

  public IPoint stride() {
    return mStride;
  }

  public float dropoutInput() {
    return mDropoutInput;
  }

  public float dropoutHidden() {
    return mDropoutHidden;
  }

  public JSMap modelConfig() {
    return mModelConfig;
  }

  public boolean monochromeSourceImages() {
    return mMonochromeSourceImages;
  }

  public DataType imageDataType() {
    return mImageDataType;
  }

  public DataType labelDataType() {
    return mLabelDataType;
  }

  public SpecialOption specialOption() {
    return mSpecialOption;
  }

  public NetworkOptions options() {
    return mOptions;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "version";
  protected static final String _1 = "project_type";
  protected static final String _2 = "layers";
  protected static final String _3 = "weight_count";
  protected static final String _4 = "kernel_width";
  protected static final String _5 = "alpha";
  protected static final String _6 = "stride";
  protected static final String _7 = "dropout_input";
  protected static final String _8 = "dropout_hidden";
  protected static final String _9 = "model_config";
  protected static final String _10 = "monochrome_source_images";
  protected static final String _11 = "image_data_type";
  protected static final String _12 = "label_data_type";
  protected static final String _13 = "special_option";
  protected static final String _14 = "options";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mVersion);
    m.putUnsafe(_1, mProjectType.toString().toLowerCase());
    {
      JSList j = new JSList();
      for (Layer x : mLayers)
        j.add(x.toJson());
      m.put(_2, j);
    }
    m.putUnsafe(_3, mWeightCount);
    m.putUnsafe(_4, mKernelWidth);
    m.putUnsafe(_5, mAlpha);
    m.putUnsafe(_6, mStride.toJson());
    m.putUnsafe(_7, mDropoutInput);
    m.putUnsafe(_8, mDropoutHidden);
    m.putUnsafe(_9, mModelConfig);
    m.putUnsafe(_10, mMonochromeSourceImages);
    m.putUnsafe(_11, mImageDataType.toString().toLowerCase());
    m.putUnsafe(_12, mLabelDataType.toString().toLowerCase());
    m.putUnsafe(_13, mSpecialOption.toString().toLowerCase());
    m.putUnsafe(_14, mOptions.toJson());
    return m;
  }

  @Override
  public NeuralNetwork build() {
    return this;
  }

  @Override
  public NeuralNetwork parse(Object obj) {
    return new NeuralNetwork((JSMap) obj);
  }

  private NeuralNetwork(JSMap m) {
    mVersion = m.opt(_0, 0);
    {
      String x = m.opt(_1, "");
      mProjectType = x.isEmpty() ? NetworkProjectType.DEFAULT_INSTANCE : NetworkProjectType.valueOf(x.toUpperCase());
    }
    mLayers = DataUtil.parseListOfObjects(Layer.DEFAULT_INSTANCE, m.optJSList(_2), false);
    mWeightCount = m.opt(_3, 0L);
    mKernelWidth = m.opt(_4, 3);
    mAlpha = m.opt(_5, 0.01f);
    {
      mStride = _D6;
      Object x = m.optUnsafe(_6);
      if (x != null) {
        mStride = IPoint.DEFAULT_INSTANCE.parse(x);
      }
    }
    mDropoutInput = m.opt(_7, 0.2f);
    mDropoutHidden = m.opt(_8, 0.5f);
    {
      mModelConfig = JSMap.DEFAULT_INSTANCE;
      JSMap x = m.optJSMap(_9);
      if (x != null) {
        mModelConfig = x.lock();
      }
    }
    mMonochromeSourceImages = m.opt(_10, false);
    {
      String x = m.opt(_11, "");
      mImageDataType = x.isEmpty() ? DataType.DEFAULT_INSTANCE : DataType.valueOf(x.toUpperCase());
    }
    {
      String x = m.opt(_12, "");
      mLabelDataType = x.isEmpty() ? DataType.DEFAULT_INSTANCE : DataType.valueOf(x.toUpperCase());
    }
    {
      String x = m.opt(_13, "");
      mSpecialOption = x.isEmpty() ? SpecialOption.DEFAULT_INSTANCE : SpecialOption.valueOf(x.toUpperCase());
    }
    {
      mOptions = NetworkOptions.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_14);
      if (x != null) {
        mOptions = NetworkOptions.DEFAULT_INSTANCE.parse(x);
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
    if (object == null || !(object instanceof NeuralNetwork))
      return false;
    NeuralNetwork other = (NeuralNetwork) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mVersion == other.mVersion))
      return false;
    if (!(mProjectType.equals(other.mProjectType)))
      return false;
    if (!(mLayers.equals(other.mLayers)))
      return false;
    if (!(mWeightCount == other.mWeightCount))
      return false;
    if (!(mKernelWidth == other.mKernelWidth))
      return false;
    if (!(mAlpha == other.mAlpha))
      return false;
    if (!(mStride.equals(other.mStride)))
      return false;
    if (!(mDropoutInput == other.mDropoutInput))
      return false;
    if (!(mDropoutHidden == other.mDropoutHidden))
      return false;
    if (!(mModelConfig.equals(other.mModelConfig)))
      return false;
    if (!(mMonochromeSourceImages == other.mMonochromeSourceImages))
      return false;
    if (!(mImageDataType.equals(other.mImageDataType)))
      return false;
    if (!(mLabelDataType.equals(other.mLabelDataType)))
      return false;
    if (!(mSpecialOption.equals(other.mSpecialOption)))
      return false;
    if (!(mOptions.equals(other.mOptions)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mVersion;
      r = r * 37 + mProjectType.ordinal();
      for (Layer x : mLayers)
        if (x != null)
          r = r * 37 + x.hashCode();
      r = r * 37 + (int)mWeightCount;
      r = r * 37 + mKernelWidth;
      r = r * 37 + (int)mAlpha;
      r = r * 37 + mStride.hashCode();
      r = r * 37 + (int)mDropoutInput;
      r = r * 37 + (int)mDropoutHidden;
      r = r * 37 + mModelConfig.hashCode();
      r = r * 37 + (mMonochromeSourceImages ? 1 : 0);
      r = r * 37 + mImageDataType.ordinal();
      r = r * 37 + mLabelDataType.ordinal();
      r = r * 37 + mSpecialOption.ordinal();
      r = r * 37 + mOptions.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected int mVersion;
  protected NetworkProjectType mProjectType;
  protected List<Layer> mLayers;
  protected long mWeightCount;
  protected int mKernelWidth;
  protected float mAlpha;
  protected IPoint mStride;
  protected float mDropoutInput;
  protected float mDropoutHidden;
  protected JSMap mModelConfig;
  protected boolean mMonochromeSourceImages;
  protected DataType mImageDataType;
  protected DataType mLabelDataType;
  protected SpecialOption mSpecialOption;
  protected NetworkOptions mOptions;
  protected int m__hashcode;

  public static final class Builder extends NeuralNetwork {

    private Builder(NeuralNetwork m) {
      mVersion = m.mVersion;
      mProjectType = m.mProjectType;
      mLayers = DataUtil.mutableCopyOf(m.mLayers);
      mWeightCount = m.mWeightCount;
      mKernelWidth = m.mKernelWidth;
      mAlpha = m.mAlpha;
      mStride = m.mStride;
      mDropoutInput = m.mDropoutInput;
      mDropoutHidden = m.mDropoutHidden;
      mModelConfig = m.mModelConfig;
      mMonochromeSourceImages = m.mMonochromeSourceImages;
      mImageDataType = m.mImageDataType;
      mLabelDataType = m.mLabelDataType;
      mSpecialOption = m.mSpecialOption;
      mOptions = m.mOptions;
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
    public NeuralNetwork build() {
      NeuralNetwork r = new NeuralNetwork();
      r.mVersion = mVersion;
      r.mProjectType = mProjectType;
      r.mLayers = DataUtil.immutableCopyOf(mLayers);
      r.mWeightCount = mWeightCount;
      r.mKernelWidth = mKernelWidth;
      r.mAlpha = mAlpha;
      r.mStride = mStride;
      r.mDropoutInput = mDropoutInput;
      r.mDropoutHidden = mDropoutHidden;
      r.mModelConfig = mModelConfig;
      r.mMonochromeSourceImages = mMonochromeSourceImages;
      r.mImageDataType = mImageDataType;
      r.mLabelDataType = mLabelDataType;
      r.mSpecialOption = mSpecialOption;
      r.mOptions = mOptions;
      return r;
    }

    public Builder version(int x) {
      mVersion = x;
      return this;
    }

    public Builder projectType(NetworkProjectType x) {
      mProjectType = (x == null) ? NetworkProjectType.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder layers(List<Layer> x) {
      mLayers = DataUtil.mutableCopyOf((x == null) ? DataUtil.emptyList() : x);
      return this;
    }

    public Builder weightCount(long x) {
      mWeightCount = x;
      return this;
    }

    public Builder kernelWidth(int x) {
      mKernelWidth = x;
      return this;
    }

    public Builder alpha(float x) {
      mAlpha = x;
      return this;
    }

    public Builder stride(IPoint x) {
      mStride = (x == null) ? _D6 : x.build();
      return this;
    }

    public Builder dropoutInput(float x) {
      mDropoutInput = x;
      return this;
    }

    public Builder dropoutHidden(float x) {
      mDropoutHidden = x;
      return this;
    }

    public Builder modelConfig(JSMap x) {
      mModelConfig = (x == null) ? JSMap.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder monochromeSourceImages(boolean x) {
      mMonochromeSourceImages = x;
      return this;
    }

    public Builder imageDataType(DataType x) {
      mImageDataType = (x == null) ? DataType.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder labelDataType(DataType x) {
      mLabelDataType = (x == null) ? DataType.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder specialOption(SpecialOption x) {
      mSpecialOption = (x == null) ? SpecialOption.DEFAULT_INSTANCE : x;
      return this;
    }

    public Builder options(NetworkOptions x) {
      mOptions = (x == null) ? NetworkOptions.DEFAULT_INSTANCE : x.build();
      return this;
    }

  }

  private static final IPoint _D6  = new IPoint(2, 2);

  public static final NeuralNetwork DEFAULT_INSTANCE = new NeuralNetwork();

  private NeuralNetwork() {
    mProjectType = NetworkProjectType.DEFAULT_INSTANCE;
    mLayers = DataUtil.emptyList();
    mKernelWidth = 3;
    mAlpha = 0.01f;
    mStride = _D6;
    mDropoutInput = 0.2f;
    mDropoutHidden = 0.5f;
    mModelConfig = JSMap.DEFAULT_INSTANCE;
    mImageDataType = DataType.DEFAULT_INSTANCE;
    mLabelDataType = DataType.DEFAULT_INSTANCE;
    mSpecialOption = SpecialOption.DEFAULT_INSTANCE;
    mOptions = NetworkOptions.DEFAULT_INSTANCE;
  }

}
