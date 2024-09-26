package gen;

import java.util.List;
import js.data.AbstractData;
import js.data.DataUtil;
import js.json.JSList;
import js.json.JSMap;

public class CmdItem implements AbstractData {

  public int id() {
    return mId;
  }

  public List<String> args() {
    return mArgs;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "id";
  protected static final String _1 = "args";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mId);
    {
      JSList j = new JSList();
      for (String x : mArgs)
        j.add(x);
      m.put(_1, j);
    }
    return m;
  }

  @Override
  public CmdItem build() {
    return this;
  }

  @Override
  public CmdItem parse(Object obj) {
    return new CmdItem((JSMap) obj);
  }

  private CmdItem(JSMap m) {
    mId = m.opt(_0, 0);
    mArgs = DataUtil.parseListOfObjects(m.optJSList(_1), false);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof CmdItem))
      return false;
    CmdItem other = (CmdItem) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mId == other.mId))
      return false;
    if (!(mArgs.equals(other.mArgs)))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mId;
      for (String x : mArgs)
        if (x != null)
          r = r * 37 + x.hashCode();
      m__hashcode = r;
    }
    return r;
  }

  protected int mId;
  protected List<String> mArgs;
  protected int m__hashcode;

  public static final class Builder extends CmdItem {

    private Builder(CmdItem m) {
      mId = m.mId;
      mArgs = DataUtil.mutableCopyOf(m.mArgs);
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
    public CmdItem build() {
      CmdItem r = new CmdItem();
      r.mId = mId;
      r.mArgs = DataUtil.immutableCopyOf(mArgs);
      return r;
    }

    public Builder id(int x) {
      mId = x;
      return this;
    }

    public Builder args(List<String> x) {
      mArgs = DataUtil.mutableCopyOf((x == null) ? DataUtil.emptyList() : x);
      return this;
    }

  }

  public static final CmdItem DEFAULT_INSTANCE = new CmdItem();

  private CmdItem() {
    mArgs = DataUtil.emptyList();
  }

}
