package algorithms;

import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;

public final class Sort {
  private Sort() {
    throw new UnsupportedOperationException("Utility class");
  }

  /**
   * Sorts a vector of integers in ascending order
   *
   * @param v The vector to be sorted
   */
  public static void sortVector(ArrayList<Integer> v) {
    Collections.sort(v);
  }

  /**
   * Partitions a vector of integers around a pivot
   *
   * @param v           The vector to be partitioned
   * @param pivot_value
   */
  public static void dutchFlagPartition(ArrayList<Integer> v, int pivot_value) {
    int next_value = 0;

    for (int i = 0; i < v.size(); i++) {
      if (v.get(i) < pivot_value) {
        Collections.swap(v, i, next_value);
        next_value++;
      }
    }

    for (int i = next_value; i < v.size(); i++) {
      if (v.get(i) == pivot_value) {
        Collections.swap(v, i, next_value);
        next_value++;
      }
    }
  }

  /**
   * Returns the largest n elements in a vector
   *
   * @param v The vector to be sorted
   * @param n The number of elements to return
   * @return A vector of the largest n elements in v
   */
  public static ArrayList<Integer> maxN(ArrayList<Integer> v, int n) {
    if (n <= 0 || n > v.size()) {
      return new ArrayList<>();
    }

    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    for (int i = 0; i < n; ++i) {
      minHeap.offer(v.get(i));
    }

    for (int i = n; i < v.size(); ++i) {
      if (v.get(i) > minHeap.peek()) {
        minHeap.poll();
        minHeap.offer(v.get(i));
      }
    }

    ArrayList<Integer> ret = new ArrayList<>(minHeap);
    Collections.sort(ret, Collections.reverseOrder()); // Sort in descending order
    return ret;
  }
}

