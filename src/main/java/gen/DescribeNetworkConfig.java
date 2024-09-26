package gen;

import java.io.File;
import js.data.AbstractData;
import js.json.JSMap;

public class DescribeNetworkConfig implements AbstractData {

  public File path() {
    return mPath;
  }

  public int maxSizeMb() {
    return mMaxSizeMb;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "path";
  protected static final String _1 = "max_size_mb";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mPath.toString());
    m.putUnsafe(_1, mMaxSizeMb);
    return m;
  }

  @Override
  public DescribeNetworkConfig build() {
    return this;
  }

  @Override
  public DescribeNetworkConfig parse(Object obj) {
    return new DescribeNetworkConfig((JSMap) obj);
  }

  private DescribeNetworkConfig(JSMap m) {
    {
      mPath = _D0;
      String x = m.opt(_0, (String) null);
      if (x != null) {
        mPath = new File(x);
      }
    }
    mMaxSizeMb = m.opt(_1, 300);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof DescribeNetworkConfig))
      return false;
    DescribeNetworkConfig other = (DescribeNetworkConfig) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mPath.equals(other.mPath)))
      return false;
    if (!(mMaxSizeMb == other.mMaxSizeMb))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mPath.hashCode();
      r = r * 37 + mMaxSizeMb;
      m__hashcode = r;
    }
    return r;
  }

  protected File mPath;
  protected int mMaxSizeMb;
  protected int m__hashcode;

  public static final class Builder extends DescribeNetworkConfig {

    private Builder(DescribeNetworkConfig m) {
      mPath = m.mPath;
      mMaxSizeMb = m.mMaxSizeMb;
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
    public DescribeNetworkConfig build() {
      DescribeNetworkConfig r = new DescribeNetworkConfig();
      r.mPath = mPath;
      r.mMaxSizeMb = mMaxSizeMb;
      return r;
    }

    public Builder path(File x) {
      mPath = (x == null) ? _D0 : x;
      return this;
    }

    public Builder maxSizeMb(int x) {
      mMaxSizeMb = x;
      return this;
    }

  }

  private static final File _D0 = new File("network.json");

  public static final DescribeNetworkConfig DEFAULT_INSTANCE = new DescribeNetworkConfig();

  private DescribeNetworkConfig() {
    mPath = _D0;
    mMaxSizeMb = 300;
  }

}
