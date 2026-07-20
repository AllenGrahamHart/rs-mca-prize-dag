#!/usr/bin/env python3
"""Divisibility replay for the corrected-square converse on the F_17 fixture."""

from __future__ import annotations


P_FIELD = 17


def inv(value: int) -> int:
    return pow(value % P_FIELD, P_FIELD - 2, P_FIELD)


def trim(poly: list[int]) -> list[int]:
    out = poly[:]
    while len(out) > 1 and out[-1] % P_FIELD == 0:
        out.pop()
    return [value % P_FIELD for value in out]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P_FIELD
    return trim(out)


def locator(roots: tuple[int, ...]) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % P_FIELD, 1])
    return out


def evaluate(poly: list[int], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P_FIELD
    return value


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    work = trim(dividend)
    divisor = trim(divisor)
    if len(work) < len(divisor):
        return [0], work
    quotient = [0] * (len(work) - len(divisor) + 1)
    while len(work) >= len(divisor) and work != [0]:
        degree = len(work) - len(divisor)
        scale = work[-1] * inv(divisor[-1]) % P_FIELD
        quotient[degree] = scale
        for i, coefficient in enumerate(divisor):
            work[degree + i] = (work[degree + i] - scale * coefficient) % P_FIELD
        work = trim(work)
    return trim(quotient), work


def main() -> None:
    roots_a = (2, 5)
    roots_b = (3, 13, 15)
    external = {15: (4, 9, 11), 2: (6, 7, 10), 4: (8, 12, 16)}
    supported = (0, 1, 2, 4, 15)
    ordinary = (1, 2, 4, 15)
    omitted = 14
    saturated = tuple(x for x in range(2, P_FIELD) if x != omitted)

    a = locator(roots_a) + [0]
    b = locator(roots_b)
    q_1 = [(right - left) % P_FIELD for left, right in zip(a, b, strict=True)]
    p_slope = locator(supported)
    p_clean = locator(ordinary)
    p_x = locator(saturated)

    # Every saturated row gives an exact degree-one divisor of P(z).
    row_quotients = {}
    for x in saturated:
        q_x = trim([evaluate(a, x), evaluate(q_1, x)])
        quotient, remainder = divide(p_slope, q_x)
        assert remainder == [0]
        assert len(quotient) - 1 == 4
        row_quotients[x] = quotient

    # The omitted row has no finite supported root and drops parameter degree.
    q_omitted = trim([evaluate(a, omitted), evaluate(q_1, omitted)])
    assert len(q_omitted) - 1 == 0

    # Every ordinary fiber gives an exact cubic divisor of P_X(X).
    column_quotients = {}
    expected_roots = {1: roots_b} | external
    for z in ordinary:
        q_z = trim([(left + z * right) % P_FIELD for left, right in zip(a, q_1, strict=True)])
        quotient, remainder = divide(p_x, q_z)
        assert remainder == [0]
        assert len(q_z) - 1 == 3
        assert len(quotient) - 1 == 11
        assert {x for x in saturated if evaluate(q_z, x) == 0} == set(expected_roots[z])
        column_quotients[z] = quotient

    # No clean parameter factor divides all coefficients of Q.
    for z in ordinary:
        q_z = [(left + z * right) % P_FIELD for left, right in zip(a, q_1, strict=True)]
        assert any(q_z)

    # Replacing one saturated point by the omitted row breaks a clean divisor.
    mutated_roots = tuple(x for x in saturated if x != 4) + (omitted,)
    mutated_p_x = locator(mutated_roots)
    q_external = trim([(left + 15 * right) % P_FIELD for left, right in zip(a, q_1, strict=True)])
    _, mutated_remainder = divide(mutated_p_x, q_external)
    assert mutated_remainder != [0]

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_CORRECTED_SQUARE_CONVERSE_PASS "
        f"field={P_FIELD} row_divisors={len(row_quotients)} "
        f"column_divisors={len(column_quotients)} omitted={omitted}"
    )


if __name__ == "__main__":
    main()
