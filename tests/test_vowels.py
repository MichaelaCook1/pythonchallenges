import pytest
from programs import vowels

def test_no_vowels():
    assert vowels.vowels("my") ==0

def test_vowels():
    assert vowels.vowels("start") ==1