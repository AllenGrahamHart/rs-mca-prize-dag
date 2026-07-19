#!/usr/bin/env python3
"""Independent polynomial-fiber audit for the residual atlas."""

from __future__ import annotations


P = 101


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % P
    return tuple(answer)


def subtract(left: tuple[int, ...], right: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return tuple(
        ((left[i] if i < len(left) else 0) - scalar * (right[i] if i < len(right) else 0)) % P
        for i in range(size)
    )


def evaluate(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def linear(root: int) -> tuple[int, ...]:
    return (-root % P, 1)


def maximum_fiber(numerator: tuple[int, ...], denominator: tuple[int, ...]) -> int:
    maximum = 0
    for parameter in range(P):
        equation = subtract(numerator, denominator, parameter)
        assert any(equation)
        roots = sum(evaluate(equation, x) == 0 and evaluate(denominator, x) != 0 for x in range(P))
        maximum = max(maximum, roots)
    return maximum


def main() -> None:
    mobius = maximum_fiber(linear(2), linear(3))
    cross_ratio = maximum_fiber(
        multiply(linear(2), linear(5)), multiply(linear(3), linear(7))
    )
    pendant_linear = maximum_fiber(linear(11), multiply(linear(13), linear(17)))
    pendant_quadratic = maximum_fiber(
        multiply(linear(11), linear(19)), multiply(linear(13), linear(17))
    )
    assert (mobius, cross_ratio, pendant_linear, pendant_quadratic) == (1, 2, 2, 2)

    constant_numerator = multiply(linear(3), linear(7))
    constant_denominator = multiply(linear(3), linear(7))
    assert subtract(constant_numerator, constant_denominator, 1) == (0, 0, 0)
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_RESIDUAL_TRANSVERSAL_ATLAS_PASS "
        "fiber_caps=1,2,2,2 constant_mutation=1/1"
    )


if __name__ == "__main__":
    main()
