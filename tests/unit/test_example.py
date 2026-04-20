"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from pyospackage_feulloah.example import add_numbers, multiply_integers_slow

def test_add_numbers_pos():
    """
    Test that add_numbers works as expected with 2 positive inputs.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_add_numbers_neg():
    """
    Test that add_numbers works as expected with 2 negative inputs.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(-1, -2)
    expected_out = -3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_add_numbers_posneg():
    """
    Test that add_numbers works as expected with a positive and a negative input.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, -2)
    expected_out = -1
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_integers_slow_pos():
    """
    Test that multiply_integers_slow works as expected with 2 positive inputs.

    A single line docstring for tests is generally sufficient.
    """
    out = multiply_integers_slow(1, 2)
    expected_out = 2
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_integers_slow_neg():
    """
    Test that multiply_integers_slow works as expected with two negative values.

    A single line docstring for tests is generally sufficient.
    """
    out = multiply_integers_slow(-10, -3)
    expected_out = 30
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_integers_slow_posneg():
    """
    Test that multiply_integers_slow works as expected with a positive and negative value.

    A single line docstring for tests is generally sufficient.
    """
    out = multiply_integers_slow(-1, 2)
    expected_out = multiply_integers_slow(-2,1)
    assert  out == expected_out, f"Expected {expected_out} but got {out}"
