import pytest
from primos import is_prime

def test_is_prime():
    assert is_prime(93) == False
    assert is_prime(199) == True 