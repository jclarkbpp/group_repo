import pytest
from calc import add, divide, multiply, subtract

def test_add():
    result = add(10, 5)
    assert result == 15

def test_subtract():
    result = subtract(10, 5)
    assert result == 5
    
def test_multiply():
    result = multiply(10, 5)
    assert result == 50

def test_divide():
    result = divide(10, 5)
    assert result == 2



