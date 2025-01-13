package algorithms;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Vector;

public class Sort {
  /**
   * Sorts a vector of integers in ascending order
   *
   * @param v The vector to be sorted
   */
  public static void SortVector(Vector<Integer> v) {
    Collections.sort(v);
  }

  /**
   * Partitions a vector of integers around a pivot
   *
   * @param v           The vector to be partitioned
   * @param pivot_value
   */
  public static void DutchFlagPartition(Vector<Integer> v, int pivot_value) {
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
  public static Vector<Integer> MaxN(Vector<Integer> v, int n) {
    if (n <= 0 || n > v.size()) {
      return new Vector<Integer>();
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

    Vector<Integer> ret = new Vector<>(minHeap);
    Collections.sort(ret, Collections.reverseOrder()); // Sort in descending order
    return ret;
  }
}