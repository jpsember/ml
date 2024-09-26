package gen;

import java.io.File;
import js.data.AbstractData;
import js.file.Files;
import js.json.JSMap;

public class CompileImagesConfig implements AbstractData {

  public CompileOper oper() {
    return mOper;
  }

  public NeuralNetwork network() {
    return mNetwork;
  }

  public File networkPath() {
    return mNetworkPath;
  }

  public File sourceDir() {
    return mSourceDir;
  }

  public AugmentationConfig augmentationConfig() {
    return mAugmentationConfig;
  }

  public int seed() {
    return mSeed;
  }

  public File targetDirModel() {
    return mTargetDirModel;
  }

  public File inspectionDir() {
    return mInspectionDir;
  }

  public TrainParam trainParam() {
    return mTrainParam;
  }

  public File snapshotDir() {
    return mSnapshotDir;
  }

  public File progressFile() {
    return mProgressFile;
  }

  public File inferenceDir() {
    return mInferenceDir;
  }

  public int maxImageCount() {
    return mMaxImageCount;
  }

  public int inactivityTimeoutSeconds() {
    return mInactivityTimeoutSeconds;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "oper";
  protected static final String _1 = "network";
  protected static final String _2 = "network_path";
  protected static final String _3 = "source_dir";
  protected static final String _4 = "augmentation_config";
  protected static final String _5 = "seed";
  protected static final String _6 = "target_dir_model";
  protected static final String _7 = "inspection_dir";
  protected static final String _8 = "train_param";
  protected static final String _9 = "snapshot_dir";
  protected static final String _10 = "progress_file";
  protected static final String _11 = "inference_dir";
  protected static final String _12 = "max_image_count";
  protected static final String _13 = "inactivity_timeout_seconds";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mOper.toString().toLowerCase());
    if (mNetwork != null) {
      m.putUnsafe(_1, mNetwork.toJson());
    }
    m.putUnsafe(_2, mNetworkPath.toString());
    m.putUnsafe(_3, mSourceDir.toString());
    m.putUnsafe(_4, mAugmentationConfig.toJson());
    m.putUnsafe(_5, mSeed);
    m.putUnsafe(_6, mTargetDirModel.toString());
    m.putUnsafe(_7, mInspectionDir.toString());
    m.putUnsafe(_8, mTrainParam.toJson());
    m.putUnsafe(_9, mSnapshotDir.toString());
    m.putUnsafe(_10, mProgressFile.toString());
    m.putUnsafe(_11, mInferenceDir.toString());
    m.putUnsafe(_12, mMaxImageCount);
    m.putUnsafe(_13, mInactivityTimeoutSeconds);
    return m;
  }

  @Override
  public CompileImagesConfig build() {
    return this;
  }

  @Override
  public CompileImagesConfig parse(Object obj) {
    return new CompileImagesConfig((JSMap) obj);
  }

  private CompileImagesConfig(JSMap m) {
    {
      String x = m.opt(_0, "");
      mOper = x.isEmpty() ? CompileOper.DEFAULT_INSTANCE : CompileOper.valueOf(x.toUpperCase());
    }
    {
      Object x = m.optUnsafe(_1);
      if (x != null) {
        mNetwork = NeuralNetwork.DEFAULT_INSTANCE.parse(x);
      }
    }
    {
      mNetworkPath = Files.DEFAULT;
      String x = m.opt(_2, (String) null);
      if (x != null) {
        mNetworkPath = new File(x);
      }
    }
    {
      mSourceDir = Files.DEFAULT;
      String x = m.opt(_3, (String) null);
      if (x != null) {
        mSourceDir = new File(x);
      }
    }
    {
      mAugmentationConfig = AugmentationConfig.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_4);
      if (x != null) {
        mAugmentationConfig = AugmentationConfig.DEFAULT_INSTANCE.parse(x);
      }
    }
    mSeed = m.opt(_5, 0);
    {
      mTargetDirModel = _D6;
      String x = m.opt(_6, (String) null);
      if (x != null) {
        mTargetDirModel = new File(x);
      }
    }
    {
      mInspectionDir = Files.DEFAULT;
      String x = m.opt(_7, (String) null);
      if (x != null) {
        mInspectionDir = new File(x);
      }
    }
    {
      mTrainParam = TrainParam.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_8);
      if (x != null) {
        mTrainParam = TrainParam.DEFAULT_INSTANCE.parse(x);
      }
    }
    {
      mSnapshotDir = Files.DEFAULT;
      String x = m.opt(_9, (String) null);
      if (x != null) {
        mSnapshotDir = new File(x);
      }
    }
    {
      mProgressFile = _D10;
      String x = m.opt(_10, (String) null);
      if (x != null) {
        mProgressFile = new File(x);
      }
    }
    {
      mInferenceDir = _D11;
      String x = m.opt(_11, (String) null);
      if (x != null) {
        mInferenceDir = new File(x);
      }
    }
    mMaxImageCount = m.opt(_12, 32);
    mInactivityTimeoutSeconds = m.opt(_13, 900);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof CompileImagesConfig))
      return false;
    CompileImagesConfig other = (CompileImagesConfig) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mOper.equals(other.mOper)))
      return false;
    if ((mNetwork == null) ^ (other.mNetwork == null))
      return false;
    if (mNetwork != null) {
      if (!(mNetwork.equals(other.mNetwork)))
        return false;
    }
    if (!(mNetworkPath.equals(other.mNetworkPath)))
      return false;
    if (!(mSourceDir.equals(other.mSourceDir)))
      return false;
    if (!(mAugmentationConfig.equals(other.mAugmentationConfig)))
      return false;
    if (!(mSeed == other.mSeed))
      return false;
    if (!(mTargetDirModel.equals(other.mTargetDirModel)))
      return false;
    if (!(mInspectionDir.equals(other.mInspectionDir)))
      return false;
    if (!(mTrainParam.equals(other.mTrainParam)))
      return false;
    if (!(mSnapshotDir.equals(other.mSnapshotDir)))
      return false;
    if (!(mProgressFile.equals(other.mProgressFile)))
      return false;
    if (!(mInferenceDir.equals(other.mInferenceDir)))
      return false;
    if (!(mMaxImageCount == other.mMaxImageCount))
      return false;
    if (!(mInactivityTimeoutSeconds == other.mInactivityTimeoutSeconds))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mOper.ordinal();
      if (mNetwork != null) {
        r = r * 37 + mNetwork.hashCode();
      }
      r = r * 37 + mNetworkPath.hashCode();
      r = r * 37 + mSourceDir.hashCode();
      r = r * 37 + mAugmentationConfig.hashCode();
      r = r * 37 + mSeed;
      r = r * 37 + mTargetDirModel.hashCode();
      r = r * 37 + mInspectionDir.hashCode();
      r = r * 37 + mTrainParam.hashCode();
      r = r * 37 + mSnapshotDir.hashCode();
      r = r * 37 + mProgressFile.hashCode();
      r = r * 37 + mInferenceDir.hashCode();
      r = r * 37 + mMaxImageCount;
      r = r * 37 + mInactivityTimeoutSeconds;
      m__hashcode = r;
    }
    return r;
  }

  protected CompileOper mOper;
  protected NeuralNetwork mNetwork;
  protected File mNetworkPath;
  protected File mSourceDir;
  protected AugmentationConfig mAugmentationConfig;
  protected int mSeed;
  protected File mTargetDirModel;
  protected File mInspectionDir;
  protected TrainParam mTrainParam;
  protected File mSnapshotDir;
  protected File mProgressFile;
  protected File mInferenceDir;
  protected int mMaxImageCount;
  protected int mInactivityTimeoutSeconds;
  protected int m__hashcode;

  public static final class Builder extends CompileImagesConfig {

    private Builder(CompileImagesConfig m) {
      mOper = m.mOper;
      mNetwork = m.mNetwork;
      mNetworkPath = m.mNetworkPath;
      mSourceDir = m.mSourceDir;
      mAugmentationConfig = m.mAugmentationConfig;
      mSeed = m.mSeed;
      mTargetDirModel = m.mTargetDirModel;
      mInspectionDir = m.mInspectionDir;
      mTrainParam = m.mTrainParam;
      mSnapshotDir = m.mSnapshotDir;
      mProgressFile = m.mProgressFile;
      mInferenceDir = m.mInferenceDir;
      mMaxImageCount = m.mMaxImageCount;
      mInactivityTimeoutSeconds = m.mInactivityTimeoutSeconds;
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
    public CompileImagesConfig build() {
      CompileImagesConfig r = new CompileImagesConfig();
      r.mOper = mOper;
      r.mNetwork = mNetwork;
      r.mNetworkPath = mNetworkPath;
      r.mSourceDir = mSourceDir;
      r.mAugmentationConfig = mAugmentationConfig;
      r.mSeed = mSeed;
      r.mTargetDirModel = mTargetDirModel;
      r.mInspectionDir = mInspectionDir;
      r.mTrainParam = mTrainParam;
      r.mSnapshotDir = mSnapshotDir;
      r.mProgressFile = mProgressFile;
      r.mInferenceDir = mInferenceDir;
      r.mMaxImageCount = mMaxImageCount;
      r.mInactivityTimeoutSeconds = mInactivityTimeoutSeconds;
      return r;
    }

    public Builder oper(CompileOper x) {
      mOper = (x == null) ? CompileOper.DEFAULT_INSTANCE : x;
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

    public Builder sourceDir(File x) {
      mSourceDir = (x == null) ? Files.DEFAULT : x;
      return this;
    }

    public Builder augmentationConfig(AugmentationConfig x) {
      mAugmentationConfig = (x == null) ? AugmentationConfig.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder seed(int x) {
      mSeed = x;
      return this;
    }

    public Builder targetDirModel(File x) {
      mTargetDirModel = (x == null) ? _D6 : x;
      return this;
    }

    public Builder inspectionDir(File x) {
      mInspectionDir = (x == null) ? Files.DEFAULT : x;
      return this;
    }

    public Builder trainParam(TrainParam x) {
      mTrainParam = (x == null) ? TrainParam.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder snapshotDir(File x) {
      mSnapshotDir = (x == null) ? Files.DEFAULT : x;
      return this;
    }

    public Builder progressFile(File x) {
      mProgressFile = (x == null) ? _D10 : x;
      return this;
    }

    public Builder inferenceDir(File x) {
      mInferenceDir = (x == null) ? _D11 : x;
      return this;
    }

    public Builder maxImageCount(int x) {
      mMaxImageCount = x;
      return this;
    }

    public Builder inactivityTimeoutSeconds(int x) {
      mInactivityTimeoutSeconds = x;
      return this;
    }

  }

  private static final File _D6 = new File("train_info");
  private static final File _D10 = new File("progress.txt");
  private static final File _D11 = new File("inference");

  public static final CompileImagesConfig DEFAULT_INSTANCE = new CompileImagesConfig();

  private CompileImagesConfig() {
    mOper = CompileOper.DEFAULT_INSTANCE;
    mNetworkPath = Files.DEFAULT;
    mSourceDir = Files.DEFAULT;
    mAugmentationConfig = AugmentationConfig.DEFAULT_INSTANCE;
    mTargetDirModel = _D6;
    mInspectionDir = Files.DEFAULT;
    mTrainParam = TrainParam.DEFAULT_INSTANCE;
    mSnapshotDir = Files.DEFAULT;
    mProgressFile = _D10;
    mInferenceDir = _D11;
    mMaxImageCount = 32;
    mInactivityTimeoutSeconds = 900;
  }

}
