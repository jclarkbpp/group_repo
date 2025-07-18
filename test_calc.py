import pytest
from calc import add, divide, multiply, subtract

def test_add(self):
    result = add(10, 5)
    assert result == 15

def test_subtract(self):
    result = subtract(10, 5)
    assert result == 5
    
def test_multiply(self):
    result = multiply(10, 5)
    assert result == 50

def test_divide(self):
    result = divide(10, 5)
    assert result == 2



