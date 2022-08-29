"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# A very basic example
# --------------------------------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1 == 2
    
# --------------------------------------------------------------------------------
# A test function to show assertion instrospection
# --------------------------------------------------------------------------------

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
    
    
# --------------------------------------------------------------------------------
# A test function that verifies an exception
# --------------------------------------------------------------------------------

# Import
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
        
    assert 'division by zero' in str(e.value)