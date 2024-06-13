import pytest

from outputs_input import output_input

def test_func_one():
    assert "Hello" == output_input("Hello")

def test_func_two_error():
    assert "ERROR" == output_input(":P")