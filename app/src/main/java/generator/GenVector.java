package generator;
import java.util.ArrayList;

import java.util.concurrent.ThreadLocalRandom;

public final class GenVector {
  private GenVector() {
    throw new UnsupportedOperationException("Utility class");
  }

  /**
   * Generates a random list of integers, length n
   *
   * @param n The length of the list
   * @param m The maximum value of any element in the list (non-inclusive)
   * @return An ArrayList of length n
   */
  public static ArrayList<Integer> generateVector(int n, int m) {
    // Use ArrayList for better performance. Initialize with capacity to avoid resizing.
    ArrayList<Integer> ret = new ArrayList<>(n);

    for (int i = 0; i < n; i++) {
      ret.add(ThreadLocalRandom.current().nextInt(m));
    }

    return ret;
  }
}

