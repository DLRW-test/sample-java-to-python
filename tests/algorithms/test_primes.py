"""
Comprehensive test suite for the algorithms.primes module.
Translated from algorithms.PrimesTest.java (JUnit 5 to pytest).
"""

import pytest
from sample_project.algorithms.primes import (
    is_prime,
    sum_primes,
    prime_factors,
    generate_sieve,
    get_all_primes_up_to,
    sum_primes_using_sieve,
)


# ============================================================================
# IsPrime(int n) tests
# ============================================================================

class TestIsPrime:
    """Tests for the is_prime function."""

    def test_is_prime_negative(self):
        """Edge case: negative numbers should return False"""
        assert not is_prime(-1), "is_prime(-1) should return False"
        assert not is_prime(-5), "is_prime(-5) should return False"
        assert not is_prime(-100), "is_prime(-100) should return False"

    def test_is_prime_zero(self):
        """Edge case: n=0 should return False"""
        assert not is_prime(0), "is_prime(0) should return False"

    def test_is_prime_one(self):
        """Edge case: n=1 should return False"""
        assert not is_prime(1), "is_prime(1) should return False"

    def test_is_prime_two(self):
        """n=2 (smallest prime) should return True"""
        assert is_prime(2), "is_prime(2) should return True"

    def test_is_prime_small_primes(self):
        """Small primes: 3, 5, 7 should return True"""
        assert is_prime(3), "is_prime(3) should return True"
        assert is_prime(5), "is_prime(5) should return True"
        assert is_prime(7), "is_prime(7) should return True"

    def test_is_prime_small_composites(self):
        """Small composites: 4, 6, 8, 9 should return False"""
        assert not is_prime(4), "is_prime(4) should return False"
        assert not is_prime(6), "is_prime(6) should return False"
        assert not is_prime(8), "is_prime(8) should return False"
        assert not is_prime(9), "is_prime(9) should return False"

    def test_is_prime_larger_primes(self):
        """Larger primes: 13, 17, 19 should return True"""
        assert is_prime(13), "is_prime(13) should return True"
        assert is_prime(17), "is_prime(17) should return True"
        assert is_prime(19), "is_prime(19) should return True"

    def test_is_prime_larger_composites(self):
        """Larger composites: 15, 20, 100 should return False"""
        assert not is_prime(15), "is_prime(15) should return False"
        assert not is_prime(20), "is_prime(20) should return False"
        assert not is_prime(100), "is_prime(100) should return False"


# ============================================================================
# SumPrimes(int n) tests
# ============================================================================

class TestSumPrimes:
    """Tests for the sum_primes function."""

    def test_sum_primes_negative(self):
        """Exception: negative input should raise ValueError"""
        with pytest.raises(ValueError) as exc_info:
            sum_primes(-1)
        assert "negative" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            sum_primes(-10)
        assert "negative" in str(exc_info.value).lower()

    def test_sum_primes_zero(self):
        """Edge case: n=0 should return 0"""
        assert sum_primes(0) == 0, "sum_primes(0) should return 0"

    def test_sum_primes_one(self):
        """Edge case: n=1 should return 0 (no primes less than 1)"""
        assert sum_primes(1) == 0, "sum_primes(1) should return 0"

    def test_sum_primes_two(self):
        """Edge case: n=2 should return 0 (no primes less than 2)"""
        assert sum_primes(2) == 0, "sum_primes(2) should return 0"

    def test_sum_primes_five(self):
        """n=5 should return 5 (primes < 5: 2, 3)"""
        # Primes less than 5 are: 2, 3
        # Sum = 2 + 3 = 5
        assert sum_primes(5) == 5, "sum_primes(5) should return 5"

    def test_sum_primes_six(self):
        """n=6 should return 10 (primes < 6: 2, 3, 5)"""
        # Primes less than 6 are: 2, 3, 5
        # Sum = 2 + 3 + 5 = 10
        assert sum_primes(6) == 10, "sum_primes(6) should return 10"

    def test_sum_primes_ten(self):
        """n=10 should return 17 (primes < 10: 2, 3, 5, 7)"""
        # Primes less than 10 are: 2, 3, 5, 7
        # Sum = 2 + 3 + 5 + 7 = 17
        assert sum_primes(10) == 17, "sum_primes(10) should return 17"

    def test_sum_primes_eleven(self):
        """n=11 should return 17 (primes < 11: 2, 3, 5, 7)"""
        # Primes less than 11 are: 2, 3, 5, 7
        # Sum = 2 + 3 + 5 + 7 = 17
        assert sum_primes(11) == 17, "sum_primes(11) should return 17"

    def test_sum_primes_twelve(self):
        """n=12 should return 28 (primes < 12: 2, 3, 5, 7, 11)"""
        # Primes less than 12 are: 2, 3, 5, 7, 11
        # Sum = 2 + 3 + 5 + 7 + 11 = 28
        assert sum_primes(12) == 28, "sum_primes(12) should return 28"


# ============================================================================
# PrimeFactors(int n) tests
# ============================================================================

class TestPrimeFactors:
    """Tests for the prime_factors function."""

    def test_prime_factors_invalid(self):
        """Exception: n <= 0 should raise ValueError"""
        with pytest.raises(ValueError) as exc_info:
            prime_factors(0)
        assert "positive" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            prime_factors(-1)
        assert "positive" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            prime_factors(-10)
        assert "positive" in str(exc_info.value).lower()

    def test_prime_factors_one(self):
        """Edge case: n=1 should return empty list"""
        result = prime_factors(1)
        assert len(result) == 0, "prime_factors(1) should return empty list"

    def test_prime_factors_two(self):
        """Edge case: n=2 should return [2]"""
        expected = [2]
        assert prime_factors(2) == expected, "prime_factors(2) should return [2]"

    def test_prime_factors_seven(self):
        """Prime input: n=7 should return [7]"""
        expected = [7]
        assert prime_factors(7) == expected, "prime_factors(7) should return [7]"

    def test_prime_factors_eleven(self):
        """Prime input: n=11 should return [11]"""
        expected = [11]
        assert prime_factors(11) == expected, "prime_factors(11) should return [11]"

    def test_prime_factors_thirteen(self):
        """Prime input: n=13 should return [13]"""
        expected = [13]
        assert prime_factors(13) == expected, "prime_factors(13) should return [13]"

    def test_prime_factors_twelve(self):
        """Composite input: n=12 should return [2, 2, 3]"""
        # 12 = 2 * 2 * 3
        expected = [2, 2, 3]
        msg = "prime_factors(12) should return [2, 2, 3]"
        assert prime_factors(12) == expected, msg

    def test_prime_factors_eighteen(self):
        """Composite input: n=18 should return [2, 3, 3]"""
        # 18 = 2 * 3 * 3
        expected = [2, 3, 3]
        msg = "prime_factors(18) should return [2, 3, 3]"
        assert prime_factors(18) == expected, msg

    def test_prime_factors_twenty_four(self):
        """Composite input: n=24 should return [2, 2, 2, 3]"""
        # 24 = 2 * 2 * 2 * 3
        expected = [2, 2, 2, 3]
        msg = "prime_factors(24) should return [2, 2, 2, 3]"
        assert prime_factors(24) == expected, msg

    def test_prime_factors_four(self):
        """Perfect square: n=4 should return [2, 2]"""
        # 4 = 2 * 2
        expected = [2, 2]
        assert prime_factors(4) == expected, "prime_factors(4) should return [2, 2]"

    def test_prime_factors_nine(self):
        """Perfect square: n=9 should return [3, 3]"""
        # 9 = 3 * 3
        expected = [3, 3]
        assert prime_factors(9) == expected, "prime_factors(9) should return [3, 3]"

    def test_prime_factors_sixteen(self):
        """Perfect square: n=16 should return [2, 2, 2, 2]"""
        # 16 = 2 * 2 * 2 * 2
        expected = [2, 2, 2, 2]
        msg = "prime_factors(16) should return [2, 2, 2, 2]"
        assert prime_factors(16) == expected, msg

    def test_prime_factors_thirty(self):
        """Composite with larger factors: n=30 should return [2, 3, 5]"""
        # 30 = 2 * 3 * 5
        expected = [2, 3, 5]
        msg = "prime_factors(30) should return [2, 3, 5]"
        assert prime_factors(30) == expected, msg


# ============================================================================
# generateSieve(int n) tests
# ============================================================================

class TestGenerateSieve:
    """Tests for the generate_sieve function."""

    def test_generate_sieve_negative(self):
        """Exception: negative input should raise ValueError"""
        with pytest.raises(ValueError) as exc_info:
            generate_sieve(-1)
        assert "negative" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            generate_sieve(-10)
        assert "negative" in str(exc_info.value).lower()

    def test_generate_sieve_zero(self):
        """Edge case: n=0 should return array with no primes"""
        sieve = generate_sieve(0)
        assert len(sieve) == 1, "generate_sieve(0) should return array of length 1"
        assert not sieve[0], "sieve[0] should be False (0 is not prime)"

    def test_generate_sieve_one(self):
        """Edge case: n=1 should return array with no primes"""
        sieve = generate_sieve(1)
        assert len(sieve) == 2, "generate_sieve(1) should return array of length 2"
        assert not sieve[0], "sieve[0] should be False (0 is not prime)"
        assert not sieve[1], "sieve[1] should be False (1 is not prime)"

    def test_generate_sieve_two(self):
        """Edge case: n=2 should mark 2 as prime"""
        sieve = generate_sieve(2)
        assert len(sieve) == 3, "generate_sieve(2) should return array of length 3"
        assert not sieve[0], "sieve[0] should be False (0 is not prime)"
        assert not sieve[1], "sieve[1] should be False (1 is not prime)"
        assert sieve[2], "sieve[2] should be True (2 is prime)"

    def test_generate_sieve_ten(self):
        """n=10 should correctly identify primes: 2, 3, 5, 7"""
        sieve = generate_sieve(10)
        # Primes up to 10: 2, 3, 5, 7
        assert sieve[2], "2 should be prime"
        assert sieve[3], "3 should be prime"
        assert not sieve[4], "4 should not be prime"
        assert sieve[5], "5 should be prime"
        assert not sieve[6], "6 should not be prime"
        assert sieve[7], "7 should be prime"
        assert not sieve[8], "8 should not be prime"
        assert not sieve[9], "9 should not be prime"
        assert not sieve[10], "10 should not be prime"

    def test_generate_sieve_thirty(self):
        """n=30 should correctly identify all primes up to 30"""
        sieve = generate_sieve(30)
        # Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        for prime in expected_primes:
            assert sieve[prime], f"{prime} should be prime"

        # Check some composites
        assert not sieve[4], "4 should not be prime"
        assert not sieve[15], "15 should not be prime"
        assert not sieve[25], "25 should not be prime"
        assert not sieve[30], "30 should not be prime"

    def test_generate_sieve_hundred(self):
        """n=100 should count 25 primes"""
        sieve = generate_sieve(100)
        prime_count = sum(1 for i in range(101) if sieve[i])
        assert prime_count == 25, "There should be 25 primes up to 100"


# ============================================================================
# getAllPrimesUpTo(int n) tests
# ============================================================================

class TestGetAllPrimesUpTo:
    """Tests for the get_all_primes_up_to function."""

    def test_get_all_primes_up_to_negative(self):
        """Exception: negative input should raise ValueError"""
        with pytest.raises(ValueError) as exc_info:
            get_all_primes_up_to(-5)
        assert "negative" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            get_all_primes_up_to(-100)
        assert "negative" in str(exc_info.value).lower()

    def test_get_all_primes_up_to_zero(self):
        """Edge case: n=0 should return empty list"""
        primes = get_all_primes_up_to(0)
        assert len(primes) == 0, "get_all_primes_up_to(0) should return empty list"

    def test_get_all_primes_up_to_one(self):
        """Edge case: n=1 should return empty list"""
        primes = get_all_primes_up_to(1)
        assert len(primes) == 0, "get_all_primes_up_to(1) should return empty list"

    def test_get_all_primes_up_to_two(self):
        """Edge case: n=2 should return [2]"""
        expected = [2]
        msg = "get_all_primes_up_to(2) should return [2]"
        assert get_all_primes_up_to(2) == expected, msg

    def test_get_all_primes_up_to_ten(self):
        """n=10 should return [2, 3, 5, 7]"""
        expected = [2, 3, 5, 7]
        msg = "get_all_primes_up_to(10) should return [2, 3, 5, 7]"
        assert get_all_primes_up_to(10) == expected, msg

    def test_get_all_primes_up_to_twenty(self):
        """n=20 should return correct primes"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        msg = "get_all_primes_up_to(20) should return all primes up to 20"
        assert get_all_primes_up_to(20) == expected, msg

    def test_get_all_primes_up_to_thirty(self):
        """n=30 should return 10 primes"""
        primes = get_all_primes_up_to(30)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert primes == expected, "get_all_primes_up_to(30) should return correct primes"
        assert len(primes) == 10, "There should be 10 primes up to 30"

    def test_get_all_primes_up_to_hundred(self):
        """n=100 should return 25 primes"""
        primes = get_all_primes_up_to(100)
        assert len(primes) == 25, "There should be 25 primes up to 100"

        # Verify first and last primes
        assert primes[0] == 2, "First prime should be 2"
        assert primes[24] == 97, "Last prime up to 100 should be 97"

    def test_get_all_primes_up_to_correctness_check(self):
        """Verify all returned numbers are actually prime using is_prime"""
        primes = get_all_primes_up_to(50)

        # Every number returned should pass is_prime check
        for prime in primes:
            msg = (
                f"{prime} returned by get_all_primes_up_to should pass "
                "is_prime check"
            )
            assert is_prime(prime), msg

        # Verify count matches expected (15 primes up to 50)
        assert len(primes) == 15, "There should be 15 primes up to 50"


# ============================================================================
# sumPrimesUsingSieve(int n) tests
# ============================================================================

class TestSumPrimesUsingSieve:
    """Tests for the sum_primes_using_sieve function."""

    def test_sum_primes_using_sieve_negative(self):
        """Exception: negative input should raise ValueError"""
        with pytest.raises(ValueError) as exc_info:
            sum_primes_using_sieve(-10)
        assert "negative" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            sum_primes_using_sieve(-1)
        assert "negative" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            sum_primes_using_sieve(-100)
        assert "negative" in str(exc_info.value).lower()

    def test_sum_primes_using_sieve_zero(self):
        """Edge case: n=0 should return 0"""
        assert sum_primes_using_sieve(0) == 0, "sum_primes_using_sieve(0) should return 0"

    def test_sum_primes_using_sieve_one(self):
        """Edge case: n=1 should return 0"""
        assert sum_primes_using_sieve(1) == 0, "sum_primes_using_sieve(1) should return 0"

    def test_sum_primes_using_sieve_two(self):
        """Edge case: n=2 should return 0"""
        assert sum_primes_using_sieve(2) == 0, "sum_primes_using_sieve(2) should return 0"

    def test_sum_primes_using_sieve_three(self):
        """n=3 should return 2 (prime 2)"""
        assert sum_primes_using_sieve(3) == 2, "sum_primes_using_sieve(3) should return 2"

    def test_sum_primes_using_sieve_five(self):
        """n=5 should return 5 (primes 2, 3)"""
        assert sum_primes_using_sieve(5) == 5, "sum_primes_using_sieve(5) should return 5"

    def test_sum_primes_using_sieve_ten(self):
        """n=10 should return 17 (primes 2, 3, 5, 7)"""
        assert sum_primes_using_sieve(10) == 17, "sum_primes_using_sieve(10) should return 17"

    def test_sum_primes_using_sieve_matches_sum_primes_twelve(self):
        """Verify sum_primes_using_sieve matches sum_primes for n=12"""
        n = 12
        sieve_result = sum_primes_using_sieve(n)
        original_result = sum_primes(n)
        msg = f"sum_primes_using_sieve({n}) should match sum_primes({n})"
        assert sieve_result == original_result, msg

    def test_sum_primes_using_sieve_matches_sum_primes_hundred(self):
        """Verify sum_primes_using_sieve matches sum_primes for n=100"""
        n = 100
        sieve_result = sum_primes_using_sieve(n)
        original_result = sum_primes(n)
        msg = f"sum_primes_using_sieve({n}) should match sum_primes({n})"
        assert sieve_result == original_result, msg

    def test_sum_primes_using_sieve_matches_sum_primes_thousand(self):
        """Verify sum_primes_using_sieve matches sum_primes for n=1000"""
        n = 1000
        sieve_result = sum_primes_using_sieve(n)
        original_result = sum_primes(n)
        msg = f"sum_primes_using_sieve({n}) should match sum_primes({n})"
        assert sieve_result == original_result, msg

    def test_sum_primes_using_sieve_ten_thousand(self):
        """Large n=10000 should compute correctly"""
        n = 10000
        result = sum_primes_using_sieve(n)
        # Sum of primes less than 10000 is 5736396
        assert result == 5736396, "sum_primes_using_sieve(10000) should return 5736396"


# ============================================================================
# Performance tests
# ============================================================================

class TestPerformance:
    """Performance tests for prime algorithms."""

    def test_performance_comparison(self):
        """Performance comparison: sum_primes vs sum_primes_using_sieve."""
        import time

        n = 100000

        # Test sieve-based method
        sieve_start = time.perf_counter_ns()
        sieve_result = sum_primes_using_sieve(n)
        sieve_end = time.perf_counter_ns()
        sieve_time = sieve_end - sieve_start

        # Test original method
        original_start = time.perf_counter_ns()
        original_result = sum_primes(n)
        original_end = time.perf_counter_ns()
        original_time = original_end - original_start

        # Verify correctness
        assert sieve_result == original_result, "Results should match"

        # Calculate speedup
        speedup = original_time / sieve_time

        # Print performance results
        print(f"\n=== Performance Test Results for n={n} ===")
        print(f"Original sum_primes time: {original_time / 1_000_000:.3f} ms")
        print(f"Sieve sum_primes_using_sieve time: {sieve_time / 1_000_000:.3f} ms")
        print(f"Speedup: {speedup:.2f}x faster")
        print(f"Result: {sieve_result}")

        # Sieve should compute a valid result
        assert sieve_result > 0, "Sieve should compute a valid result"

    def test_performance_large_n(self):
        """Performance test: get_all_primes_up_to for n=1000000"""
        import time

        n = 1000000

        start = time.perf_counter_ns()
        primes = get_all_primes_up_to(n)
        end = time.perf_counter_ns()
        duration = end - start

        # Print performance results
        print(f"\n=== Performance Test: get_all_primes_up_to({n}) ===")
        print(f"Time taken: {duration / 1_000_000:.3f} ms")
        print(f"Primes found: {len(primes)}")
        print(f"Expected: 78498 primes up to 1,000,000")

        # Verify count (there are 78,498 primes below 1,000,000)
        msg = "There should be 78,498 primes up to 1,000,000"
        assert len(primes) == 78498, msg

        # Verify first and last primes
        assert primes[0] == 2, "First prime should be 2"
        assert primes[-1] == 999983, "Last prime up to 1,000,000 should be 999,983"

    def test_performance_sum_large_n(self):
        """Performance test: sum_primes_using_sieve for n=1000000"""
        import time

        n = 1000000

        start = time.perf_counter_ns()
        sum_val = sum_primes_using_sieve(n)
        end = time.perf_counter_ns()
        duration = end - start

        # Print performance results
        print(f"\n=== Performance Test: sum_primes_using_sieve({n}) ===")
        print(f"Time taken: {duration / 1_000_000:.3f} ms")
        print(f"Sum of primes < 1,000,000: {sum_val}")
        print(f"Expected: 37,550,402,023")

        # Verify result (sum of primes less than 1,000,000 is 37,550,402,023)
        msg = "Sum of primes less than 1,000,000 should be 37,550,402,023"
        assert sum_val == 37550402023, msg
