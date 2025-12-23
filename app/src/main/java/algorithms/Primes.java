package algorithms;
import java.util.Vector;

public class Primes {
  /**
   * Checks if a number is prime
   * test comment
   * @param n The number to check.
   * @return True if the number is prime, false otherwise.
   */
  public static boolean IsPrime(int n) {
    if (n < 2) {
      return false;
    }
    for (int i = 2; i * i <= n; i++) { // Optimized loop condition
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }

  /**
   * Sums all prime numbers from 0 to n
   *
   * @param n The number of prime numbers to sum.
   * @return The sum of the first n prime numbers.
   */
  public static int SumPrimes(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
      if (IsPrime(i)) {
        sum = sum + i;
      }
    }
    return sum;
  }

  /**
   * Finds all primes factors of a number
   *
   * @param n The number to find the prime factors of.
   * @return An vector of all prime factors of n.
   */
  public static Vector<Integer> PrimeFactors(int n) {
    Vector<Integer> ret = new Vector<Integer>();

    for (int i = 2; i * i <= n; i++) { // Optimized loop condition
      while (n % i == 0) { // Optimized to handle repeated factors
        ret.add(i);
        n /= i; // Reduce n to avoid redundant checks.
      }
    }
    if (n > 1) { // Add any remaining prime factor.
        ret.add(n);
    }
    return ret;
  }

  /**
   * Generates a boolean array using the Sieve of Eratosthenes algorithm.
   * The array indicates which numbers from 0 to n are prime.
   * 
   * <p>Algorithm: Sieve of Eratosthenes
   * <ul>
   *   <li>Time complexity: O(n log log n)</li>
   *   <li>Space complexity: O(n)</li>
   * </ul>
   * 
   * <p>This is significantly faster than checking each number individually,
   * especially for large values of n. The algorithm works by iteratively marking
   * the multiples of each prime as composite, starting from 2.
   * 
   * @param n The upper limit (inclusive) for prime generation.
   * @return A boolean array where sieve[i] is true if i is prime, false otherwise.
   *         Returns array with all false for n < 2.
   */
  public static boolean[] generateSieve(int n) {
    if (n < 2) {
      // For n < 2, there are no primes
      boolean[] sieve = new boolean[n + 1];
      return sieve; // All false by default
    }

    boolean[] sieve = new boolean[n + 1];
    
    // Initialize all numbers as potentially prime
    for (int i = 2; i <= n; i++) {
      sieve[i] = true;
    }
    
    // Sieve of Eratosthenes algorithm
    for (int i = 2; i * i <= n; i++) {
      if (sieve[i]) {
        // Mark all multiples of i as composite
        // Start from i*i as smaller multiples already marked by smaller primes
        for (int j = i * i; j <= n; j += i) {
          sieve[j] = false;
        }
      }
    }
    
    return sieve;
  }

  /**
   * Returns all prime numbers up to and including n using the Sieve of Eratosthenes.
   * 
   * <p>Algorithm: Sieve of Eratosthenes
   * <ul>
   *   <li>Time complexity: O(n log log n)</li>
   *   <li>Space complexity: O(n)</li>
   * </ul>
   * 
   * <p>This method is significantly faster than repeatedly calling IsPrime() for each number,
   * making it ideal for generating all primes up to a limit. For n=1,000,000, this can be
   * orders of magnitude faster than the naive approach.
   * 
   * @param n The upper limit (inclusive) for prime generation.
   * @return A Vector containing all prime numbers from 2 to n in ascending order.
   *         Returns empty vector for n < 2.
   */
  public static Vector<Integer> getAllPrimesUpTo(int n) {
    Vector<Integer> primes = new Vector<Integer>();
    
    if (n < 2) {
      return primes; // No primes less than 2
    }
    
    boolean[] sieve = generateSieve(n);
    
    // Collect all prime numbers
    for (int i = 2; i <= n; i++) {
      if (sieve[i]) {
        primes.add(i);
      }
    }
    
    return primes;
  }

  /**
   * Sums all prime numbers from 0 to n using the Sieve of Eratosthenes algorithm.
   * 
   * <p>This is an optimized alternative to SumPrimes() that uses the Sieve of Eratosthenes
   * algorithm for significantly improved performance on large values of n.
   * 
   * <p>Algorithm: Sieve of Eratosthenes
   * <ul>
   *   <li>Time complexity: O(n log log n)</li>
   *   <li>Space complexity: O(n)</li>
   * </ul>
   * 
   * <p>Performance comparison:
   * <ul>
   *   <li>SumPrimes(): O(n√n) - checks primality of each number individually</li>
   *   <li>sumPrimesUsingSieve(): O(n log log n) - generates all primes at once</li>
   * </ul>
   * 
   * <p>For large n (e.g., n=1,000,000), this method can be orders of magnitude faster.
   * Both methods produce identical results.
   * 
   * @param n The upper limit (exclusive) for prime summation.
   * @return The sum of all prime numbers less than n.
   */
  public static long sumPrimesUsingSieve(int n) {
    if (n < 2) {
      return 0; // No primes less than 2
    }
    
    boolean[] sieve = generateSieve(n - 1);
    long sum = 0;
    
    // Sum all prime numbers
    for (int i = 2; i < n; i++) {
      if (sieve[i]) {
        sum += i;
      }
    }
    
    return sum;
  }
}
