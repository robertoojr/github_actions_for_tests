from functions import *

def test_sum():
    result = sum_numbers(3, 2)
    assert result == 5

def test_subtract():
    result = subtract_numbers(3, 2)
    assert result == 1
