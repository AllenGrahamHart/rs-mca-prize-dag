#!/usr/bin/env python3
"""Exact finite-field checks for the harmonic spectral quadratic gate."""

from itertools import combinations, permutations, product


PAIRINGS = (
    ((0, 1), (2, 3)),
    ((0, 2), (1, 3)),
    ((0, 3), (1, 2)),
)


def pairing_form(roots, pairing, p):
    (i, j), (k, ell) = pairing
    return (
        2 * (roots[i] * roots[j] + roots[k] * roots[ell])
        - (roots[i] + roots[j]) * (roots[k] + roots[ell])
    ) % p


def direct_sign_norm(roots, pairing, p):
    answer = 1
    for signs in product((1, -1), repeat=3):
        signed = [roots[0]] + [signs[i - 1] * roots[i] % p for i in range(1, 4)]
        answer = answer * pairing_form(signed, pairing, p) % p
    return answer


def coefficient_norm(square_roots, pairing, p, mutate=False):
    (i, j), (k, ell) = pairing
    x, y, z, t = (
        square_roots[i],
        square_roots[j],
        square_roots[k],
        square_roots[ell],
    )
    s = (x + y) % p
    q = x * y % p
    capital_t = (z + t) % p
    u = z * t % p
    a = (4 * q + 4 * u - s * capital_t) % p
    last_coefficient = 15 if mutate else 16
    c0 = (
        a * a
        + 4 * capital_t * capital_t * q
        - 4 * u * s * s
        - last_coefficient * u * q
    ) % p
    c1 = (-4 * a * capital_t + 16 * u * s) % p
    return (c0 * c0 - q * c1 * c1) % p


def multiply_quadratics(s, q, t, u, p):
    # Coefficients in ascending order of Y.
    left = [q % p, -s % p, 1]
    right = [u % p, -t % p, 1]
    out = [0] * 5
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


def check_all_small_supports():
    p = 17
    representatives = list(range(1, 9))
    for roots in combinations(representatives, 4):
        squares = [root * root % p for root in roots]
        assert len(set(squares)) == 4
        for pairing in PAIRINGS:
            expected = direct_sign_norm(roots, pairing, p)
            assert coefficient_norm(squares, pairing, p) == expected


def check_factor_order_invariance():
    p = 97
    roots = [1, 2, 3, 4]
    squares = [root * root % p for root in roots]
    baseline = coefficient_norm(squares, PAIRINGS[0], p)
    assert baseline != 0
    preserving_orders = (
        (0, 1, 2, 3),
        (1, 0, 2, 3),
        (0, 1, 3, 2),
        (2, 3, 0, 1),
        (3, 2, 1, 0),
    )
    for order in preserving_orders:
        reordered = [squares[i] for i in order]
        assert coefficient_norm(reordered, PAIRINGS[0], p) == baseline

    (i, j), (k, ell) = PAIRINGS[0]
    first = multiply_quadratics(
        (squares[i] + squares[j]) % p,
        squares[i] * squares[j] % p,
        (squares[k] + squares[ell]) % p,
        squares[k] * squares[ell] % p,
        p,
    )
    for order in preserving_orders:
        values = [squares[index] for index in order]
        other = multiply_quadratics(
            (values[0] + values[1]) % p,
            values[0] * values[1] % p,
            (values[2] + values[3]) % p,
            values[2] * values[3] % p,
            p,
        )
        assert other == first


def check_harmonic_witness_and_mutation():
    p = 97
    roots = [1, 27, 12, 75]
    squares = [root * root % p for root in roots]
    assert len(set(squares)) == 4
    assert any(coefficient_norm(squares, pairing, p) == 0 for pairing in PAIRINGS)

    fixture = [1, 4, 9, 16]
    assert coefficient_norm(fixture, PAIRINGS[0], p) != coefficient_norm(
        fixture, PAIRINGS[0], p, mutate=True
    )


def main():
    check_all_small_supports()
    check_factor_order_invariance()
    check_harmonic_witness_and_mutation()
    print("PASS pure harmonic spectral quadratic gate")


if __name__ == "__main__":
    main()
