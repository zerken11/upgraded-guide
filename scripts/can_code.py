"""Utility functions demonstrating coding capabilities.

This module currently provides a Fibonacci number generator and a
simple factorial implementation. Both functions are implemented with
input validation and unit-test friendly interfaces.
"""
from __future__ import annotations

from functools import lru_cache


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to compute. Must be a
            non-negative integer.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If ``n`` is negative.
        TypeError: If ``n`` is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def _fib(k: int) -> int:
        if k < 2:
            return k
        return _fib(k - 1) + _fib(k - 2)

    return _fib(n)


def factorial(n: int) -> int:
    """Compute ``n!`` for non-negative integers.

    Args:
        n: Non-negative integer.

    Returns:
        The factorial of ``n``.

    Raises:
        ValueError: If ``n`` is negative.
        TypeError: If ``n`` is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Fibonacci(10) =", fibonacci(10))
    print("Factorial(5) =", factorial(5))
