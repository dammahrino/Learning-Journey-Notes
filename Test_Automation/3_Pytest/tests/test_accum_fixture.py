"""
This module ccontains a modified version of the test_accum.py class with
fixtures included to align to the DRY principle.

"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator

# --------------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------------

@pytest.fixture
def accum():
    return Accumulator()

# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0
    
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1
    
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3
    
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError) as e:
        accum.count = 10
        
    assert 'can\'t set attribute' in str(e.value)