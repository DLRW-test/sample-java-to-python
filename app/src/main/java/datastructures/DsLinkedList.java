package datastructures;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;

public final class DsLinkedList {
  private DsLinkedList() {
    throw new UnsupportedOperationException("Utility class");
  }

  /**
   * Shuffles a linked list into a new list
   *
   * @param l the linked list to be shuffled
   * @return the shuffled linked list
   * @throws NullPointerException if l is null
   */
  public static LinkedList<Integer> shuffle(LinkedList<Integer> l) {
    if (l == null) {
      throw new NullPointerException("LinkedList cannot be null");
    }
    ArrayList<Integer> tmp = new ArrayList<>(l);
    Collections.shuffle(tmp);
    return new LinkedList<>(tmp);
  }

  /**
   * Returns a slice of a linked list
   *
   * @param l     the linked list to be sliced
   * @param start the starting index of the slice
   * @param end   the ending index of the slice (exclusive)
   * @return the sliced linked list
   * @throws NullPointerException if l is null
   * @throws IndexOutOfBoundsException if start or end are out of bounds
   */
  public static LinkedList<Integer> slice(LinkedList<Integer> l, int start,
      int end) {
    if (l == null) {
      throw new NullPointerException("LinkedList cannot be null");
    }
    if (start < 0 || start > l.size()) {
      throw new IndexOutOfBoundsException(
          "Start index out of bounds: " + start + " for size: " + l.size());
    }
    if (end < 0 || end > l.size()) {
      throw new IndexOutOfBoundsException(
          "End index out of bounds: " + end + " for size: " + l.size());
    }
    if (start > end) {
      throw new IndexOutOfBoundsException(
          "Start index (" + start + ") cannot be greater than end index (" + end + ")");
    }
    return new LinkedList<>(l.subList(start, end));
  }
}

