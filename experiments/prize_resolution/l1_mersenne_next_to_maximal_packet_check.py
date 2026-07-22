#!/usr/bin/env python3
"""Exact packet check for the Mersenne h=m-1 outer binomial."""

from __future__ import annotations


ROWS = (
    (8191, 8, (64, 8127), 8100),
    (131071, 8, (130815, 130815), 109166),
    (524287, 8, (523775, 512), 454794),
    (2147483647, 8, (32768, 2147450879), 634005911),
    (8191, 16, (6456, 7379), 6763),
)


def add(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def neg(x: tuple[int, int], p: int) -> tuple[int, int]:
    return (-x[0] % p, -x[1] % p)


def mul(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return ((x[0] * y[0] - x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def power(x: tuple[int, int], exponent: int, p: int) -> tuple[int, int]:
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul(out, x, p)
        x = mul(x, x, p)
        exponent //= 2
    return out


def inverse(x: tuple[int, int], p: int) -> tuple[int, int]:
    denominator = (x[0] * x[0] + x[1] * x[1]) % p
    inv_denominator = pow(denominator, -1, p)
    return (x[0] * inv_denominator % p, -x[1] * inv_denominator % p)


def divide(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return mul(x, inverse(y, p), p)


def quotient_product(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
    coefficient: tuple[int, int],
    constant: tuple[int, int],
    p: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Multiply modulo W^2=coefficient*W+constant."""
    l0, l1 = left
    r0, r1 = right
    cross = mul(l1, r1, p)
    return (
        add(mul(l0, r0, p), mul(cross, constant, p), p),
        add(add(mul(l0, r1, p), mul(l1, r0, p), p),
            mul(cross, coefficient, p), p),
    )


def quotient_power(
    exponent: int,
    coefficient: tuple[int, int],
    constant: tuple[int, int],
    p: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    out = ((1, 0), (0, 0))
    base = ((0, 0), (1, 0))
    while exponent:
        if exponent & 1:
            out = quotient_product(out, base, coefficient, constant, p)
        base = quotient_product(base, base, coefficient, constant, p)
        exponent //= 2
    return out


def gcd_degree(p: int, xi: int, epsilon: tuple[int, int]) -> int:
    """Degree of gcd(P_epsilon, W^(p+1)-epsilon) over F_(p^2)."""
    inv_xi = pow(xi, -1, p)
    coefficient = ((1 - inv_xi) % p, 0)
    constant = (epsilon[0] * inv_xi % p, epsilon[1] * inv_xi % p)
    remainder = quotient_power(p + 1, coefficient, constant, p)
    r0 = add(remainder[0], neg(epsilon, p), p)
    r1 = remainder[1]
    if r1 == (0, 0):
        return 2 if r0 == (0, 0) else 0
    root = divide(neg(r0, p), r1, p)
    value = add(
        add(mul((xi, 0), mul(root, root, p), p),
            mul(((1 - xi) % p, 0), root, p), p),
        neg(epsilon, p),
        p,
    )
    return 1 if value == (0, 0) else 0


def check_row(
    p: int,
    m: int,
    epsilon_generator: tuple[int, int],
    expected_xi: int,
) -> dict[str, object]:
    assert p % 4 == 3
    assert power(epsilon_generator, m, p) == (1, 0)
    assert power(epsilon_generator, m // 2, p) != (1, 0)
    length = m - 2
    constant = (m - 1) * pow(m - 2, -1, p) % p
    assert (p - 1) % length == 0
    xi = pow(constant, (p - 1) // length, p)
    assert xi == expected_xi
    assert pow(xi, length, p) == 1

    degrees = []
    epsilon = (1, 0)
    for index in range(m):
        degree = gcd_degree(p, xi, epsilon)
        if degree:
            degrees.append((index, degree, epsilon))
        epsilon = mul(epsilon, epsilon_generator, p)
    assert degrees == [(0, 1, (1, 0))]
    return {
        "p": p,
        "m": m,
        "h": m - 1,
        "split_roots_required": length,
        "xi": xi,
        "admissible_norm_packets": 1,
        "total_admissible_w_roots": 1,
    }


def main() -> None:
    results = [check_row(*row) for row in ROWS]
    for result in results:
        print(
            "MERSENNE_NEXT_TO_MAX_PACKET_PASS "
            + " ".join(f"{key}={value}" for key, value in result.items())
        )


if __name__ == "__main__":
    main()
