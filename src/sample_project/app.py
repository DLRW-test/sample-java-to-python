"""Main application entry point for sample_project.

This module serves as the main entry point for the sample project, demonstrating
all library functionality through a series of demo functions.
"""

import sys
from sample_project.control import single as single_module
from sample_project.control import double as double_module
from sample_project.datastructures import vector as vector_module
from sample_project.algorithms import primes as primes_module
from sample_project.algorithms import sort as sort_module
from sample_project.generator import vector_gen


def single() -> None:
    """Demonstrate single-loop control flow operations.
    
    Shows examples of sum_range, max_array, and sum_modulus functions
    from the control.single module.
    
    Returns:
        None.
    """
    try:
        print("SingleForLoop")
        print("-------------")
        print(f"SumRange(10): {single_module.sum_range(10)}")
        print(f"MaxArray([1, 2, 3, 4, 5]): {single_module.max_array([1, 2, 3, 4, 5])}")
        print(f"SumModulus(100, 3): {single_module.sum_modulus(100, 3)}")
        print()
    except (ValueError, TypeError) as e:
        print(f"Error in single loop operations: {e}", file=sys.stderr)
        raise


def double_() -> None:
    """Demonstrate double-loop control flow operations.
    
    Shows examples of sum_square, sum_triangle, count_pairs, and count_duplicates
    functions from the control.double module. Named double_ to avoid Python keyword.
    
    Returns:
        None.
    """
    try:
        print("DoubleForLoop")
        print("-------------")
        print(f"SumSquare(10): {double_module.sum_square(10)}")
        print(f"SumTriangle(10): {double_module.sum_triangle(10)}")
        print(f"CountPairs([1, 2, 3, 4, 5]): {double_module.count_pairs([1, 2, 3, 4, 5, 2])}")
        print(f"CountDuplicates([1, 2, 3, 4, 5], [1, 3, 2, 4, 5]): {double_module.count_duplicates([1, 2, 3, 4, 5], [1, 3, 2, 4, 5])}")
        print()
    except (ValueError, TypeError) as e:
        print(f"Error in double loop operations: {e}", file=sys.stderr)
        raise


def vector() -> None:
    """Demonstrate vector (list) manipulation operations.
    
    Shows examples of modify_vector, search_vector, sort_vector, reverse_vector,
    rotate_vector, and merge_vectors functions from the datastructures.vector module.
    
    Returns:
        None.
    """
    try:
        input_vec = vector_gen.generate_vector(10, 0, 9)
        input_vec2 = vector_gen.generate_vector(10, 0, 9)

        print("Vector")
        print("------")
        print(f"ModifyVector({input_vec}): {vector_module.modify_vector(input_vec)}")
        print(f"SearchVector({input_vec}, 5): {vector_module.search_vector(input_vec, 5)}")
        print(f"SortVector({input_vec}): {vector_module.sort_vector(input_vec)}")
        print(f"ReverseVector({input_vec}): {vector_module.reverse_vector(input_vec)}")
        print(f"RotateVector({input_vec}, 3): {vector_module.rotate_vector(input_vec, 3)}")
        print(f"MergeVectors({input_vec}, {input_vec2}): {vector_module.merge_vectors(input_vec, input_vec2)}")

        print()
    except (ValueError, TypeError) as e:
        print(f"Error in vector operations: {e}", file=sys.stderr)
        raise


def primes() -> None:
    """Demonstrate prime number operations.
    
    Shows examples of is_prime, sum_primes, and prime_factors functions
    from the algorithms.primes module.
    
    Returns:
        None.
    """
    try:
        print("Primes")
        print("------")
        print(f"IsPrime(10): {primes_module.is_prime(10)}")
        print(f"SumPrimes(10): {primes_module.sum_primes(10)}")
        print(f"PrimeFactors(10): {primes_module.prime_factors(10)}")
        print()
    except ValueError as e:
        print(f"Error in prime operations: {e}", file=sys.stderr)
        raise


def sort() -> None:
    """Demonstrate sorting and partitioning operations.
    
    Shows examples of sort_vector, dutch_flag_partition, and max_n functions
    from the algorithms.sort module.
    
    Returns:
        None.
    """
    try:
        initial_vec = vector_gen.generate_vector(20, 0, 9)
        print("Sort")
        print("------")
        input_vec0 = initial_vec.copy()
        sort_module.sort_vector(input_vec0)
        print(f"SortVector({initial_vec}): {input_vec0}")
        input_vec1 = initial_vec.copy()
        sort_module.dutch_flag_partition(input_vec1, 5)
        print(f"DutchFlagPartition({initial_vec}, 5): {input_vec1}")
        print(f"MaxN({initial_vec}, 5): {sort_module.max_n(initial_vec, 5)}")
        print()
    except (ValueError, TypeError) as e:
        print(f"Error in sort operations: {e}", file=sys.stderr)
        raise


def main() -> None:
    """Main entry point for the sample project demonstration.
    
    This function runs all demo functions in sequence to showcase the
    functionality of the sample_project library, including:
    - Single-loop control flow operations
    - Double-loop control flow operations
    - Vector (list) manipulation
    - Prime number algorithms
    - Sorting and partitioning algorithms
    
    The function handles exceptions and exits with status code 1 if any
    errors occur during execution.
    
    Returns:
        None.
    """
    try:
        single()
        double_()
        vector()
        primes()
        sort()
    except Exception as e:
        print(f"Application error: {e}", file=sys.stderr)
        print("The application encountered an error and will terminate.", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
