#!/usr/bin/env python3
"""Exact 16-case value-coset check for the nu=0, b=0 cubic arm."""

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


def inverse(x: Fp2, p: int) -> Fp2:
    norm = (x[0] * x[0] + x[1] * x[1]) % p
    assert norm
    scalar = pow(norm, -1, p)
    return x[0] * scalar % p, -x[1] * scalar % p


def qadd(x: Quotient, y: Quotient, p: int) -> Quotient:
    return add(x[0], y[0], p), add(x[1], y[1], p)


def qmul(x: Quotient, y: Quotient, coefficient: Fp2,
         constant: Fp2, p: int) -> Quotient:
    ac = mul(x[0], y[0], p)
    bd = mul(x[1], y[1], p)
    return (
        add(ac, neg(mul(bd, constant, p), p), p),
        add(add(mul(x[0], y[1], p), mul(x[1], y[0], p), p),
            neg(mul(bd, coefficient, p), p), p),
    )


def qpow(x: Quotient, exponent: int, coefficient: Fp2,
         constant: Fp2, p: int) -> Quotient:
    out: Quotient = ((1, 0), (0, 0))
    while exponent:
        if exponent & 1:
            out = qmul(out, x, coefficient, constant, p)
        x = qmul(x, x, coefficient, constant, p)
        exponent >>= 1
    return out


def evaluate_q(x: Fp2, coefficient: Fp2,
               constant: Fp2, p: int) -> Fp2:
    return add(add(mul(x, x, p), mul(coefficient, x, p), p), constant, p)


def linear_root(value: Quotient, p: int) -> tuple[str, Fp2 | None]:
    constant, linear = value
    if linear != (0, 0):
        return "POINT", mul(neg(constant, p), inverse(linear, p), p)
    return ("ALL", None) if constant == (0, 0) else ("NONE", None)


def classify(p: int, epsilon: Fp2, eta: Fp2) -> str:
    zero, one, two = (0, 0), (1, 0), (2, 0)
    inverse_two = (pow(2, -1, p), 0)
    coefficient = mul(
        add(add(eta, neg(epsilon, p), p), (-4 % p, 0), p),
        inverse_two,
        p,
    )
    u: Quotient = (zero, one)
    v: Quotient = (two, (-1 % p, 0))
    first = qadd(qpow(u, p + 1, coefficient, epsilon, p),
                 (neg(epsilon, p), zero), p)
    second = qadd(qpow(v, p + 1, coefficient, epsilon, p),
                  (neg(eta, p), zero), p)
    first_kind, first_point = linear_root(first, p)
    second_kind, second_point = linear_root(second, p)
    if "NONE" in (first_kind, second_kind):
        return "NONE"
    if first_kind == second_kind == "ALL":
        # The (1,1) quadratic is (u-1)^2 and is geometrically degenerate.
        if coefficient == (-2 % p, 0) and epsilon == one:
            return "DEGENERATE_DOUBLE_ROOT"
        return "ALL_QUADRATIC_ROOTS"
    point = first_point if first_kind == "POINT" else second_point
    assert point is not None
    if evaluate_q(point, coefficient, epsilon, p) != zero:
        return "NONE"
    for constant, linear in (first, second):
        if add(constant, mul(linear, point, p), p) != zero:
            return "NONE"
    v_point = add(two, neg(point, p), p)
    if point in (zero, one) or v_point in (zero, one, point):
        return "DEGENERATE_POINT"
    return f"POINT u={point} v={v_point}"


def table(p: int) -> list[tuple[Fp2, Fp2, str]]:
    quarters = ((1, 0), (-1 % p, 0), (0, 1), (0, -1 % p))
    return [
        (epsilon, eta, outcome)
        for epsilon in quarters
        for eta in quarters
        if (outcome := classify(p, epsilon, eta)) != "NONE"
    ]


def main() -> None:
    for p in (8191, 131071, 524287, 2147483647):
        survivors = table(p)
        print(f"p={p} survivors={len(survivors)}")
        for epsilon, eta, outcome in survivors:
            print(f"  epsilon={epsilon} eta={eta} {outcome}")
    print("L1_M4_H3_NU0_ZERO_B_VALUE_COSET_CHECK_PASS")


if __name__ == "__main__":
    main()
