package algorithms;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Vector;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;

public class PrimesTest {

  @Nested
  @DisplayName("IsPrime(int n) tests")
  class IsPrimeTests {

    @Test
    @DisplayName("Edge case: negative numbers should return false")
    public void testIsPrimeNegative() {
      assertFalse(Primes.IsPrime(-1), "IsPrime(-1) should return false");
      assertFalse(Primes.IsPrime(-5), "IsPrime(-5) should return false");
      assertFalse(Primes.IsPrime(-100), "IsPrime(-100) should return false");
    }

    @Test
    @DisplayName("Edge case: n=0 should return false")
    public void testIsPrimeZero() {
      assertFalse(Primes.IsPrime(0), "IsPrime(0) should return false");
    }

    @Test
    @DisplayName("Edge case: n=1 should return false")
    public void testIsPrimeOne() {
      assertFalse(Primes.IsPrime(1), "IsPrime(1) should return false");
    }

    @Test
    @DisplayName("n=2 (smallest prime) should return true")
    public void testIsPrimeTwo() {
      assertTrue(Primes.IsPrime(2), "IsPrime(2) should return true");
    }

    @Test
    @DisplayName("Small primes: 3, 5, 7 should return true")
    public void testIsPrimeSmallPrimes() {
      assertTrue(Primes.IsPrime(3), "IsPrime(3) should return true");
      assertTrue(Primes.IsPrime(5), "IsPrime(5) should return true");
      assertTrue(Primes.IsPrime(7), "IsPrime(7) should return true");
    }

    @Test
    @DisplayName("Small composites: 4, 6, 8, 9 should return false")
    public void testIsPrimeSmallComposites() {
      assertFalse(Primes.IsPrime(4), "IsPrime(4) should return false");
      assertFalse(Primes.IsPrime(6), "IsPrime(6) should return false");
      assertFalse(Primes.IsPrime(8), "IsPrime(8) should return false");
      assertFalse(Primes.IsPrime(9), "IsPrime(9) should return false");
    }

    @Test
    @DisplayName("Larger primes: 13, 17, 19 should return true")
    public void testIsPrimeLargerPrimes() {
      assertTrue(Primes.IsPrime(13), "IsPrime(13) should return true");
      assertTrue(Primes.IsPrime(17), "IsPrime(17) should return true");
      assertTrue(Primes.IsPrime(19), "IsPrime(19) should return true");
    }

    @Test
    @DisplayName("Larger composites: 15, 20, 100 should return false")
    public void testIsPrimeLargerComposites() {
      assertFalse(Primes.IsPrime(15), "IsPrime(15) should return false");
      assertFalse(Primes.IsPrime(20), "IsPrime(20) should return false");
      assertFalse(Primes.IsPrime(100), "IsPrime(100) should return false");
    }
  }

  @Nested
  @DisplayName("SumPrimes(int n) tests")
  class SumPrimesTests {

    @Test
    @DisplayName("Edge case: n=0 should return 0")
    public void testSumPrimesZero() {
      assertEquals(0, Primes.SumPrimes(0), "SumPrimes(0) should return 0");
    }

    @Test
    @DisplayName("Edge case: n=1 should return 0 (no primes less than 1)")
    public void testSumPrimesOne() {
      assertEquals(0, Primes.SumPrimes(1), "SumPrimes(1) should return 0");
    }

    @Test
    @DisplayName("Edge case: n=2 should return 0 (no primes less than 2)")
    public void testSumPrimesTwo() {
      assertEquals(0, Primes.SumPrimes(2), "SumPrimes(2) should return 0");
    }

    @Test
    @DisplayName("n=5 should return 5 (primes < 5: 2, 3)")
    public void testSumPrimesFive() {
      // Primes less than 5 are: 2, 3
      // Sum = 2 + 3 = 5
      assertEquals(5, Primes.SumPrimes(5), "SumPrimes(5) should return 5");
    }

    @Test
    @DisplayName("n=6 should return 5 (primes < 6: 2, 3, 5)")
    public void testSumPrimesSix() {
      // Primes less than 6 are: 2, 3, 5
      // Sum = 2 + 3 + 5 = 10
      assertEquals(10, Primes.SumPrimes(6), "SumPrimes(6) should return 10");
    }

    @Test
    @DisplayName("n=10 should return 17 (primes < 10: 2, 3, 5, 7)")
    public void testSumPrimesTen() {
      // Primes less than 10 are: 2, 3, 5, 7
      // Sum = 2 + 3 + 5 + 7 = 17
      assertEquals(17, Primes.SumPrimes(10), "SumPrimes(10) should return 17");
    }

    @Test
    @DisplayName("n=11 should return 17 (primes < 11: 2, 3, 5, 7)")
    public void testSumPrimesEleven() {
      // Primes less than 11 are: 2, 3, 5, 7
      // Sum = 2 + 3 + 5 + 7 = 17
      assertEquals(17, Primes.SumPrimes(11), "SumPrimes(11) should return 17");
    }

    @Test
    @DisplayName("n=12 should return 28 (primes < 12: 2, 3, 5, 7, 11)")
    public void testSumPrimesTwelve() {
      // Primes less than 12 are: 2, 3, 5, 7, 11
      // Sum = 2 + 3 + 5 + 7 + 11 = 28
      assertEquals(28, Primes.SumPrimes(12), "SumPrimes(12) should return 28");
    }
  }

  @Nested
  @DisplayName("PrimeFactors(int n) tests")
  class PrimeFactorsTests {

    @Test
    @DisplayName("Edge case: n=1 should return empty vector")
    public void testPrimeFactorsOne() {
      Vector<Integer> result = Primes.PrimeFactors(1);
      assertEquals(0, result.size(), "PrimeFactors(1) should return empty vector");
    }

    @Test
    @DisplayName("Edge case: n=2 should return [2]")
    public void testPrimeFactorsTwo() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(2));
      assertEquals(expected, Primes.PrimeFactors(2), "PrimeFactors(2) should return [2]");
    }

    @Test
    @DisplayName("Prime input: n=7 should return [7]")
    public void testPrimeFactorsSeven() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(7));
      assertEquals(expected, Primes.PrimeFactors(7), "PrimeFactors(7) should return [7]");
    }

    @Test
    @DisplayName("Prime input: n=11 should return [11]")
    public void testPrimeFactorsEleven() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(11));
      assertEquals(expected, Primes.PrimeFactors(11), "PrimeFactors(11) should return [11]");
    }

    @Test
    @DisplayName("Prime input: n=13 should return [13]")
    public void testPrimeFactorsThirteen() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(13));
      assertEquals(expected, Primes.PrimeFactors(13), "PrimeFactors(13) should return [13]");
    }

    @Test
    @DisplayName("Composite input: n=12 should return [2, 2, 3]")
    public void testPrimeFactorsTwelve() {
      // 12 = 2 * 2 * 3
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 2, 3));
      assertEquals(expected, Primes.PrimeFactors(12), "PrimeFactors(12) should return [2, 2, 3]");
    }

    @Test
    @DisplayName("Composite input: n=18 should return [2, 3, 3]")
    public void testPrimeFactorsEighteen() {
      // 18 = 2 * 3 * 3
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 3, 3));
      assertEquals(expected, Primes.PrimeFactors(18), "PrimeFactors(18) should return [2, 3, 3]");
    }

    @Test
    @DisplayName("Composite input: n=24 should return [2, 2, 2, 3]")
    public void testPrimeFactorsTwentyFour() {
      // 24 = 2 * 2 * 2 * 3
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 2, 2, 3));
      assertEquals(expected, Primes.PrimeFactors(24), "PrimeFactors(24) should return [2, 2, 2, 3]");
    }

    @Test
    @DisplayName("Perfect square: n=4 should return [2, 2]")
    public void testPrimeFactorsFour() {
      // 4 = 2 * 2
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 2));
      assertEquals(expected, Primes.PrimeFactors(4), "PrimeFactors(4) should return [2, 2]");
    }

    @Test
    @DisplayName("Perfect square: n=9 should return [3, 3]")
    public void testPrimeFactorsNine() {
      // 9 = 3 * 3
      Vector<Integer> expected = new Vector<>(Arrays.asList(3, 3));
      assertEquals(expected, Primes.PrimeFactors(9), "PrimeFactors(9) should return [3, 3]");
    }

    @Test
    @DisplayName("Perfect square: n=16 should return [2, 2, 2, 2]")
    public void testPrimeFactorsSixteen() {
      // 16 = 2 * 2 * 2 * 2
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 2, 2, 2));
      assertEquals(expected, Primes.PrimeFactors(16), "PrimeFactors(16) should return [2, 2, 2, 2]");
    }

    @Test
    @DisplayName("Composite with larger factors: n=30 should return [2, 3, 5]")
    public void testPrimeFactorsThirty() {
      // 30 = 2 * 3 * 5
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 3, 5));
      assertEquals(expected, Primes.PrimeFactors(30), "PrimeFactors(30) should return [2, 3, 5]");
    }
  }

  @Nested
  @DisplayName("generateSieve(int n) tests")
  class GenerateSieveTests {

    @Test
    @DisplayName("Edge case: n=0 should return array with no primes")
    public void testGenerateSieveZero() {
      boolean[] sieve = Primes.generateSieve(0);
      assertEquals(1, sieve.length, "generateSieve(0) should return array of length 1");
      assertFalse(sieve[0], "sieve[0] should be false (0 is not prime)");
    }

    @Test
    @DisplayName("Edge case: n=1 should return array with no primes")
    public void testGenerateSieveOne() {
      boolean[] sieve = Primes.generateSieve(1);
      assertEquals(2, sieve.length, "generateSieve(1) should return array of length 2");
      assertFalse(sieve[0], "sieve[0] should be false (0 is not prime)");
      assertFalse(sieve[1], "sieve[1] should be false (1 is not prime)");
    }

    @Test
    @DisplayName("Edge case: n=2 should mark 2 as prime")
    public void testGenerateSieveTwo() {
      boolean[] sieve = Primes.generateSieve(2);
      assertEquals(3, sieve.length, "generateSieve(2) should return array of length 3");
      assertFalse(sieve[0], "sieve[0] should be false (0 is not prime)");
      assertFalse(sieve[1], "sieve[1] should be false (1 is not prime)");
      assertTrue(sieve[2], "sieve[2] should be true (2 is prime)");
    }

    @Test
    @DisplayName("n=10 should correctly identify primes: 2, 3, 5, 7")
    public void testGenerateSieveTen() {
      boolean[] sieve = Primes.generateSieve(10);
      // Primes up to 10: 2, 3, 5, 7
      assertTrue(sieve[2], "2 should be prime");
      assertTrue(sieve[3], "3 should be prime");
      assertFalse(sieve[4], "4 should not be prime");
      assertTrue(sieve[5], "5 should be prime");
      assertFalse(sieve[6], "6 should not be prime");
      assertTrue(sieve[7], "7 should be prime");
      assertFalse(sieve[8], "8 should not be prime");
      assertFalse(sieve[9], "9 should not be prime");
      assertFalse(sieve[10], "10 should not be prime");
    }

    @Test
    @DisplayName("n=30 should correctly identify all primes up to 30")
    public void testGenerateSieveThirty() {
      boolean[] sieve = Primes.generateSieve(30);
      // Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
      int[] expectedPrimes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
      
      for (int prime : expectedPrimes) {
        assertTrue(sieve[prime], prime + " should be prime");
      }
      
      // Check some composites
      assertFalse(sieve[4], "4 should not be prime");
      assertFalse(sieve[15], "15 should not be prime");
      assertFalse(sieve[25], "25 should not be prime");
      assertFalse(sieve[30], "30 should not be prime");
    }

    @Test
    @DisplayName("n=100 should count 25 primes")
    public void testGenerateSieveHundred() {
      boolean[] sieve = Primes.generateSieve(100);
      int primeCount = 0;
      for (int i = 0; i <= 100; i++) {
        if (sieve[i]) {
          primeCount++;
        }
      }
      assertEquals(25, primeCount, "There should be 25 primes up to 100");
    }
  }

  @Nested
  @DisplayName("getAllPrimesUpTo(int n) tests")
  class GetAllPrimesUpToTests {

    @Test
    @DisplayName("Edge case: n=0 should return empty vector")
    public void testGetAllPrimesUpToZero() {
      Vector<Integer> primes = Primes.getAllPrimesUpTo(0);
      assertEquals(0, primes.size(), "getAllPrimesUpTo(0) should return empty vector");
    }

    @Test
    @DisplayName("Edge case: n=1 should return empty vector")
    public void testGetAllPrimesUpToOne() {
      Vector<Integer> primes = Primes.getAllPrimesUpTo(1);
      assertEquals(0, primes.size(), "getAllPrimesUpTo(1) should return empty vector");
    }

    @Test
    @DisplayName("Edge case: n=2 should return [2]")
    public void testGetAllPrimesUpToTwo() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(2));
      assertEquals(expected, Primes.getAllPrimesUpTo(2), "getAllPrimesUpTo(2) should return [2]");
    }

    @Test
    @DisplayName("n=10 should return [2, 3, 5, 7]")
    public void testGetAllPrimesUpToTen() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 3, 5, 7));
      assertEquals(expected, Primes.getAllPrimesUpTo(10), "getAllPrimesUpTo(10) should return [2, 3, 5, 7]");
    }

    @Test
    @DisplayName("n=20 should return correct primes")
    public void testGetAllPrimesUpToTwenty() {
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19));
      assertEquals(expected, Primes.getAllPrimesUpTo(20), "getAllPrimesUpTo(20) should return all primes up to 20");
    }

    @Test
    @DisplayName("n=30 should return 10 primes")
    public void testGetAllPrimesUpToThirty() {
      Vector<Integer> primes = Primes.getAllPrimesUpTo(30);
      Vector<Integer> expected = new Vector<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29));
      assertEquals(expected, primes, "getAllPrimesUpTo(30) should return correct primes");
      assertEquals(10, primes.size(), "There should be 10 primes up to 30");
    }

    @Test
    @DisplayName("n=100 should return 25 primes")
    public void testGetAllPrimesUpToHundred() {
      Vector<Integer> primes = Primes.getAllPrimesUpTo(100);
      assertEquals(25, primes.size(), "There should be 25 primes up to 100");
      
      // Verify first and last primes
      assertEquals(Integer.valueOf(2), primes.get(0), "First prime should be 2");
      assertEquals(Integer.valueOf(97), primes.get(24), "Last prime up to 100 should be 97");
    }

    @Test
    @DisplayName("Verify all returned numbers are actually prime using IsPrime")
    public void testGetAllPrimesUpToCorrectnessCheck() {
      Vector<Integer> primes = Primes.getAllPrimesUpTo(50);
      
      // Every number returned should pass IsPrime check
      for (int prime : primes) {
        assertTrue(Primes.IsPrime(prime), prime + " returned by getAllPrimesUpTo should pass IsPrime check");
      }
      
      // Verify count matches expected (15 primes up to 50)
      assertEquals(15, primes.size(), "There should be 15 primes up to 50");
    }
  }

  @Nested
  @DisplayName("sumPrimesUsingSieve(int n) tests")
  class SumPrimesUsingSieveTests {

    @Test
    @DisplayName("Edge case: n=0 should return 0")
    public void testSumPrimesUsingSieveZero() {
      assertEquals(0, Primes.sumPrimesUsingSieve(0), "sumPrimesUsingSieve(0) should return 0");
    }

    @Test
    @DisplayName("Edge case: n=1 should return 0")
    public void testSumPrimesUsingSieveOne() {
      assertEquals(0, Primes.sumPrimesUsingSieve(1), "sumPrimesUsingSieve(1) should return 0");
    }

    @Test
    @DisplayName("Edge case: n=2 should return 0")
    public void testSumPrimesUsingSieveTwo() {
      assertEquals(0, Primes.sumPrimesUsingSieve(2), "sumPrimesUsingSieve(2) should return 0");
    }

    @Test
    @DisplayName("n=3 should return 2 (prime 2)")
    public void testSumPrimesUsingSieveThree() {
      assertEquals(2, Primes.sumPrimesUsingSieve(3), "sumPrimesUsingSieve(3) should return 2");
    }

    @Test
    @DisplayName("n=5 should return 5 (primes 2, 3)")
    public void testSumPrimesUsingSieveFive() {
      assertEquals(5, Primes.sumPrimesUsingSieve(5), "sumPrimesUsingSieve(5) should return 5");
    }

    @Test
    @DisplayName("n=10 should return 17 (primes 2, 3, 5, 7)")
    public void testSumPrimesUsingSieveTen() {
      assertEquals(17, Primes.sumPrimesUsingSieve(10), "sumPrimesUsingSieve(10) should return 17");
    }

    @Test
    @DisplayName("Verify sumPrimesUsingSieve matches SumPrimes for n=12")
    public void testSumPrimesUsingSieveMatchesSumPrimesTwelve() {
      int n = 12;
      long sieveResult = Primes.sumPrimesUsingSieve(n);
      int originalResult = Primes.SumPrimes(n);
      assertEquals(originalResult, sieveResult, "sumPrimesUsingSieve(" + n + ") should match SumPrimes(" + n + ")");
    }

    @Test
    @DisplayName("Verify sumPrimesUsingSieve matches SumPrimes for n=100")
    public void testSumPrimesUsingSieveMatchesSumPrimesHundred() {
      int n = 100;
      long sieveResult = Primes.sumPrimesUsingSieve(n);
      int originalResult = Primes.SumPrimes(n);
      assertEquals(originalResult, sieveResult, "sumPrimesUsingSieve(" + n + ") should match SumPrimes(" + n + ")");
    }

    @Test
    @DisplayName("Verify sumPrimesUsingSieve matches SumPrimes for n=1000")
    public void testSumPrimesUsingSieveMatchesSumPrimesThousand() {
      int n = 1000;
      long sieveResult = Primes.sumPrimesUsingSieve(n);
      int originalResult = Primes.SumPrimes(n);
      assertEquals(originalResult, sieveResult, "sumPrimesUsingSieve(" + n + ") should match SumPrimes(" + n + ")");
    }

    @Test
    @DisplayName("Large n=10000 should compute correctly")
    public void testSumPrimesUsingSieveTenThousand() {
      int n = 10000;
      long result = Primes.sumPrimesUsingSieve(n);
      // Sum of primes less than 10000 is 5736396
      assertEquals(5736396, result, "sumPrimesUsingSieve(10000) should return 5736396");
    }
  }

  @Nested
  @DisplayName("Performance tests")
  class PerformanceTests {

    @Test
    @DisplayName("Performance comparison: SumPrimes vs sumPrimesUsingSieve for n=100000")
    public void testPerformanceComparison() {
      int n = 100000;
      
      // Test sieve-based method
      long sieveStart = System.nanoTime();
      long sieveResult = Primes.sumPrimesUsingSieve(n);
      long sieveEnd = System.nanoTime();
      long sieveTime = sieveEnd - sieveStart;
      
      // Test original method
      long originalStart = System.nanoTime();
      int originalResult = Primes.SumPrimes(n);
      long originalEnd = System.nanoTime();
      long originalTime = originalEnd - originalStart;
      
      // Verify correctness
      assertEquals(originalResult, sieveResult, "Results should match");
      
      // Calculate speedup
      double speedup = (double) originalTime / sieveTime;
      
      // Print performance results
      System.out.println("\n=== Performance Test Results for n=" + n + " ===");
      System.out.println("Original SumPrimes time: " + originalTime / 1_000_000.0 + " ms");
      System.out.println("Sieve sumPrimesUsingSieve time: " + sieveTime / 1_000_000.0 + " ms");
      System.out.println("Speedup: " + String.format("%.2f", speedup) + "x faster");
      System.out.println("Result: " + sieveResult);
      
      // Sieve should be faster (though we don't assert this to avoid flaky tests)
      assertTrue(sieveResult > 0, "Sieve should compute a valid result");
    }

    @Test
    @DisplayName("Performance test: getAllPrimesUpTo for n=1000000")
    public void testPerformanceLargeN() {
      int n = 1000000;
      
      long start = System.nanoTime();
      Vector<Integer> primes = Primes.getAllPrimesUpTo(n);
      long end = System.nanoTime();
      long duration = end - start;
      
      // Print performance results
      System.out.println("\n=== Performance Test: getAllPrimesUpTo(" + n + ") ===");
      System.out.println("Time taken: " + duration / 1_000_000.0 + " ms");
      System.out.println("Primes found: " + primes.size());
      System.out.println("Expected: 78498 primes up to 1,000,000");
      
      // Verify count (there are 78,498 primes below 1,000,000)
      assertEquals(78498, primes.size(), "There should be 78,498 primes up to 1,000,000");
      
      // Verify first and last primes
      assertEquals(Integer.valueOf(2), primes.get(0), "First prime should be 2");
      assertEquals(Integer.valueOf(999983), primes.get(primes.size() - 1), "Last prime up to 1,000,000 should be 999,983");
    }

    @Test
    @DisplayName("Performance test: sumPrimesUsingSieve for n=1000000")
    public void testPerformanceSumLargeN() {
      int n = 1000000;
      
      long start = System.nanoTime();
      long sum = Primes.sumPrimesUsingSieve(n);
      long end = System.nanoTime();
      long duration = end - start;
      
      // Print performance results
      System.out.println("\n=== Performance Test: sumPrimesUsingSieve(" + n + ") ===");
      System.out.println("Time taken: " + duration / 1_000_000.0 + " ms");
      System.out.println("Sum of primes < 1,000,000: " + sum);
      System.out.println("Expected: 37,550,402,023");
      
      // Verify result (sum of primes less than 1,000,000 is 37,550,402,023)
      assertEquals(37550402023L, sum, "Sum of primes less than 1,000,000 should be 37,550,402,023");
    }
  }
}
