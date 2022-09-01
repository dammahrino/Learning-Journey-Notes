import pytest
from stuff import Accumulator

@pytest.fixture
def accum():
    return Accumulator()