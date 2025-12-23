package control;

public final class Single {
  private Single() {
    throw new UnsupportedOperationException("Utility class");
  }

  /**
   * This method is used to calculate the sum of the first n natural numbers.
   * n exclusive
   *
   * @param n The number of natural numbers to sum.
   * @return The sum of the first n natural numbers.
   * @throws IllegalArgumentException if n is negative
   */
  public static int sumRange(int n) {
    if (n < 0) {
      throw new IllegalArgumentException("n must be non-negative, got: " + n);
    }
    return n * (n - 1) / 2;
  }

  /**
   * This method calculates the maximum value in an array of integers.
   *
   * @param arr The array of integers.
   * @return The maximum value in the array.
   * @throws NullPointerException if arr is null
   * @throws IllegalArgumentException if arr is empty
   */
  public static int maxArray(int[] arr) {
    if (arr == null) {
      throw new NullPointerException("Array cannot be null");
    }
    if (arr.length == 0) {
      throw new IllegalArgumentException("Array cannot be empty");
    }
    int max = arr[0];
    for (int i : arr) {
      if (i > max) {
        max = i;
      }
    }
    return max;
  }

  /**
   * This method calculates the sum of the first n natural numbers, modulo m.
   *
   * @param n The number of natural numbers to sum.
   * @param m The modulus.
   * @return The sum of the first n natural numbers, modulo m.
   * @throws IllegalArgumentException if m is zero or negative
   */
  public static int sumModulus(int n, int m) {
    if (m <= 0) {
      throw new IllegalArgumentException("Modulus must be positive, got: " + m);
    }
    int k = (n - 1) / m;
    return m * k * (k + 1) / 2;
  }
}
