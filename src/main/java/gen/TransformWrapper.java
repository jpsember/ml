package gen;

import js.data.AbstractData;
import js.geometry.Matrix;
import js.json.JSMap;

public class TransformWrapper implements AbstractData {

  public Matrix matrix() {
    return mMatrix;
  }

  public Matrix inverse() {
    return mInverse;
  }

  public int rotationDegrees() {
    return mRotationDegrees;
  }

  @Override
  public Builder toBuilder() {
    return new Builder(this);
  }

  protected static final String _0 = "matrix";
  protected static final String _1 = "inverse";
  protected static final String _2 = "rotation_degrees";

  @Override
  public String toString() {
    return toJson().prettyPrint();
  }

  @Override
  public JSMap toJson() {
    JSMap m = new JSMap();
    m.putUnsafe(_0, mMatrix.toJson());
    m.putUnsafe(_1, mInverse.toJson());
    m.putUnsafe(_2, mRotationDegrees);
    return m;
  }

  @Override
  public TransformWrapper build() {
    return this;
  }

  @Override
  public TransformWrapper parse(Object obj) {
    return new TransformWrapper((JSMap) obj);
  }

  private TransformWrapper(JSMap m) {
    {
      mMatrix = Matrix.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_0);
      if (x != null) {
        mMatrix = Matrix.DEFAULT_INSTANCE.parse(x);
      }
    }
    {
      mInverse = Matrix.DEFAULT_INSTANCE;
      Object x = m.optUnsafe(_1);
      if (x != null) {
        mInverse = Matrix.DEFAULT_INSTANCE.parse(x);
      }
    }
    mRotationDegrees = m.opt(_2, 0);
  }

  public static Builder newBuilder() {
    return new Builder(DEFAULT_INSTANCE);
  }

  @Override
  public boolean equals(Object object) {
    if (this == object)
      return true;
    if (object == null || !(object instanceof TransformWrapper))
      return false;
    TransformWrapper other = (TransformWrapper) object;
    if (other.hashCode() != hashCode())
      return false;
    if (!(mMatrix.equals(other.mMatrix)))
      return false;
    if (!(mInverse.equals(other.mInverse)))
      return false;
    if (!(mRotationDegrees == other.mRotationDegrees))
      return false;
    return true;
  }

  @Override
  public int hashCode() {
    int r = m__hashcode;
    if (r == 0) {
      r = 1;
      r = r * 37 + mMatrix.hashCode();
      r = r * 37 + mInverse.hashCode();
      r = r * 37 + mRotationDegrees;
      m__hashcode = r;
    }
    return r;
  }

  protected Matrix mMatrix;
  protected Matrix mInverse;
  protected int mRotationDegrees;
  protected int m__hashcode;

  public static final class Builder extends TransformWrapper {

    private Builder(TransformWrapper m) {
      mMatrix = m.mMatrix;
      mInverse = m.mInverse;
      mRotationDegrees = m.mRotationDegrees;
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
    public TransformWrapper build() {
      TransformWrapper r = new TransformWrapper();
      r.mMatrix = mMatrix;
      r.mInverse = mInverse;
      r.mRotationDegrees = mRotationDegrees;
      return r;
    }

    public Builder matrix(Matrix x) {
      mMatrix = (x == null) ? Matrix.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder inverse(Matrix x) {
      mInverse = (x == null) ? Matrix.DEFAULT_INSTANCE : x.build();
      return this;
    }

    public Builder rotationDegrees(int x) {
      mRotationDegrees = x;
      return this;
    }

  }

  public static final TransformWrapper DEFAULT_INSTANCE = new TransformWrapper();

  private TransformWrapper() {
    mMatrix = Matrix.DEFAULT_INSTANCE;
    mInverse = Matrix.DEFAULT_INSTANCE;
  }

}
