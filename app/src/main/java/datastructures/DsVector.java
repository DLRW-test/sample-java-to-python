package datastructures;

import java.util.ArrayList;
import java.util.Collections;

public final class DsVector {
  private DsVector() {
    throw new UnsupportedOperationException("Utility class");
  }

  /**
   * Adds 1 to each element of the ArrayList
   *
   * @param v the ArrayList to be incremented
   * @return the incremented ArrayList
   */
  public static ArrayList<Integer> modifyVector(ArrayList<Integer> v) {
    for (int i = 0; i < v.size(); i++) {
      v.set(i, v.get(i) + 1);
    }
    return v;
  }

  /**
   * Searches the ArrayList for all instances of n
   *
   * @param v the ArrayList to be searched
   * @return An ArrayList of all indices where n was found
   */
  public static ArrayList<Integer> searchVector(ArrayList<Integer> v, int n) {
    ArrayList<Integer> indices = new ArrayList<Integer>();
    for (int i = 0; i < v.size(); i++) {
      if (v.get(i) == n) {
        indices.add(i);
      }
    }
    return indices;
  }

  /**
   * Sorts the ArrayList in ascending order
   *
   * @param v the ArrayList to be sorted
   * @return the sorted ArrayList
   */
  public static ArrayList<Integer> sortVector(ArrayList<Integer> v) {
    ArrayList<Integer> ret = new ArrayList<Integer>(v);
    Collections.sort(ret);
    return ret;
  }

  /**
   * Reverses the ArrayList
   *
   * @param v the ArrayList to be reversed
   * @return the reversed ArrayList
   */
  public static ArrayList<Integer> reverseVector(ArrayList<Integer> v) {
    ArrayList<Integer> ret = new ArrayList<Integer>();

    for (int i = v.size() - 1; i >= 0; i--) {
      ret.add(v.get(i));
    }
    return ret;
  }

  /**
   * Rotates the ArrayList by n
   *
   * @param v the ArrayList to be rotated
   * @param n the number of times to rotate the ArrayList
   * @return the rotated ArrayList
   */
  public static ArrayList<Integer> rotateVector(ArrayList<Integer> v, int n) {
    ArrayList<Integer> ret = new ArrayList<Integer>();

    for (int i = n; i < v.size(); i++) {
      ret.add(v.get(i));
    }
    for (int i = 0; i < n; i++) {
      ret.add(v.get(i));
    }
    return ret;
  }

  /**
   * Merges two ArrayLists
   *
   * @param v1 the first ArrayList to be merged
   * @param v2 the second ArrayList to be merged
   * @return the merged ArrayList
   */
  public static ArrayList<Integer> mergeVectors(ArrayList<Integer> v1,
      ArrayList<Integer> v2) {
    ArrayList<Integer> ret = new ArrayList<Integer>();

    for (int i = 0; i < v1.size(); i++) {
      ret.add(v1.get(i));
    }
    for (int i = 0; i < v2.size(); i++) {
      ret.add(v2.get(i));
    }
    return ret;
  }
}
