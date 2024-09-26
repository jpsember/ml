package gen;

import java.io.File;
import js.data.AbstractData;
import js.file.Files;
import js.json.JSMap;

public class GenerateImagesConfig implements AbstractData {

  public File targetDir() {
    return mTargetDir;
  }

  public int imageTotal() {
    return mImageTotal;
  }

  public int seed() {
    return mSeed;
  }

  public NeuralNetwork network() {
    return mNetwork;
  }

  public File networkPath() {
    return mNetworkPath;
  }

  public String categories() {
    return mCategories;
  }

  public int maxObjects() {
    return mMaxObjects;
  }

  public AugmentationConfig augmentationConfig() {
    return mAugmentationConfig;
  }

  public int noiseFactor() {
    return mNoiseFactor;
  }

  public int fontLimit() {
    return mFontLimit;
  }

  public int colorLimit() {
    return mColorLimit;
  }

  public String bgndImage() {
    return mBgndImage;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "target_dir";
  protected static final String _1 = "image_total";
  protected static final String _2 = "seed";
  protected static final String _3 = "network";
  protected static final String _4 = "network_path";
  protected static final String _5 = "categories";
  protected static final String _6 = "max_objects";
  protected static final String _7 = "augmentation_config";
  protected static final String _8 = "noise_factor";
  protected static final String _9 = "font_limit";
  protected static final String _10 = "color_limit";
  protected static final String _11 = "bgnd_image";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mTargetDir.toString());
    m.putUnsafe(_1, mImageTotal);
    m.putUnsafe(_2, mSeed);
    if (mNetwork != null) {
      m.putUnsafe(_3, mNetwork.toJson());
    }
    m.putUnsafe(_4, mNetworkPath.toString());
    m.putUnsafe(_5, mCategories);
    m.putUnsafe(_6, mMaxObjects);
    m.putUnsafe(_7, mAugmentationConfig.toJson());
    m.putUnsafe(_8, mNoiseFactor);
    m.putUnsafe(_9, mFontLimit);
    m.putUnsafe(_10, mColorLimit);
    m.putUnsafe(_11, mBgndImage);
    return m;
  }

  @Override
  public GenerateImagesConfig build() {
    return this;
  }

  @Override
  public GenerateImagesConfig parse(Object obj) {
    return new GenerateImagesConfig((JSMap) obj);
  }

  private GenerateImagesConfig(JSMap m) {
    {
      mTargetDir = _D0;
      String x = m.opt(_0, (String) null);
      if (x != null) {
        mTargetDir = new File(x);
      }
    }
    mImageTotal = m.opt(_1, 20);
    mSeed = m.opt(_2, 0);
    {
      Object x = m.optUnsafe(_3);
      if (x != null) {
        mNetwork = NeuralNetwork.DEFAULT_INSTANCE.parse(x);
      }
    }
    {
      mNetworkPath = Files.DEFAULT;
      String x = m.opt(_4, (String) null);
      if (x != null) {
        mNetworkPath = new File(x);
      }
    }
    mCategories = m.opt(_5, "");
    mMaxObjects = m.opt(_6, 4);
    {
      mAugmentationConfig = AugmentationConfig.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_7);
      if (x != null) {
        mAugmentationConfig = AugmentationConfig.DEFAULT_INSTANCE.parse(x);
      }
    }
    mNoiseFactor = m.opt(_8, 30);
    mFontLimit = m.opt(_9, 0);
    mColorLimit = m.opt(_10, 0);
    mBgndImage = m.opt(_11, "");
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof GenerateImagesConfig))
      return false;
    GenerateImagesConfig other = (GenerateImagesConfig) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mTargetDir.equals(other.mTargetDir)))
      return false;
    if (!(mImageTotal == other.mImageTotal))
      return false;
    if (!(mSeed == other.mSeed))
      return false;
    if ((mNetwork == null) ^ (other.mNetwork == null))
      return false;
    if (mNetwork != null) {
      if (!(mNetwork.equals(other.mNetwork)))
        return false;
    }
    if (!(mNetworkPath.equals(other.mNetworkPath)))
      return false;
    if (!(mCategories.equals(other.mCategories)))
      return false;
    if (!(mMaxObjects == other.mMaxObjects))
      return false;
    if (!(mAugmentationConfig.equals(other.mAugmentationConfig)))
      return false;
    if (!(mNoiseFactor == other.mNoiseFactor))
      return false;
    if (!(mFontLimit == other.mFontLimit))
      return false;
    if (!(mColorLimit == other.mColorLimit))
      return false;
    if (!(mBgndImage.equals(other.mBgndImage)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mTargetDir.hashCode();
      r = r * 37 + mImageTotal;
      r = r * 37 + mSeed;
      if (mNetwork != null) {
        r = r * 37 + mNetwork.hashCode();
      }
      r = r * 37 + mNetworkPath.hashCode();
      r = r * 37 + mCategories.hashCode();
      r = r * 37 + mMaxObjects;
      r = r * 37 + mAugmentationConfig.hashCode();
      r = r * 37 + mNoiseFactor;
      r = r * 37 + mFontLimit;
      r = r * 37 + mColorLimit;
      r = r * 37 + mBgndImage.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected File mTargetDir;
  protected int mImageTotal;
  protected int mSeed;
  protected NeuralNetwork mNetwork;
  protected File mNetworkPath;
  protected String mCategories;
  protected int mMaxObjects;
  protected AugmentationConfig mAugmentationConfig;
  protected int mNoiseFactor;
  protected int mFontLimit;
  protected int mColorLimit;
  protected String mBgndImage;
  protected int m__hashcode;

  public static final class Builder extends GenerateImagesConfig {

    private Builder(GenerateImagesConfig m) {
      mTargetDir = m.mTargetDir;
      mImageTotal = m.mImageTotal;
      mSeed = m.mSeed;
      mNetwork = m.mNetwork;
      mNetworkPath = m.mNetworkPath;
      mCategories = m.mCategories;
      mMaxObjects = m.mMaxObjects;
      mAugmentationConfig = m.mAugmentationConfig;
      mNoiseFactor = m.mNoiseFactor;
      mFontLimit = m.mFontLimit;
      mColorLimit = m.mColorLimit;
      mBgndImage = m.mBgndImage;
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
    public GenerateImagesConfig build() {
      GenerateImagesConfig r = new GenerateImagesConfig();
      r.mTargetDir = mTargetDir;
      r.mImageTotal = mImageTotal;
      r.mSeed = mSeed;
      r.mNetwork = mNetwork;
      r.mNetworkPath = mNetworkPath;
      r.mCategories = mCategories;
      r.mMaxObjects = mMaxObjects;
      r.mAugmentationConfig = mAugmentationConfig;
      r.mNoiseFactor = mNoiseFactor;
      r.mFontLimit = mFontLimit;
      r.mColorLimit = mColorLimit;
      r.mBgndImage = mBgndImage;
      return r;
    }

    public Builder targetDir(File x) {
      mTargetDir = (x == null) ? _D0 : x;
      return this;
    }

    public Builder imageTotal(int x) {
      mImageTotal = x;
      return this;
    }

    public Builder seed(int x) {
      mSeed = x;
      return this;
    }

    public Builder network(NeuralNetwork x) {
      mNetwork = (x == null) ? null : x.build();
      return this;
    }

    public Builder networkPath(File x) {
      mNetworkPath = (x == null) ? Files.DEFAULT : x;
      return this;
    }

    public Builder categories(String x) {
      mCategories = (x == null) ? "" : x;
      return this;
    }

    public Builder maxObjects(int x) {
      mMaxObjects = x;
      return this;
    }

    public Builder augmentationConfig(AugmentationConfig x) {
      mAugmentationConfig = (x == null) ? AugmentationConfig.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder noiseFactor(int x) {
      mNoiseFactor = x;
      return this;
    }

    public Builder fontLimit(int x) {
      mFontLimit = x;
      return this;
    }

    public Builder colorLimit(int x) {
      mColorLimit = x;
      return this;
    }

    public Builder bgndImage(String x) {
      mBgndImage = (x == null) ? "" : x;
      return this;
    }

  }

  private static final File _D0 = new File("generated_images");

  public static final GenerateImagesConfig DEFAULT_INSTANCE = new GenerateImagesConfig();

  private GenerateImagesConfig() {
    mTargetDir = _D0;
    mImageTotal = 20;
    mNetworkPath = Files.DEFAULT;
    mCategories = "";
    mMaxObjects = 4;
    mAugmentationConfig = AugmentationConfig.DEFAULT_INSTANCE;
    mNoiseFactor = 30;
    mBgndImage = "";
  }

}
