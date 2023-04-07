import math_func
import pytest
import sys

@pytest.mark.parametrize('num1, num2, result',
                         [(7,3,10),('Hello',' World','Hello World'),(10.5,5.5,16)]
                         )
def test_add(num1, num2, result):
    assert math_func.add(num1,num2) == result