import pytest
import math_func
import sys


@pytest.mark.numbers
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7, 4) == 11
    print('test_add_result', math_func.add(7, 3), "-----------------")


@pytest.mark.skipif(sys.version_info > (3, 0), reason="Skipped test because system version is not 3.0")
def test_add_strings():
    result = math_func.add("Hello", " Hello")
    assert result == 'Hello Hello'
    assert type(result) is str
    assert 'Heldlo' not in result


@pytest.mark.number
def test_multiple():
    assert math_func.multiply(2, 2) == 4
    assert math_func.multiply(3, 4) == 12


@pytest.mark.strings
def test_multiply_strings():
    result = math_func.multiply('Hello', 3)
    assert result == 'HelloHelloHello'
    assert type(result) is str
    assert 'Hello' in result
