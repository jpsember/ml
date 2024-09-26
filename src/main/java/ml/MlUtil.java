package ml;

import static js.base.Tools.*;

import java.io.File;
import java.util.Random;

public final class MlUtil {

  /**
   * Construct a Random instance
   * 
   * @param seed
   *          if zero, derives from current epoch time
   */
  public static Random buildRandom(int seed) {
    if (seed == 0)
      seed = (int) System.currentTimeMillis();
    return new Random(seed);
  }

  // ------------------------------------------------------------------
  // Training directory (a ram disk, presumably)
  // ------------------------------------------------------------------

  public static File trainDir() {
    if (sTrainDir == null) {
      sTrainDir = new File("/Volumes/ml_disk");
      if (!sTrainDir.isDirectory())
        badState("Cannot find train directory:", sTrainDir, "; run create_ramdisk.sh script first?");
    }
    return sTrainDir;
  }

  private static File sTrainDir;

}
