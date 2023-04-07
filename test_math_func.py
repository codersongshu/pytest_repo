import math_func
import pytest
import sys

@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7, 2) == 9
    assert math_func.add(7, 1) == 8

#@pytest.mark.skip(reason="do not run this test")
@pytest.mark.skipif(sys.version_info < (3,3), reason="do not run this test")
def test_product_skipped_test():
    assert math_func.product(7,3) == 21
    assert math_func.product(7, 2) == 14
    print(math_func.add(7, 3), '-----')

@pytest.mark.strings
def test_product():
    assert math_func.product(7,3) == 21
    assert math_func.product(7, 2) == 14
    print('##############$$$$$$%%%%%%%%%')

@pytest.mark.number
def test_add_string():
    result = math_func.add("Hello"," World")
    assert result == 'Hello World'
    assert type(result) is str

@pytest.mark.strings
def test_product_string():
    result = math_func.product("Hello ",3)
    assert result == "Hello Hello Hello "
    assert type(result) is str

