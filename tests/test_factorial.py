import pytest
from programs import factorial

def test_zero_factorial():
    assert factorial.fact(0)==1

def test_factorial():
    assert factorial.fact(2)==2