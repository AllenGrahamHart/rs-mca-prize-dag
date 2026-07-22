#!/usr/bin/env python3
"""Exact 16-case check for three depressed values in the Mersenne 2-group."""

from __future__ import annotations


Fp2 = tuple[int, int]
Quotient = tuple[Fp2, Fp2]


def add(x: Fp2, y: Fp2, p: int) -> Fp2:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def neg(x: Fp2, p: int) -> Fp2:
    return (-x[0] % p, -x[1] % p)


def mul(x: Fp2, y: Fp2, p: int) -> Fp2:
    return ((x[0] * y[0] - x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def inv(x: Fp2, p: int) -> Fp2:
    denominator = (x[0] * x[0] + x[1] * x[1]) % p
    assert denominator
    inverse = pow(denominator, -1, p)
    return (x[0] * inverse % p, -x[1] * inverse % p)


def qadd(x: Quotient, y: Quotient, p: int) -> Quotient:
    return (add(x[0], y[0], p), add(x[1], y[1], p))


def qmul(x: Quotient, y: Quotient, coefficient: Fp2,
         constant: Fp2, p: int) -> Quotient:
    ac = mul(x[0], y[0], p)
    bd = mul(x[1], y[1], p)
    const = add(ac, neg(mul(bd, constant, p), p), p)
    linear = add(add(mul(x[0], y[1], p), mul(x[1], y[0], p), p),
                 neg(mul(bd, coefficient, p), p), p)
    return const, linear


def qpow(x: Quotient, exponent: int, coefficient: Fp2,
         constant: Fp2, p: int) -> Quotient:
    output: Quotient = ((1, 0), (0, 0))
    while exponent:
        if exponent & 1:
            output = qmul(output, x, coefficient, constant, p)
        x = qmul(x, x, coefficient, constant, p)
        exponent >>= 1
    return output


def evaluate_quadratic(x: Fp2, coefficient: Fp2,
                       constant: Fp2, p: int) -> Fp2:
    return add(add(mul(x, x, p), mul(coefficient, x, p), p), constant, p)


def linear_candidate(remainder: Quotient, p: int) -> tuple[str, Fp2 | None]:
    constant, linear = remainder
    if linear != (0, 0):
        return "point", mul(neg(constant, p), inv(linear, p), p)
    return ("all", None) if constant == (0, 0) else ("none", None)


def classify(p: int, epsilon: Fp2, eta: Fp2) -> str:
    one = (1, 0)
    coefficient = add(add(one, epsilon, p), neg(eta, p), p)
    u: Quotient = ((0, 0), (1, 0))
    v: Quotient = ((-1 % p, 0), (-1 % p, 0))
    u_power = qpow(u, p + 1, coefficient, epsilon, p)
    v_power = qpow(v, p + 1, coefficient, epsilon, p)
    first = qadd(u_power, (neg(epsilon, p), (0, 0)), p)
    second = qadd(v_power, (neg(eta, p), (0, 0)), p)
    kind_first, point_first = linear_candidate(first, p)
    kind_second, point_second = linear_candidate(second, p)
    if "none" in (kind_first, kind_second):
        return "NONE"
    if kind_first == "all" and kind_second == "all":
        return "ALL_QUADRATIC_ROOTS"
    point = point_first if kind_first == "point" else point_second
    assert point is not None
    if evaluate_quadratic(point, coefficient, epsilon, p) != (0, 0):
        return "NONE"
    if kind_first == "point" and point != point_first:
        return "NONE"
    if kind_second == "point" and point != point_second:
        return "NONE"
    one_value = one
    v_value = add(neg(one, p), neg(point, p), p)
    if point in ((0, 0), one_value) or v_value in ((0, 0), one_value, point):
        return "DEGENERATE_POINT"
    return f"POINT u={point} v={v_value}"


def main() -> None:
    primes = (8191, 131071, 524287, 2147483647)
    for p in primes:
        assert p % 4 == 3
        quarters = ((1, 0), (-1 % p, 0), (0, 1), (0, -1 % p))
        survivors = []
        for epsilon in quarters:
            for eta in quarters:
                outcome = classify(p, epsilon, eta)
                if outcome != "NONE":
                    survivors.append((epsilon, eta, outcome))
        print(f"p={p} survivors={len(survivors)}")
        for epsilon, eta, outcome in survivors:
            print(f"  epsilon={epsilon} eta={eta} {outcome}")


if __name__ == "__main__":
    main()
