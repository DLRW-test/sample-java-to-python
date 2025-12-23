package control;

import java.util.HashMap;

public final class Double {
  private Double() {
    throw new UnsupportedOperationException("Utility class");
  }

  /**
   * Sums all values squared from 0 to n
   *
   * @param n The number of natural numbers to sum.
   * @return The sum of the first n natural numbers squared.
   */
  public static int sumSquare(int n) {
    // Formula for sum of squares: 0² + 1² + 2² + ... + (n-1)²
    // = (n-1) * n * (2*n-1) / 6
    return (n - 1) * n * (2 * n - 1) / 6;
  }

  /**
   * Sums all triangular numbers from T(1) to T(n)
   *
   * @param n The number of triangular numbers to sum.
   * @return The sum of the first n triangular numbers.
   */
  public static int sumTriangle(int n) {
    // Formula for sum of triangular numbers: T(0) + T(1) + ... + T(n)
    // = (n-1) * n * (n+1) / 6
    return (n - 1) * n * (n + 1) / 6;
  }

  /**
   * Counts the number of pairs in an array
   *
   * A pair is any value that is repeated exactly twice in the array.
   *
   * @param arr The array of integers.
   * @return The number of pairs in the array.
   */
  public static int countPairs(int[] arr) {
    // Optimized O(n) solution using HashMap to track frequencies
    HashMap<Integer, Integer> frequencyMap = new HashMap<>();
    
    // Single pass to count frequencies
    for (int i = 0; i < arr.length; i++) {
      frequencyMap.put(arr[i], frequencyMap.getOrDefault(arr[i], 0) + 1);
    }
    
    // Count elements that appear exactly twice
    int count = 0;
    for (int freq : frequencyMap.values()) {
      if (freq == 2) {
        count++;
      }
    }
    
    return count;
  }

  /**
   * Counts the number of instances where the values at the same index are equal
   *
   * @param arr0 The first array of integers.
   * @param arr1 The second array of integers.
   * @return The number of instances where the values at the same index are
   *         equal.
   */
  public static int countDuplicates(int[] arr0, int[] arr1) {
    // Optimized O(n) single-pass algorithm
    int count = 0;
    for (int i = 0; i < arr0.length; i++) {
      if (arr0[i] == arr1[i]) {
        count++;
      }
    }
    return count;
  }

  /**
   * Sums all values in a 2D array
   *
   * note: dimensions must be equal
   *
   * @param arr The 2D array of integers.
   * @return The sum of all values in the 2D array.
   */
  public static int sumMatrix(int[][] arr) {
    int sum = 0;
    int n = arr.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        sum += arr[i][j];
      }
    }
    return sum;
  }
}
