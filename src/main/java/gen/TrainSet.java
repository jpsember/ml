package gen;

import java.io.File;
import js.data.AbstractData;
import js.file.Files;
import js.json.JSMap;

public class TrainSet implements AbstractData {

  public int used() {
    return mUsed;
  }

  public File directory() {
    return mDirectory;
  }

  public int id() {
    return mId;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "used";
  protected static final String _1 = "directory";
  protected static final String _2 = "id";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mUsed);
    m.putUnsafe(_1, mDirectory.toString());
    m.putUnsafe(_2, mId);
    return m;
  }

  @Override
  public TrainSet build() {
    return this;
  }

  @Override
  public TrainSet parse(Object obj) {
    return new TrainSet((JSMap) obj);
  }

  private TrainSet(JSMap m) {
    mUsed = m.opt(_0, 0);
    {
      mDirectory = Files.DEFAULT;
      String x = m.opt(_1, (String) null);
      if (x != null) {
        mDirectory = new File(x);
      }
    }
    mId = m.opt(_2, 0);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof TrainSet))
      return false;
    TrainSet other = (TrainSet) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mUsed == other.mUsed))
      return false;
    if (!(mDirectory.equals(other.mDirectory)))
      return false;
    if (!(mId == other.mId))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mUsed;
      r = r * 37 + mDirectory.hashCode();
      r = r * 37 + mId;
      m__hashcode = r;
    }
    return r;
  }

  protected int mUsed;
  protected File mDirectory;
  protected int mId;
  protected int m__hashcode;

  public static final class Builder extends TrainSet {

    private Builder(TrainSet m) {
      mUsed = m.mUsed;
      mDirectory = m.mDirectory;
      mId = m.mId;
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
    public TrainSet build() {
      TrainSet r = new TrainSet();
      r.mUsed = mUsed;
      r.mDirectory = mDirectory;
      r.mId = mId;
      return r;
    }

    public Builder used(int x) {
      mUsed = x;
      return this;
    }

    public Builder directory(File x) {
      mDirectory = (x == null) ? Files.DEFAULT : x;
      return this;
    }

    public Builder id(int x) {
      mId = x;
      return this;
    }

  }

  public static final TrainSet DEFAULT_INSTANCE = new TrainSet();

  private TrainSet() {
    mDirectory = Files.DEFAULT;
  }

}
