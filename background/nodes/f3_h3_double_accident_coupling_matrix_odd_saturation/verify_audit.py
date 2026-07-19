#!/usr/bin/env python3
"""Independent finite-field audit of coupling-matrix cross generation."""

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
    pi_squared_inverse = pow(pi * pi % p, -1, p)
    c = {
        exponent: (1 - pow(zeta, exponent, p)) * pow(pi, -1, p) % p
        for exponent in range(1, n)
    }
    products = tuple(itertools.combinations_with_replacement(range(1, n), 2))
    beta = {
        pair: (1 - pow(zeta, pair[0], p)) * (1 - pow(zeta, pair[1], p)) % p
        for pair in products
    }
    quotients = tuple((u, v) for u in range(1, n) for v in range(1, n) if u != v)
    coupling = {
        (pair, quotient): (beta[pair] * c[quotient[0]] - c[quotient[1]]) % p
        for pair in products for quotient in quotients
    }

    checked = 0
    common_zeros = 0
    for e0, e1 in itertools.combinations(products, 2):
        alpha = (beta[e1] - beta[e0]) * pi_squared_inverse % p
        for q0, q1 in itertools.combinations(quotients, 2):
            theta = (c[q1[1]] * c[q0[0]] - c[q0[1]] * c[q1[0]]) % p
            lambda_00 = coupling[e0, q0]
            lambda_10 = coupling[e1, q0]
            lambda_01 = coupling[e0, q1]
            lambda_11 = coupling[e1, q1]
            joint_zero = lambda_00 == alpha == theta == 0
            cross_zero = lambda_00 == lambda_10 == lambda_01 == 0
            rectangle_zero = cross_zero and lambda_11 == 0
            assert joint_zero == cross_zero == rectangle_zero
            common_zeros += joint_zero
            checked += 1

    assert checked == 325458
    print(
        "AUDIT_F3_H3_DOUBLE_ACCIDENT_COUPLING_MATRIX_ODD_SATURATION_PASS "
        f"field={p} ideal_tests={checked} common_zeros={common_zeros}"
    )


if __name__ == "__main__":
    main()
