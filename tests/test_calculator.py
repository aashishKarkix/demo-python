import pytest

from add import add
from addmulti import add_and_multiply
from addsub import add_and_subtract
from calc import calculate


def test_add():
    assert add(2, 3) == 5


def test_add_and_multiply():
    assert add_and_multiply(4, 5) == (9, 20)


def test_add_and_subtract():
    assert add_and_subtract(7, 4) == (11, 3)


def test_calculate_add():
    assert calculate(1, "+", 2) == 3


def test_calculate_subtract():
    assert calculate(5, "-", 2) == 3


def test_calculate_multiply():
    assert calculate(3, "*", 4) == 12


def test_calculate_divide():
    assert calculate(10, "/", 2) == 5.0


def test_calculate_zero_division():
    with pytest.raises(ZeroDivisionError):
        calculate(1, "/", 0)


def test_calculate_invalid_operator():
    with pytest.raises(ValueError):
        calculate(1, "^", 2)
