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
   */
  public static LinkedList<Integer> shuffle(LinkedList<Integer> l) {
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
   */
  public static LinkedList<Integer> slice(LinkedList<Integer> l, int start,
      int end) {
    return new LinkedList<>(l.subList(start, end));
  }
}

