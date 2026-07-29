#!/usr/bin/env python3
"""Independent exact-rational audit of the normalized color reconstruction."""

from __future__ import annotations

from fractions import Fraction as Q


def trim(poly: list[Q]) -> list[Q]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: list[Q], value: Q) -> list[Q]:
    return trim([value * coefficient for coefficient in poly])


def multiply(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def evaluate(poly: list[Q], value: Q) -> Q:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def remainder(numerator: list[Q], denominator: list[Q]) -> list[Q]:
    out = numerator[:]
    while len(out) >= len(denominator):
        factor = out[-1] / denominator[-1]
        shift = len(out) - len(denominator)
        for index, coefficient in enumerate(denominator):
            out[index + shift] -= factor * coefficient
        trim(out)
    return out


def audit() -> None:
    u, v, y = Q(1), Q(2), Q(3)
    beta, gamma, b_value = Q(2), Q(4), Q(7)
    role = (gamma - 1) / (beta - 1)
    quadratic = [v, u, Q(1)]
    q_at_y = evaluate(quadratic, y)
    a = (role - 1) * b_value / q_at_y
    g_factor = multiply(quadratic, [-y, Q(1)])
    f_factor = add(add(g_factor, scale(quadratic, a)), [b_value])
    product = multiply(f_factor, g_factor)
    color = add([Q(1)], scale(f_factor, (beta - 1) / b_value))

    assert add(color, [Q(-1)]) == scale(f_factor, (beta - 1) / b_value)
    assert remainder(add(color, [-beta]), quadratic) == [Q(0)]
    assert evaluate(color, y) == gamma
    value_product = multiply(
        multiply(add(color, [Q(-1)]), add(color, [-beta])),
        add(color, [-gamma]),
    )
    assert remainder(value_product, product) == [Q(0)]
    eta = 1 / (role - 1)
    assert eta == (beta - 1) / (gamma - beta)


def main() -> None:
    audit()
    print("L1_M8_H7_C321_J0_OUTER_LIFT_COMPILER_AUDIT_PASS samples=1")


if __name__ == "__main__":
    main()
