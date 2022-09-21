"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.

"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator

# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0
    
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1
    
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3
    
def test_accumulator_add_twice():
    # AAA pattern
    
    # Arrange
    accum = Accumulator()
    
    # Act
    accum.add()
    accum.add()
    
    # Assert 
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError) as e:
        accum.count = 10
        
    assert 'can\'t set attribute' in str(e.value)