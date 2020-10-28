import pytest
from programs.near import near

def test_near():
    assert near("reset","rest") == True