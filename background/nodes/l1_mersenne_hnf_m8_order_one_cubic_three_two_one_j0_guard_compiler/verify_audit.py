#!/usr/bin/env python3
"""Independent exact-rational audit for the J-zero guard compiler."""

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


def scale(poly: list[Q], scalar: Q) -> list[Q]:
    return trim([scalar * value for value in poly])


def multiply(left: list[Q], right: list[Q]) -> list[Q]:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def divmod_poly(left: list[Q], right: list[Q]) -> tuple[list[Q], list[Q]]:
    remainder = trim(left[:])
    divisor = trim(right[:])
    quotient = [Q(0)] * max(1, len(remainder) - len(divisor) + 1)
    while remainder != [Q(0)] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[shift] += factor
        for index, value in enumerate(divisor):
            remainder[index + shift] -= factor * value
        trim(remainder)
    return trim(quotient), remainder


def gcd(left: list[Q], right: list[Q]) -> list[Q]:
    while right != [Q(0)]:
        left, right = right, divmod_poly(left, right)[1]
    return scale(left, 1 / left[-1])


def derivative(poly: list[Q]) -> list[Q]:
    return trim([Q(index) * value for index, value in enumerate(poly)][1:])


def evaluate(poly: list[Q], value: Q) -> Q:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def main() -> None:
    x, y, v, a_scaled = Q(1), Q(3), Q(2), Q(5)
    eta, beta = Q(1, 2), Q(2)
    gamma = beta + (beta - 1) / eta
    qhat = [v, x + y, Q(1)]
    qy = evaluate(qhat, y)
    role_r = a_scaled * qy
    s_value = eta * role_r
    ghat = multiply(qhat, [-y, Q(1)])
    fhat = add(add(ghat, scale(qhat, a_scaled)), [s_value])
    lhat = multiply(fhat, ghat)
    color = add([Q(1)], scale(fhat, (beta - 1) / s_value))

    assert gamma == Q(4)
    assert gcd(lhat, add(color, [Q(-1)])) == scale(fhat, 1 / fhat[-1])
    assert gcd(lhat, add(color, [-beta])) == qhat
    assert gcd(lhat, add(color, [-gamma])) == [-y, Q(1)]
    assert gcd(qhat, derivative(qhat)) == [Q(1)]
    assert gcd(fhat, derivative(fhat)) == [Q(1)]
    assert evaluate(lhat, Q(-1)) != 0

    d = Q(7)
    lam = 1 + 1 / eta
    common_guard = (
        (a_scaled / d)
        * (s_value / d**3)
        * (lam - 1)
        * (qy / d**2)
    )
    assert common_guard == role_r**2 / d**6
    print("L1_M8_H7_C321_J0_GUARD_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
