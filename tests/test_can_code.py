import pytest

from scripts.can_code import factorial, fibonacci


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (10, 55),
        (20, 6765),
    ],
)
def test_fibonacci_valid_inputs(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize("invalid", [1.5, "3", None])
def test_fibonacci_invalid_type(invalid):
    with pytest.raises(TypeError):
        fibonacci(invalid)  # type: ignore[arg-type]


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_valid_inputs(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("invalid", [2.2, "4", object()])
def test_factorial_invalid_type(invalid):
    with pytest.raises(TypeError):
        factorial(invalid)  # type: ignore[arg-type]


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)
