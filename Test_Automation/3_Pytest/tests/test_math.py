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
    
    
# --------------------------------------------------------------------------------
# Parameterized Test Cases
# --------------------------------------------------------------------------------

products = [
    (2, 3, 6),          # Positive ints
    (1, 99, 99),        # Identity
    (0, 99, 0),         # Zero
    (3, -4, -12),       # Pos x neg
    (-5, -5, 25),       # Neg x Neg
    (2.5, 6.7, 16.75)   # Floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product