import math

import pytest

from factorial_app import factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
    ],
)
def test_known_values(n, expected):
    assert factorial(n) == expected


def test_large_number_matches_math_factorial():
    assert factorial(100) == math.factorial(100)


@pytest.mark.parametrize("n", range(0, 30))
def test_recurrence_relation(n):
    assert factorial(n + 1) == (n + 1) * factorial(n)


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_negative_raises_value_error(n):
    with pytest.raises(ValueError):
        factorial(n)


@pytest.mark.parametrize("value", [2.5, 3.0, "5", None, [5], True, False])
def test_non_integer_raises_type_error(value):
    with pytest.raises(TypeError):
        factorial(value)
