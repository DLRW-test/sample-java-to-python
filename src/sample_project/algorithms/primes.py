"""Prime number algorithms module.

This module provides prime number algorithms including the Sieve of Eratosthenes,
primality testing, and prime factorization. All functions use efficient algorithms
optimized for performance while maintaining clear, readable implementations.

Functions:
    generate_sieve: Generate a boolean sieve for prime detection using Sieve of Eratosthenes.
    is_prime: Check if a number is prime using sieve lookup.
    sum_primes: Sum all prime numbers less than n.
    get_all_primes_up_to: Get all prime numbers up to and including n.
    prime_factors: Find all prime factors of a number using trial division.
    sum_primes_using_sieve: Sum all prime numbers less than n using sieve (returns int).
"""


def generate_sieve(n: int) -> list[bool]:
    """Generate a sieve of Eratosthenes for prime detection up to the given limit.

    This is the core algorithm used by all prime-related methods in this module.
    The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers
    up to a specified integer by iteratively marking the multiples of each prime
    as composite.

    Algorithm: Sieve of Eratosthenes
        1. Create a boolean array of size n+1, initially all True
        2. Mark 0 and 1 as not prime (False)
        3. For each number i from 2 to √n:
           - If i is marked as prime, mark all multiples of i (starting from i²) as composite
        4. Return the sieve array

    Note:
        Time complexity: O(n log log n)
        Space complexity: O(n)

    Memory Requirements:
        - n = 10: ~10 bytes
        - n = 100: ~100 bytes
        - n = 1,000: ~1 KB
        - n = 10,000: ~10 KB
        - n = 100,000: ~100 KB
        - n = 1,000,000: ~1 MB
        - n = 10,000,000: ~10 MB
        - n = 100,000,000: ~100 MB

    Args:
        n: The upper bound (inclusive) for the sieve.

    Returns:
        A boolean list where is_prime[i] is True if i is prime, False otherwise.
        The list has length n+1 to allow direct indexing by number.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> sieve = generate_sieve(10)
        >>> sieve[2]  # 2 is prime
        True
        >>> sieve[4]  # 4 is not prime
        False
        >>> [i for i in range(11) if sieve[i]]
        [2, 3, 5, 7]
    """
    if n < 0:
        raise ValueError(f"Limit cannot be negative: {n}")
    
    if n < 2:
        return [False] * (n + 1)
    
    # Initialize all numbers as potentially prime
    is_prime = [False] * (n + 1)
    for i in range(2, n + 1):
        is_prime[i] = True
    
    # Sieve of Eratosthenes algorithm
    i = 2
    while i * i <= n:
        if is_prime[i]:
            # Mark all multiples of i as composite
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1
    
    return is_prime


def is_prime(n: int) -> bool:
    """Check if a number is prime using the Sieve of Eratosthenes algorithm.

    This method generates a sieve up to n and performs a direct lookup.
    For repeated primality checks, consider using get_all_primes_up_to()
    to generate the sieve once and reuse it.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, False otherwise. Returns False for
        numbers less than 2 (including negative numbers).

    Note:
        Time complexity: O(n log log n) for sieve generation + O(1) lookup
        Space complexity: O(n)
        Memory usage: Allocates approximately n bytes for the sieve array.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(-5)
        False
    """
    if n < 2:
        return False
    
    sieve = generate_sieve(n)
    return sieve[n]


def sum_primes(n: int) -> int:
    """Sum all prime numbers from 0 to n (exclusive) using the Sieve of Eratosthenes.

    This method generates a sieve up to n-1 and sums all numbers marked as prime.
    This replaces the previous trial division approach with a single-pass sieve
    generation followed by a summation.

    Args:
        n: The upper bound (exclusive) - sums all primes less than n.

    Returns:
        The sum of all prime numbers less than n.

    Raises:
        ValueError: If n is negative.

    Note:
        Time complexity: O(n log log n) for sieve + O(n) for summation = O(n log log n)
        Space complexity: O(n)
        Memory usage: Allocates approximately n bytes for the sieve array.
        Previous implementation: O(n * √n) with trial division

    Examples:
        >>> sum_primes(10)
        17
        >>> sum_primes(5)
        5
        >>> sum_primes(2)
        0
    """
    if n < 0:
        raise ValueError(f"Upper bound cannot be negative: {n}")
    
    if n <= 2:
        return 0
    
    sieve = generate_sieve(n - 1)
    total = 0
    
    for i in range(2, n):
        if sieve[i]:
            total += i
    
    return total


def get_all_primes_up_to(n: int) -> list[int]:
    """Return all prime numbers up to and including n using the Sieve of Eratosthenes.

    This utility method exposes the sieve results directly, which is useful when
    you need to perform multiple operations with primes in a range. It's more
    efficient to call this once and reuse the result than to call is_prime()
    repeatedly.

    Args:
        n: The upper bound (inclusive) for prime generation.

    Returns:
        A list containing all prime numbers from 2 to n (inclusive).

    Raises:
        ValueError: If n is negative.

    Note:
        Time complexity: O(n log log n) for sieve generation + O(n) for collection
        Space complexity: O(n) for sieve + O(π(n)) for result list (where π(n) ≈ n/ln(n))
        Memory usage: Allocates approximately n bytes for the sieve array plus storage for the returned prime numbers.

    Examples:
        >>> get_all_primes_up_to(10)
        [2, 3, 5, 7]
        >>> get_all_primes_up_to(1)
        []
        >>> get_all_primes_up_to(2)
        [2]
    """
    if n < 0:
        raise ValueError(f"Upper bound cannot be negative: {n}")
    
    primes = []
    
    if n < 2:
        return primes
    
    sieve = generate_sieve(n)
    
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
    
    return primes


def prime_factors(n: int) -> list[int]:
    """Find all prime factors of a number using trial division.

    This method uses trial division with optimization to only check divisors
    up to √n. The result includes repeated prime factors (e.g., 12 = [2, 2, 3]).

    Algorithm:
        1. For each potential divisor i from 2 to √n:
           - While n is divisible by i, add i to the result and divide n by i
        2. If n > 1 after the loop, n itself is a prime factor

    Args:
        n: The number to find the prime factors of.

    Returns:
        A list of all prime factors of n (with repetition for prime powers).

    Raises:
        ValueError: If n is less than or equal to 0.

    Note:
        Time complexity: O(√n) in the worst case (when n is prime)
        Space complexity: O(log n) for the result list
        For factoring multiple numbers, consider pre-generating a sieve of primes
        up to √(max_n) and using those as trial divisors for improved performance.

    Examples:
        >>> prime_factors(12)
        [2, 2, 3]
        >>> prime_factors(7)
        [7]
        >>> prime_factors(1)
        []
        >>> prime_factors(30)
        [2, 3, 5]
    """
    if n <= 0:
        raise ValueError(f"Number must be positive: {n}")
    
    factors = []
    
    # Trial division up to sqrt(n)
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    
    # If n > 1, then it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


def sum_primes_using_sieve(n: int) -> int:
    """Sum all prime numbers from 0 to n using the Sieve of Eratosthenes algorithm.

    This method uses the same sieve algorithm as sum_primes() and produces identical
    results. Both methods have the same time and space complexity.

    Args:
        n: The upper limit (exclusive) for prime summation.

    Returns:
        The sum of all prime numbers less than n as an int.

    Raises:
        ValueError: If n is negative.

    Note:
        Time complexity: O(n log log n) (Sieve of Eratosthenes)
        Space complexity: O(n)
        Performance comparison: sum_primes() and sum_primes_using_sieve() have
        identical performance and return int. For large n (e.g., n=1,000,000),
        both methods have similar performance.

    Examples:
        >>> sum_primes_using_sieve(10)
        17
        >>> sum_primes_using_sieve(5)
        5
        >>> sum_primes_using_sieve(2)
        0
    """
    if n < 0:
        raise ValueError(f"Upper limit cannot be negative: {n}")
    
    if n < 2:
        return 0
    
    sieve = generate_sieve(n - 1)
    total = 0
    
    # Sum all prime numbers
    for i in range(2, n):
        if sieve[i]:
            total += i
    
    return total
