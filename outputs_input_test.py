import pytest

from outputs_input import output_input

def test_func_one():
    assert "Hello" == output_input("Hello")