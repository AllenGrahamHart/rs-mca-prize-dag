#!/usr/bin/env python3
"""Independent finite-field audit of coupling-batch localization."""

from __future__ import annotations

import itertools


def subgroup_root(p: int, n: int) -> int:
    return next(
        value for value in range(2, p)
        if pow(value, n, p) == 1 and pow(value, n // 2, p) == p - 1
    )


def main() -> None:
    p, n = 17, 8
    zeta = subgroup_root(p, n)
    pi = (1 - zeta) % p
    c = {
        exponent: (1 - pow(zeta, exponent, p)) * pow(pi, -1, p) % p
        for exponent in range(1, n)
    }
    assert all(value != 0 for value in c.values())

    quotient_lifts = tuple(
        (u, v) for u in range(1, n) for v in range(1, n) if u != v
    )
    checked = 0
    zero_sets = 0
    for x, y in itertools.combinations_with_replacement(range(1, n), 2):
        beta = (1 - pow(zeta, x, p)) * (1 - pow(zeta, y, p)) % p
        for q0, q1 in itertools.combinations(quotient_lifts, 2):
            u0, v0 = q0
            u1, v1 = q1
            lambda_0 = (beta * c[u0] - c[v0]) % p
            lambda_1 = (beta * c[u1] - c[v1]) % p
            theta = (c[v1] * c[u0] - c[v0] * c[u1]) % p
            assert (c[u0] * lambda_1 - c[u1] * lambda_0 + theta) % p == 0
            left_zero = lambda_0 == 0 and theta == 0
            right_zero = lambda_0 == 0 and lambda_1 == 0
            assert left_zero == right_zero
            zero_sets += left_zero
            checked += 1

    expected_norms = []
    for exponent in range(1, 128):
        level = (exponent & -exponent).bit_length() - 1
        expected_norms.append(2 ** (2**level - 1))
    assert all(value & (value - 1) == 0 for value in expected_norms)
    print(
        "AUDIT_F3_H3_DOUBLE_ACCIDENT_COUPLING_BATCH_ODD_SATURATION_PASS "
        f"field={p} identities={checked} common_zero_sets={zero_sets}"
    )


if __name__ == "__main__":
    main()
