package gen;

import java.io.File;
import js.data.AbstractData;
import js.json.JSMap;

public class TrainParam implements AbstractData {

  @Deprecated
  public File targetDirTrain() {
    return mTargetDirTrain;
  }

  public File targetDirCheckpoint() {
    return mTargetDirCheckpoint;
  }

  public int maxTrainSets() {
    return mMaxTrainSets;
  }

  public int recycle() {
    return mRecycle;
  }

  public int maxCheckpoints() {
    return mMaxCheckpoints;
  }

  public int targetAccuracy() {
    return mTargetAccuracy;
  }

  public float targetLoss() {
    return mTargetLoss;
  }

  public int targetEpoch() {
    return mTargetEpoch;
  }

  public int batchSize() {
    return mBatchSize;
  }

  public boolean detectAnomalies() {
    return mDetectAnomalies;
  }

  public int maxLogCount() {
    return mMaxLogCount;
  }

  public boolean withGradientNorm() {
    return mWithGradientNorm;
  }

  public boolean disableBatchNorm() {
    return mDisableBatchNorm;
  }

  public boolean generateSnapshots() {
    return mGenerateSnapshots;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "target_dir_train";
  protected static final String _1 = "target_dir_checkpoint";
  protected static final String _2 = "max_train_sets";
  protected static final String _3 = "recycle";
  protected static final String _4 = "max_checkpoints";
  protected static final String _5 = "target_accuracy";
  protected static final String _6 = "target_loss";
  protected static final String _7 = "target_epoch";
  protected static final String _8 = "batch_size";
  protected static final String _9 = "detect_anomalies";
  protected static final String _10 = "max_log_count";
  protected static final String _11 = "with_gradient_norm";
  protected static final String _12 = "disable_batch_norm";
  protected static final String _13 = "generate_snapshots";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mTargetDirTrain.toString());
    m.putUnsafe(_1, mTargetDirCheckpoint.toString());
    m.putUnsafe(_2, mMaxTrainSets);
    m.putUnsafe(_3, mRecycle);
    m.putUnsafe(_4, mMaxCheckpoints);
    m.putUnsafe(_5, mTargetAccuracy);
    m.putUnsafe(_6, mTargetLoss);
    m.putUnsafe(_7, mTargetEpoch);
    m.putUnsafe(_8, mBatchSize);
    m.putUnsafe(_9, mDetectAnomalies);
    m.putUnsafe(_10, mMaxLogCount);
    m.putUnsafe(_11, mWithGradientNorm);
    m.putUnsafe(_12, mDisableBatchNorm);
    m.putUnsafe(_13, mGenerateSnapshots);
    return m;
  }

  @Override
  public TrainParam build() {
    return this;
  }

  @Override
  public TrainParam parse(Object obj) {
    return new TrainParam((JSMap) obj);
  }

  private TrainParam(JSMap m) {
    {
      mTargetDirTrain = _D0;
      String x = m.opt(_0, (String) null);
      if (x != null) {
        mTargetDirTrain = new File(x);
      }
    }
    {
      mTargetDirCheckpoint = _D1;
      String x = m.opt(_1, (String) null);
      if (x != null) {
        mTargetDirCheckpoint = new File(x);
      }
    }
    mMaxTrainSets = m.opt(_2, 3);
    mRecycle = m.opt(_3, 3);
    mMaxCheckpoints = m.opt(_4, 3);
    mTargetAccuracy = m.opt(_5, 95);
    mTargetLoss = m.opt(_6, 0f);
    mTargetEpoch = m.opt(_7, 0);
    mBatchSize = m.opt(_8, 32);
    mDetectAnomalies = m.opt(_9, false);
    mMaxLogCount = m.opt(_10, 20);
    mWithGradientNorm = m.opt(_11, false);
    mDisableBatchNorm = m.opt(_12, false);
    mGenerateSnapshots = m.opt(_13, false);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof TrainParam))
      return false;
    TrainParam other = (TrainParam) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mTargetDirTrain.equals(other.mTargetDirTrain)))
      return false;
    if (!(mTargetDirCheckpoint.equals(other.mTargetDirCheckpoint)))
      return false;
    if (!(mMaxTrainSets == other.mMaxTrainSets))
      return false;
    if (!(mRecycle == other.mRecycle))
      return false;
    if (!(mMaxCheckpoints == other.mMaxCheckpoints))
      return false;
    if (!(mTargetAccuracy == other.mTargetAccuracy))
      return false;
    if (!(mTargetLoss == other.mTargetLoss))
      return false;
    if (!(mTargetEpoch == other.mTargetEpoch))
      return false;
    if (!(mBatchSize == other.mBatchSize))
      return false;
    if (!(mDetectAnomalies == other.mDetectAnomalies))
      return false;
    if (!(mMaxLogCount == other.mMaxLogCount))
      return false;
    if (!(mWithGradientNorm == other.mWithGradientNorm))
      return false;
    if (!(mDisableBatchNorm == other.mDisableBatchNorm))
      return false;
    if (!(mGenerateSnapshots == other.mGenerateSnapshots))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mTargetDirTrain.hashCode();
      r = r * 37 + mTargetDirCheckpoint.hashCode();
      r = r * 37 + mMaxTrainSets;
      r = r * 37 + mRecycle;
      r = r * 37 + mMaxCheckpoints;
      r = r * 37 + mTargetAccuracy;
      r = r * 37 + (int)mTargetLoss;
      r = r * 37 + mTargetEpoch;
      r = r * 37 + mBatchSize;
      r = r * 37 + (mDetectAnomalies ? 1 : 0);
      r = r * 37 + mMaxLogCount;
      r = r * 37 + (mWithGradientNorm ? 1 : 0);
      r = r * 37 + (mDisableBatchNorm ? 1 : 0);
      r = r * 37 + (mGenerateSnapshots ? 1 : 0);
      m__hashcode = r;
    }
    return r;
  }

  protected File mTargetDirTrain;
  protected File mTargetDirCheckpoint;
  protected int mMaxTrainSets;
  protected int mRecycle;
  protected int mMaxCheckpoints;
  protected int mTargetAccuracy;
  protected float mTargetLoss;
  protected int mTargetEpoch;
  protected int mBatchSize;
  protected boolean mDetectAnomalies;
  protected int mMaxLogCount;
  protected boolean mWithGradientNorm;
  protected boolean mDisableBatchNorm;
  protected boolean mGenerateSnapshots;
  protected int m__hashcode;

  public static final class Builder extends TrainParam {

    private Builder(TrainParam m) {
      mTargetDirTrain = m.mTargetDirTrain;
      mTargetDirCheckpoint = m.mTargetDirCheckpoint;
      mMaxTrainSets = m.mMaxTrainSets;
      mRecycle = m.mRecycle;
      mMaxCheckpoints = m.mMaxCheckpoints;
      mTargetAccuracy = m.mTargetAccuracy;
      mTargetLoss = m.mTargetLoss;
      mTargetEpoch = m.mTargetEpoch;
      mBatchSize = m.mBatchSize;
      mDetectAnomalies = m.mDetectAnomalies;
      mMaxLogCount = m.mMaxLogCount;
      mWithGradientNorm = m.mWithGradientNorm;
      mDisableBatchNorm = m.mDisableBatchNorm;
      mGenerateSnapshots = m.mGenerateSnapshots;
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
    public TrainParam build() {
      TrainParam r = new TrainParam();
      r.mTargetDirTrain = mTargetDirTrain;
      r.mTargetDirCheckpoint = mTargetDirCheckpoint;
      r.mMaxTrainSets = mMaxTrainSets;
      r.mRecycle = mRecycle;
      r.mMaxCheckpoints = mMaxCheckpoints;
      r.mTargetAccuracy = mTargetAccuracy;
      r.mTargetLoss = mTargetLoss;
      r.mTargetEpoch = mTargetEpoch;
      r.mBatchSize = mBatchSize;
      r.mDetectAnomalies = mDetectAnomalies;
      r.mMaxLogCount = mMaxLogCount;
      r.mWithGradientNorm = mWithGradientNorm;
      r.mDisableBatchNorm = mDisableBatchNorm;
      r.mGenerateSnapshots = mGenerateSnapshots;
      return r;
    }

    @Deprecated
    public Builder targetDirTrain(File x) {
      mTargetDirTrain = (x == null) ? _D0 : x;
      return this;
    }

    public Builder targetDirCheckpoint(File x) {
      mTargetDirCheckpoint = (x == null) ? _D1 : x;
      return this;
    }

    public Builder maxTrainSets(int x) {
      mMaxTrainSets = x;
      return this;
    }

    public Builder recycle(int x) {
      mRecycle = x;
      return this;
    }

    public Builder maxCheckpoints(int x) {
      mMaxCheckpoints = x;
      return this;
    }

    public Builder targetAccuracy(int x) {
      mTargetAccuracy = x;
      return this;
    }

    public Builder targetLoss(float x) {
      mTargetLoss = x;
      return this;
    }

    public Builder targetEpoch(int x) {
      mTargetEpoch = x;
      return this;
    }

    public Builder batchSize(int x) {
      mBatchSize = x;
      return this;
    }

    public Builder detectAnomalies(boolean x) {
      mDetectAnomalies = x;
      return this;
    }

    public Builder maxLogCount(int x) {
      mMaxLogCount = x;
      return this;
    }

    public Builder withGradientNorm(boolean x) {
      mWithGradientNorm = x;
      return this;
    }

    public Builder disableBatchNorm(boolean x) {
      mDisableBatchNorm = x;
      return this;
    }

    public Builder generateSnapshots(boolean x) {
      mGenerateSnapshots = x;
      return this;
    }

  }

  private static final File _D0 = new File("train_data");
  private static final File _D1 = new File("checkpoints");

  public static final TrainParam DEFAULT_INSTANCE = new TrainParam();

  private TrainParam() {
    mTargetDirTrain = _D0;
    mTargetDirCheckpoint = _D1;
    mMaxTrainSets = 3;
    mRecycle = 3;
    mMaxCheckpoints = 3;
    mTargetAccuracy = 95;
    mBatchSize = 32;
    mMaxLogCount = 20;
  }

}
