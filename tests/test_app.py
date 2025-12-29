"""
Test suite for the app module.

This module contains smoke tests for the main entry point and demo functions
in the app module. Tests verify that the CLI works correctly without checking
specific output values.
"""

import pytest


def test_module_import_no_side_effects() -> None:
    """
    Test that the app module can be imported without side effects.
    
    Verifies that importing the module doesn't automatically execute
    the main function or produce any output.
    """
    import sample_project.app  # noqa: F401


def test_main_executes_without_errors(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that the main() function executes without raising exceptions.
    
    This is a smoke test that verifies the main entry point can run
    to completion without errors. Uses capsys to capture any output
    but doesn't validate specific values.
    """
    from sample_project.app import main
    
    # Should not raise any exceptions
    main()
    
    # Verify some output was generated
    captured = capsys.readouterr()
    assert len(captured.out) > 0, "main() should generate console output"


def test_demo_functions_individually(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that each demo function can be called individually without errors.
    
    Verifies that single(), double_(), vector(), primes(), and sort()
    can each be executed independently without raising exceptions.
    """
    from sample_project.app import double_, primes, single, sort, vector
    
    # Test each function individually
    demo_functions = [single, double_, vector, primes, sort]
    
    for func in demo_functions:
        # Clear previous output
        capsys.readouterr()
        
        # Should not raise any exceptions
        func()
        
        # Verify output was generated
        captured = capsys.readouterr()
        assert len(captured.out) > 0, f"{func.__name__}() should generate output"


def test_output_generation(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that console output is generated when main() executes.
    
    Verifies that the main function produces non-empty output to stdout.
    This ensures the demo functions are actually printing results.
    """
    from sample_project.app import main
    
    main()
    
    captured = capsys.readouterr()
    
    # Verify stdout has content
    assert captured.out, "Output should be written to stdout"
    assert len(captured.out) > 100, "Output should be substantial"
    
    # Verify output contains section headers from demo functions
    expected_sections = [
        "SingleForLoop",
        "DoubleForLoop",
        "Vector",
        "Primes",
        "Sort"
    ]
    
    for section in expected_sections:
        assert section in captured.out, f"Output should contain '{section}' section"


def test_single_function_output(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that the single() function generates expected output structure.
    
    Verifies the function executes and produces output containing
    the SingleForLoop section header and separator.
    """
    from sample_project.app import single
    
    single()
    
    captured = capsys.readouterr()
    assert "SingleForLoop" in captured.out
    assert "-------------" in captured.out


def test_double_function_output(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that the double_() function generates expected output structure.
    
    Verifies the function executes and produces output containing
    the DoubleForLoop section header and separator.
    """
    from sample_project.app import double_
    
    double_()
    
    captured = capsys.readouterr()
    assert "DoubleForLoop" in captured.out
    assert "-------------" in captured.out


def test_vector_function_output(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that the vector() function generates expected output structure.
    
    Verifies the function executes and produces output containing
    the Vector section header and separator.
    """
    from sample_project.app import vector
    
    vector()
    
    captured = capsys.readouterr()
    assert "Vector" in captured.out
    assert "------" in captured.out


def test_primes_function_output(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that the primes() function generates expected output structure.
    
    Verifies the function executes and produces output containing
    the Primes section header and separator.
    """
    from sample_project.app import primes
    
    primes()
    
    captured = capsys.readouterr()
    assert "Primes" in captured.out
    assert "------" in captured.out


def test_sort_function_output(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test that the sort() function generates expected output structure.
    
    Verifies the function executes and produces output containing
    the Sort section header and separator.
    """
    from sample_project.app import sort
    
    sort()
    
    captured = capsys.readouterr()
    assert "Sort" in captured.out
    assert "------" in captured.out
